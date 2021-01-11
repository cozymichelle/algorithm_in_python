'''
Implement Byte Pair Encoding
'''

class BPE:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
    
    # Given text, return its vocabulary and counter of word counts
    def initialize(self, training_corpus):
        words = []
        for t in training_corpus:
            # Change to lowercase
            t = t.lower()
            # Remove punctuation
            t = re.sub(r'[^a-zA-Z0-9]', ' ', t)
            
            self.vocabulary += list(set(re.sub(r'\s', '', t)))
            # Add a whitespace to every character and add the end token
            words += [' '.join(w) + ' </w>' for w in t.split()]
        self.vocabulary = list(set(self.vocabulary)) + ['</w>']
        return self.vocabulary, Counter(words)
    
    # Count pairs of symbols
    def max_pair(self, word_counts):
        pairs = dict()
        for word, count in word_counts.items():
            token = word.split()
            for i in range(len(token) - 1):
                pairs[(token[i], token[i + 1])] = \
                    pairs.get((token[i], token[i + 1]), 0) + count
        return max(pairs, key=pairs.get)
    
    # Merge the most frequent pair symbols
    def merge(self, max_pair, word_counts):
        self.vocabulary.append(''.join(max_pair))
        word_counts_ = dict()
        for word, count in word_counts.items():
            word_ = word.replace(' '.join(max_pair), ''.join(max_pair))
            word_counts_[word_] = count
        return word_counts_
    
    # Return sorted vocabulary
    def get_vocabulary(self):
        self.vocabulary = sorted(self.vocabulary, key= lambda x: len(x), reverse=True)
        return self.vocabulary
    
    # Tokenize a given word using the BPE vocabulary
    def bpe_tokenize(self, word, vocabulary, token_dict):
        if word in token_dict:
            return token_dict[word]

        tokenized_word = []
        for i in range(len(vocabulary)):
            token = vocabulary[i]
            token_idx = [(m.start(0), m.end(0)) for m in re.finditer(token, word)]
            if not token_idx:
                continue

            idx = 0
            for idx0, idx1 in token_idx:
                if idx0 != 0 and idx != idx0:
                    tokenized_word += self.bpe_tokenize(word[idx:idx0], vocabulary[i+1:], token_dict)
                idx = idx1
            tokenized_word.append(token)
            if idx != len(word):
                tokenized_word += self.bpe_tokenize(word[idx:], vocabulary[i+1:], token_dict)
            break
        return tokenized_word


# Train with the training_corpus
# and apply Byte Pair Encoding to the text with k merges
def BytePairEncoding(text, k, training_corpus, verbose = False):
    tokenized_text = []
    vocabulary = []
    
    if verbose:
        print("Begin byte-pair-encoding. k = ", k)
    # Initialize vocabulary and a dictionary with counts for each word
    bpe = BPE(vocabulary)
    vocab, word_counts = bpe.initialize(training_corpus)
    
    # Find a pair with maximum number and merge tokens for k times
    for i in range(k):
        if i % 500 == 0:
            print('Byte-pair-encoding iteration ', i)
        max_pair = bpe.max_pair(word_counts)
        word_counts = bpe.merge(max_pair, word_counts)
        
    # Tokenize text using the learned vocabulary
    vocabulary = bpe.get_vocabulary()
    token_dict = dict()
    text = [word + '</w>' for word in text.split()]
    if verbose:
        print("Tokenizing text with %d words" % len(text))
    for i, word in enumerate(text):
        tokenized_word = bpe.bpe_tokenize(word, vocabulary, token_dict)
        token_dict[word] = tokenized_word
        tokenized_text += tokenized_word
        if i % 1000 == 0:
            print("The number of words tokenized: ", i)

    return vocabulary, tokenized_text