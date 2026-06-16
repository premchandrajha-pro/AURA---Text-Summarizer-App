# fast api
from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

#initialing the fast api app
app = FastAPI(title="Text summerizer App", description="Text Summerization using T5", version="1.0")

#loding model and tokenizer
model = T5ForConditionalGeneration.from_pretrained("./saved_summery_model")
tokenizer =T5Tokenizer.from_pretrained("./saved_summery_model")

#device setup
if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)

#templating 
templates = Jinja2Templates(directory=".")

#input schema for dialogue ==> string
class DialogueInput(BaseModel):
    Dialogue: str

#clean function
def clean_data(text):
    text = re.sub(r"\r\n", " ", text)  # for lines 
    text = re.sub(r"\s+", " ", text)  # for spaces 
    text = re.sub(r"<.*?>", " ", text) # for html tags
    text = text.strip().lower()    #.strip for removing trailing zeros and leading zeros 
    return text

#summerize function
def summarize_dialogue(dialogue):
    dialogue = clean_data(dialogue)  #cleaning the data 
    # this function is already made above 

    #tokenize
    input = tokenizer(
        dialogue,
        padding = "max_length",
        max_length = 512,
        truncation = True,
        return_tensors = "pt"
    ) 
    #generate teh summery ==> token ids
    targets = model.generate(
        input_ids = input["input_ids"],
        attention_mask = input["attention_mask"],
        max_length = 150,
        num_beams = 4,   # it will generate 4 diff. no. of ouputs of summery and compare them and then returm the best one
        early_stopping = True   # 
    )
    #token ids convert to summary => decoding 

    summary = tokenizer.decode(targets[0], skip_special_tokens = True)   # EOS, SEP
    return summary

# API Endpoins

 
@app.post("/summarize/")
async def summarize(dialogue_input: DialogueInput):  # value of input and type of input
    summary = summarize_dialogue(dialogue_input.Dialogue)
    return {"summary":summary}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )