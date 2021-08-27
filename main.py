from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get('/')
def read_form():
    return 'hello world'


@app.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, sl: int = Form(...),sw: int = Form(...),pl: int = Form(...),pw: int = Form(...)):
    r = [sl,sw,pl,pw]
    result = len(r)
    return templates.TemplateResponse('index.html', context={'request': request, 'result': result})
