# Data Extraction and Analysis

## Description
This project involves extracting data from a list of URLs related to AI in healthcare articles and performing data analysis on the extracted text. The analysis includes sentiment analysis, computation of various variables such as word count, sentence count, average sentence length, percentage of complex words, and more.

## Dependencies
1. `Python 3.x`

2. `pandas`

3. `nltk (Natural Language Toolkit)`

4. `newspaper3k`

5. `syllables`

## Installation
1. Install Python: [`Python Installation Guide`](https://www.python.org/downloads/)

2. Install the required libraries using pip:
```
pip install pandas nltk newspaper3k syllables
```

3. Download NLTK data:
```
import nltk
nltk.download('punkt')
```

## Usage
1. Clone or download the project repository.

2. Place the input file "input.xlsx" in the same directory as the Python script.

3. Run the Python script:
```
blackcoffer_internship_task.py
```

4. The output file "output.csv" will be generated in the same directory.

## Notes
1. The input file should follow the structure specified in "Input Data Structure.xlsx".

2. If any error occurs during data extraction or analysis, an error message will be displayed, and the script will continue to process the remaining URLs.

3. The output file will contain the computed variables and sentiment analysis scores for each URL in the input file.

4. Please note that the sentiment analysis scores are based on the VADER sentiment analysis tool and may not always perfectly reflect the sentiment of the article.
