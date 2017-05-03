# extractive-summarizer
Extractive Summarizer using LexRank.

## Setup

**Import the repository folder into Pycharm**

## Testing Locally

1. **Download CNN datasets into project directory**
    
    [Dataset](https://docs.google.com/uc?id=0B0Obe9L1qtsnSXZEd0JCenIyejg&export=download)

2. **Train summarizer** 
    Use training-summarizer.py on the training dataset - This application calculates the inverse document frequencies (idf) of every word in the training dataset.
    
    usage: training-summarizer [-h] TRAINING_DIRECTORY OUTPUT_FILE
3. **Summarize test file**
    Use test-summarizer.py on test dataset - This application summarizes a given article using previously calculated
inverse document frequencies (idf).
    
    usage: test-summarizer [-h] IDF_FILE ORIGINAL_FILE

## Dev Guide

1. **Pull/Sync master for latest code**

2. **Create new feature branch from master**

3. **Code out the feature on the new feature branch, test locally**

4. **When finished, pull/sync master again**

5. **Update feature branch from master, resolve conflicts**

6. **Merge feature branch into master locally**

7. **Push/Sync master**