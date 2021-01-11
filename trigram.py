'''
A tri-gram model
'''

from nltk.stem.porter import PorterStemmer
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from random import sample

class TriGram:
    def __init__(self):
        self.unigrams_idx = dict()
        self.bigrams_idx = dict()
    
    def extract_word_ngrams(self, data, num):
        n_grams = ngrams(nltk.word_tokenize(data), num)
        return [ ' '.join(grams) for grams in n_grams]
    
    def keep_counts(self, ngrams):
        counts = dict()
        for ngram in ngrams:
            counts[ngram] = counts.get(ngram, 0) + 1
        return counts
        
    def train(self, data, smoothing_lambda, verbose = False):
        if verbose:
            print('Extract ngrams')
        
        unigrams = []
        bigrams = []
        trigrams = []
        for d in data:
            d = d.lower()
            d = re.sub(r'[^a-zA-Z0-9\.\?\!]', ' ', d)
            unigrams += self.extract_word_ngrams(d, 1)
            bigrams += self.extract_word_ngrams(d, 2)
            trigrams += self.extract_word_ngrams(d, 3)
            
        if verbose:
            print('Count trigrams')
        
        tri_counts = self.keep_counts(trigrams)
        
        if verbose:
            print('Initialize the probability dictionary')
        
        unigrams_vocab = list(set(unigrams))
        bigrams_vocab = list(set(bigrams))
        bigrams_vocab_size = len(bigrams_vocab)
        unigrams_vocab_size = len(unigrams_vocab)

        self.probs = np.full((bigrams_vocab_size, unigrams_vocab_size), smoothing_lambda)
        row_sum = np.full(bigrams_vocab_size, unigrams_vocab_size * smoothing_lambda)
        
        for i, unigram in enumerate(unigrams_vocab):
            self.unigrams_idx[unigram] = i
        for i, bigram in enumerate(bigrams_vocab):
            self.bigrams_idx[bigram] = i
            
        if verbose:
            print('Convert the count to probabilities')
        
        for ngram, count in tri_counts.items():
            tokens = ngram.split()
            given_token = ' '.join(tokens[:2])
            given_token_idx = self.bigrams_idx[given_token]
            next_token_idx = self.unigrams_idx[tokens[-1]]
            self.probs[given_token_idx][next_token_idx] += count
            row_sum[given_token_idx] += count
        
        for i in range(bigrams_vocab_size):
            self.probs[i] = self.probs[i] / row_sum[i]
    
    def sample_next_gram(self, given_token):
        if given_token in self.bigrams_idx:
            given_token_idx = self.bigrams_idx[given_token]
            distribution = list(self.probs[given_token_idx])
        else:
            vocab_size = len(self.unigrams_idx)
            distribution = np.full(vocab_size, 1/vocab_size)
        sample_from_multinomial = np.random.multinomial(1,distribution)
        sample_idx = np.where(sample_from_multinomial==1)[0][0]
        next_token = next((token for token, idx in self.unigrams_idx.items() if idx == sample_idx), None)
        return(next_token)

    def create_new_sentence(self, seed_token):
        while not re.match(r'[\.\?\!]', seed_token[-1][-1]):
            seed_token.append(self.sample_next_gram(' '.join(seed_token[-2:])))
        return seed_token
