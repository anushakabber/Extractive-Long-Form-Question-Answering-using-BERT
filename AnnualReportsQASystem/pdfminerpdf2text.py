from pdfminer.high_level import extract_text


def pdfminer(filename):
    text = extract_text(filename)
    f1 = open("converted_text.txt", "w")
    f1.write(text)
    return
