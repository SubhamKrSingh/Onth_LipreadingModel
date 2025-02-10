# ONTH Lipreading Model

ONTH is an advanced lip-reading model designed to accurately interpret and transcribe spoken words by analyzing the movements of a person's lips. This repository provides a Keras implementation of the method described in the paper "LipNet: End-to-End Sentence-level Lipreading" by Yannis M. Assael, Brendan Shillingford, Shimon Whiteson, and Nando de Freitas ([https://arxiv.org/abs/1611.01599](https://arxiv.org/abs/1611.01599)).

## Demo

A demonstration of the model's capabilities can be viewed on LinkedIn: [https://www.linkedin.com/posts/subhamsingh02_lipreading-ai-machinelearning-activity-7294804057532116994-mIaS](https://www.linkedin.com/posts/subhamsingh02_lipreading-ai-machinelearning-activity-7294804057532116994-mIaS)

![LipNet performing prediction (subtitle alignment only for visualization)](/lipreading.gif)

## Overview

This project implements a lip-reading model based on the LipNet architecture.  It aims to translate video sequences of lip movements into corresponding text.  The model is trained on a dataset of videos and their transcriptions, learning to map visual features to linguistic output.

![Image](https://github.com/user-attachments/assets/635fb032-664a-4967-bc6a-a9ff2dfdb355)

## Results

The model's performance is evaluated using metrics like Character Error Rate (CER), Word Error Rate (WER), and BLEU score.  The following table summarizes the results achieved on different test scenarios:

| Scenario             | Epoch | CER   | WER    | BLEU   |
|----------------------|-------|-------|--------|--------|
| Unseen speakers [C]  | N/A   | N/A   | N/A    | N/A    |
| Unseen speakers      | 178   | 6.19% | 14.19% | 88.21% |
| Overlapped speakers [C]| N/A   | N/A   | N/A    | N/A    |
| Overlapped speakers  | 368   | 1.56% | 3.38%  | 96.93% |

*Note:  "[C]" likely indicates a specific condition or subset of the data.  More details about these scenarios would be beneficial.*

## Dataset

This model utilizes the GRID corpus ([http://spandh.dcs.shef.ac.uk/gridcorpus/](http://spandh.dcs.shef.ac.uk/gridcorpus/)).  This dataset provides a collection of videos of people speaking simple sentences, along with their corresponding text transcriptions.

## Pre-trained Weights

For convenience, pre-trained weights are available for download.  These weights can be used to quickly test the model or as a starting point for further training. You can download them from this link: [https://drive.google.com/uc?id=1vWscXs4Vt0a_1IH1-ct2TCgXAZT-N3_Y](https://drive.google.com/uc?id=1vWscXs4Vt0a_1IH1-ct2TCgXAZT-N3_Y)

## Installation (Optional - Add details if applicable)

*(Include instructions on how to set up the environment and install dependencies.  For example:)*

```bash
pip install -r requirements.txt

