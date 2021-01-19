'''
Compute TF-IDF
'''

from sklearn.feature_extraction.text import CountVectorizer

# Given a list of strings(documents), return a dictionary of TF-IDF values
def compute_TF_IDF(dataset, verbose = False):
    # Get Bag-of-Words
    vectorizer = CountVectorizer()
    word_counts = vectorizer.fit_transform(dataset)
    word_counts = word_counts.toarray()
    
    # Count inverse document frequency (IDF)
    # IDF[word_idx] = log_10 (N / df_word)
    if verbose:
        print('\nCounting inverse document frequency...')
    total_doc_num = word_counts.shape[0]
    IDF = np.asarray(word_counts > 0).astype(float)
    IDF = np.sum(IDF, axis = 0)
    IDF = np.log10(total_doc_num * np.reciprocal(IDF))
    if verbose:
        print('IDF shape: ',IDF.shape)
        pprint(IDF)
        
    # Count term frequency (TF)
    # TF[doc_num, word_idx] = 1 + log_10 {count(word,doc)}
    TF = [] 
    if verbose:
        print('\nCounting term frequency...')
    for document in word_counts:
        TF.append([1 + np.log10(cnt) if cnt>0 else 0 for cnt in document])
    TF = np.asarray(TF)
    if verbose:
        print('TF shape: ', TF.shape)
        pprint(TF)

    # Compute TF-IDF and store the value in TF dictionary
    # TF[doc_num, word_idx] = TF * IDF
    if verbose:
        print('\nComputing TF-IDF...')
    for idx in range(len(IDF)):
        TF[:, idx] = np.multiply(TF[:, idx], IDF[idx])
    if verbose:
        pprint(TF)
    
    return TF