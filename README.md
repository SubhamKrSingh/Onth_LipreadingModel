![Image](https://github.com/user-attachments/assets/635fb032-664a-4967-bc6a-a9ff2dfdb355)
# Onth Lipreading Model
ONTH is an advanced lip-reading model designed to accurately interpret and transcribe spoken words by analyzing the movements of a person's lips.
Keras implementation of the method described in the paper 'LipNet: End-to-End Sentence-level Lipreading' by Yannis M. Assael, Brendan Shillingford, Shimon Whiteson, and Nando de Freitas (https://arxiv.org/abs/1611.01599).



![LipNet performing prediction (subtitle alignment only for visualization)](/lipreading.gif)

## Results
|       Scenario          | Epoch |  CER  |  WER  |  BLEU |
|:-----------------------:|:-----:|:-----:|:-----:|:-----:|
|  Unseen speakers [C]    |  N/A  |  N/A  |  N/A  |  N/A  |
|    Unseen speakers      |  178  |  6.19%  |  14.19%  |  88.21%  |
| Overlapped speakers [C] |  N/A  |  N/A  |  N/A  |  N/A  |
|   Overlapped speakers   |  368  |  1.56%  |  3.38%  |  96.93%  |

## Dataset
This model uses GRID corpus (http://spandh.dcs.shef.ac.uk/gridcorpus/)
## Pre-trained weights
For those of you who are having difficulties in training the model (or just want to see the end results), you can download and use the weights provided here (https://drive.google.com/uc?id=1vWscXs4Vt0a_1IH1-ct2TCgXAZT-N3_Y)


