# Import all of the dependencies
import streamlit as st
import os 
import imageio 
import numpy as np
import tensorflow as tf 
from utils import load_data, num_to_char
from modelutil import load_model
import subprocess

def display_video(file_path):
    # Create 'temp' directory if it doesn't exist
    temp_dir = 'temp'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        
    # Convert to absolute path
    file_path = os.path.abspath(file_path)
    output_path = os.path.join(temp_dir, f'temp_{os.path.basename(file_path)}.mp4')
    
    try:
        # Check if input file exists
        if not os.path.exists(file_path):
            st.error(f"Input video file not found: {file_path}")
            return
            
        # Print paths for debugging
        st.text(f"Input path: {file_path}")
        st.text(f"Output path: {output_path}")
        
        result = subprocess.run([
            'ffmpeg', '-y',
            '-i', str(file_path),
            '-c:v', 'libx264',
            '-preset', 'medium',
            '-crf', '23',
            str(output_path)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            with open(output_path, 'rb') as video_file:
                video_bytes = video_file.read()
            st.video(video_bytes)
        else:
            st.error(f"FFmpeg error: {result.stderr}")
            
    except Exception as e:
        st.error(f"Error displaying video: {str(e)}")
        st.text(f"Current working directory: {os.getcwd()}")
    finally:
        if os.path.exists(output_path):
            os.remove(output_path)

def display_processed_frames(video_tensor):
    try:
        temp_dir = 'temp'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
            
        gif_path = os.path.join(temp_dir, f'animation_{str(np.random.randint(1000))}.gif')
        
        video_array = video_tensor.numpy()
        
        if len(video_array.shape) == 4:
            video_array = video_array[..., 0]
        elif len(video_array.shape) == 5:
            video_array = video_array[0, ..., 0]
            
        video_array = np.clip(video_array * 255, 0, 255).astype(np.uint8)
        frames = [frame.squeeze() for frame in video_array]
        
        imageio.mimsave(gif_path, frames, fps=10)
        st.image(gif_path, width=400)
        
        if os.path.exists(gif_path):
            os.remove(gif_path)
            
    except Exception as e:
        st.error(f"Error displaying processed frames: {str(e)}")

def process_video(col1, col2, selected_video):
    try:
        file_path = os.path.join('..', 'data', 's1', selected_video)
        if not os.path.exists(file_path):
            st.error(f"Video file not found: {file_path}")
            return None

        with col1:
            st.info('The video below displays the converted video in mp4 format')
            display_video(file_path)

        with col2:
            st.info('This is all the machine learning model sees when making a prediction')
            video_tensor, annotations = load_data(tf.convert_to_tensor(file_path))
            display_processed_frames(video_tensor)
            return video_tensor

    except Exception as e:
        st.error(f"Error in processing: {str(e)}")
        return None

# Set the layout to the streamlit app as wide 
st.set_page_config(page_title="LipNet", layout="wide")

# Setup the sidebar
with st.sidebar: 
    st.image('https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png')
    st.title('LipBuddy')
    st.info('This application is originally developed from the LipNet deep learning model.')

st.title('LipNet Full Stack App') 

# Generate two columns 
col1, col2 = st.columns(2)

# Generating a list of options or videos 
options = os.listdir(os.path.join('..', 'data', 's1'))
selected_video = st.selectbox('Choose video', options)

if selected_video:
    video_tensor = process_video(col1, col2, selected_video)
    
    if video_tensor is not None:
        st.info('This is the output of the machine learning model as tokens')
        model = load_model()
        yhat = model.predict(tf.expand_dims(video_tensor, axis=0))
        decoder = tf.keras.backend.ctc_decode(yhat, [75], greedy=True)[0][0].numpy()
        st.text(decoder)

        st.info('Decode the raw tokens into words')
        converted_prediction = tf.strings.reduce_join(num_to_char(decoder)).numpy().decode('utf-8')
        st.text(converted_prediction)
        