documents = [
    "i am the king of the world",                         # Document A
    "dogs are the best companion",                       # Document B
    "dogs are the best companion in the world",          # Document C
    "i love dogs i love cats i love dogs and cats"       # Document D
]

import math

# 計算 TF (Term Frequency)
def compute_tf(term, doc_tokens):
    term_count = doc_tokens.count(term)
    total_terms = len(doc_tokens)
    return term_count / total_terms if total_terms > 0 else 0

# 計算 IDF (Inverse Document Frequency)
def compute_idf(term, corpus_tokens):
    N = len(corpus_tokens)
    doc_freq = sum(1 for doc in corpus_tokens if term in doc)
    return math.log((1 + N) / (1 + doc_freq))

# 計算 TF-IDF
def compute_tfidf(term, corpus_tokens):
    idf = compute_idf(term, corpus_tokens)
    tfidf_scores = []
    for doc in corpus_tokens:
        tf = compute_tf(term, doc)
        tfidf_scores.append(tf * idf)
    return tfidf_scores


# 預先處理成 tokens
corpus_tokens = [doc.lower().split() for doc in documents]

# 計算 "dogs" 的 TF-IDF
term = "dogs"
tfidf_scores = compute_tfidf(term, corpus_tokens)

# 印出每篇文件的 TF-IDF 分數
for i, score in enumerate(tfidf_scores):
    print(f"Document {chr(ord('A') + i)} - TF-IDF('{term}') = {score:.5f}")