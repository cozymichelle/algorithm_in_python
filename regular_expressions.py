'''
Pre-process texts using the regular expression opreations re
'''

import re

from nltk.stem.porter import PorterStemmer
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# Return a processed text, given a raw text
def clean_text(txt:str) -> str:
    # replace various whitespace with a single whitespace
    txt = re.sub('\s+', ' ', txt)
    
    # cast all text to lower case
    txt = txt.lower()
    
    # replace common abbreviations with their full form
    txt = re.sub(r'([a-z]+)\'s([^a-z]|$)', r'\1 is ', txt)
    txt = re.sub(r'([a-z]+)n\'t([^a-z]|$)', r'\1 not ', txt)
    txt = re.sub(r'([a-z]+)n\'([^a-z]|$)', r'\1 not ', txt)
    txt = re.sub(r'([a-z]+)\'re([^a-z]|$)', r'\1 are ', txt)
    txt = re.sub(r'([a-z]+)\'ll([^a-z]|$)', r'\1 will ', txt)
    txt = re.sub(r'([a-z]+)\'d([^a-z]|$)', r'\1 had ', txt)
    txt = re.sub(r'([a-z]+)\'ve([^a-z]|$)', r'\1 have ', txt)
    txt = re.sub('i\'m([^a-z]|$)', 'i am ', txt)
    txt = re.sub('let\'s([^a-z]|$)', 'let us', txt)
    return txt


# Extract sentences that have given regular expression
def extract_sentences(regular_expression:str, text:str) -> list:
    return [m.group() for m in re.finditer(regular_expression,text)]


# Replace punctuations with a single whitespace
def remove_punctuation(txt:str) -> str:
    return re.sub(r'[^a-zA-Z0-9]+', ' ', txt)


# Split a given text, based on whitespace
def tokenize(text: str) -> list:
    return text.split()