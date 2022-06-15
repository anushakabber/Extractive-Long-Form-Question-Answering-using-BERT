import re
import nltk
from subprocess import call
nltk.download('punkt')


def cleaningText() -> list:
    f1_new = open('converted_text.txt', 'r')
    f1_old = open('cleaned_text.txt', 'w')
    lines = f1_new.readlines()
    for line in range(len(lines)):
        if (len(lines[line]) > 10 and re.search('[a-zA-Z]', lines[line]) and '|' not in lines[line]):

            if (len(lines[line + 1]) > 10):
                f1_old.write(lines[line].strip('\n'))
            elif (len(lines[line - 1]) > 10 and re.search('[a-zA-Z]', lines[line - 1]) and '|' not in lines[
                line - 1]) and (len(lines[line + 1]) < 10 and re.search('[a-zA-Z]', lines[line + 1])):

                f1_old.write(lines[line].strip('\n'))
                f1_old.write(lines[line + 1].strip('\n') + '\n')

            elif (len(lines[line - 1]) > 10 and re.search('[a-zA-Z]', lines[line - 1]) and '|' not in lines[line - 1]):

                f1_old.write(lines[line].strip('\n') + '\n')


    f_1 = open('cleaned_text.txt', 'r')
    all_1 = f_1.readlines()
    all_sentences_text = []
    for i in all_1:
        sentences = nltk.sent_tokenize(i)
        for j in sentences:
            j = j.replace(',', '')
            j = j.replace('-', ' ')
            all_sentences_text.append(j)


    call(["rm", "converted_text.txt"])
    call(["rm", "cleaned_text.txt"])
    return all_sentences_text