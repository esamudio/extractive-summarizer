# extractive-summarizer
Extractive-Summarizer using LexRank.

## Setup

1. **Import the repository folder into Pycharm**
    
2. **Download CNN datasets into project directory**

    [Dataset](https://docs.google.com/uc?id=0B0Obe9L1qtsnSXZEd0JCenIyejg&export=download)

## Usage

1. **Train summarizer** 
    Use training-summarizer.py on the training dataset - This application calculates the inverse document frequencies (idf) of every word in the training dataset.
    
    usage: training-summarizer [-h] TRAINING_DIRECTORY OUTPUT_FILE
2. **Summarize test file**
    Use test-summarizer.py on test dataset - This application summarizes a given article using previously calculated
inverse document frequencies (idf).
    
    usage: test-summarizer [-h] IDF_FILE ORIGINAL_FILE

    **note:** delete .summary files if recreating summaries
3. **Evaluator**
    Use test-evaluator.py on summarized files - This application evaluates our LexRank summarizer using the sentence labels provided in the dataset.

    usage: test-evaluator [-h] SUMMARIES_DIRECTORY

## Dev Guide

1. **Pull/Sync master for latest code**

2. **Create new feature branch from master**

3. **Code out the feature on the new feature branch, test locally**

4. **When finished, pull/sync master again**

5. **Update feature branch from master, resolve conflicts**

6. **Merge feature branch into master locally**

7. **Push/Sync master**