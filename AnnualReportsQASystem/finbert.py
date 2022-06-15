from finbert_embedding.embedding import FinbertEmbedding
from scipy import spatial
finbert = FinbertEmbedding()

def finbertReranking(to_finbert, question):
    X = question
    vectorX = finbert.sentence_vector(X)
    scores = list()
    for line in to_finbert:
        Y = line
        vectorY = finbert.sentence_vector(Y)
        scores.append([Y, 1 - spatial.distance.cosine(vectorY, vectorX)])

    scores.sort(key=lambda x: x[1], reverse=True)
    top_k_sentences = []
    for i in range(20):
        top_k_sentences.append(scores[i][0])
    return top_k_sentences
