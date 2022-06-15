import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import pdfminerpdf2text
import cleaningText
import tfidf
import finbert
import bert


#uvicorn main:app --reload   -- use this to start the app

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

pdf = ""

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# @app.get("/form", response_class=HTMLResponse)
# def form(request: Request):
#     return templates.TemplateResponse("formpdf.html", {"request": request})

@app.get("/formpdf", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse("formpdf.html", {"request": request})

@app.post("/formquestion", response_class=HTMLResponse)
def form(request: Request, inputpdf:str = Form(...)):
    global pdf
    pdf = inputpdf
    return templates.TemplateResponse("questionForm.html", {"request": request})

@app.post("/response", response_class=HTMLResponse)
async def getting_form_data(request: Request, question: str = Form(...)):

    pdfminerpdf2text.pdfminer(pdf)
    tfidf_text = cleaningText.cleaningText()
    to_finbert = tfidf.tfidf(tfidf_text, question)
    bert_text = finbert.finbertReranking(to_finbert, question)
    result = bert.bertReranking(bert_text, question)

    return templates.TemplateResponse("result.html", {"request": request, "result": result})

if __name__ == '__main__':
    uvicorn.run(app)