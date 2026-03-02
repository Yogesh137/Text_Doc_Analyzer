# Text Document Analyzer
## Overview

This project implements a modular text analysis system in Python that processes a plain text file and generates comprehensive word statistics.

The system performs text normalization, filters irrelevant words, computes frequency distributions, and produces structured statistical output. The design emphasizes separation of concerns and clean data processing.

## Features

Reads and normalizes plain text input

Converts text to lowercase

Removes punctuation (keeps alphanumeric characters and spaces only)

Ignores words with fewer than 3 characters

Excludes common stop words

Computes:

- Total word count

- Unique word count

- Average word length

- Longest word

- Most frequent word

Provides:

- Top N most frequent words

- Words starting with a specific prefix

- Exports a formatted report to a text file

## Project Structure

Text_Doc_Analyzer/
│
├── text_reader.py
├── word_counter.py
├── statistics_report.py
├── sample.txt
└── main.py

### text_reader.py

Responsible for:

- Reading file content

- Normalizing text using regular expressions

- Converting text to lowercase

- Removing punctuation

### word_counter.py

Responsible for:

- Tokenizing normalized text

- Filtering stop words

- Ignoring short words (< 3 characters)

- Building a frequency dictionary

### statistics_report.py

Responsible for:

- Computing statistical metrics

- Sorting and retrieving top N words

- Performing prefix-based word filtering

- Exporting formatted analysis report

### main.py

- Demonstrates complete workflow:

- Read and normalize file

- Count word frequencies

- Generate statistics
  
- print results
  
- export the report

Print resul
E
