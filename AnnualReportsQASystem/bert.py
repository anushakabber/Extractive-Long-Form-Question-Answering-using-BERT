from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline


def bertReranking(finbertReranking, question):

  model_name = "deepset/roberta-base-squad2"

  nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

  scores_sentences = []

  for i in range(len(finbertReranking)):
    QA_input = {
      'question': question,
      'context': finbertReranking[i]}

    res = nlp(QA_input)
    scores_sentences.append([res['score'], i])
    scores_sentences.sort(key=lambda x: x[0], reverse=True)

  lines = ''
  for i in range(5):
    lines += (finbertReranking[scores_sentences[i][1]]) + " "

  return lines