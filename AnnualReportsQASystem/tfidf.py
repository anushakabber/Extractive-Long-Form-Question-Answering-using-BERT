import re
from sklearn.feature_extraction.text import TfidfVectorizer

def tfidf(all_sentences_text, question):
    all_sentences_text.append(re.sub(r"[^a-zA-Z0-9]+", ' ', question))
    tfidf = TfidfVectorizer().fit_transform(all_sentences_text)
    pairwise_similarity = tfidf * tfidf.T
    arr =  pairwise_similarity.toarray()
    temp = list(arr[len(arr)-1]).copy()
    temp.sort(reverse= True)
    to_finbert = []
    for i in range(200):
      to_finbert.append(all_sentences_text[list(arr[len(arr)-1]).index(temp[i])])

    return to_finbert