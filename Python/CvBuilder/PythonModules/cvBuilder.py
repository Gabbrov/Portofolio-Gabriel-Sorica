import openai
import PyPDF2
import os

from enum import Enum

from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab import *


key = "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"


pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))




pdfs=[]

openai.api_key = key


class part(Enum):
    Personal = 1
    Skills = 2
    WorkHist = 3

def aiGen(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    ai_response= response.choices[0].message.content
    return (ai_response)
    

def analyse_keys(text):
    print("Analising...")
    prompt_text = "detect key words to help in looking to hiring candidates for job description: "+text
    return (aiGen(prompt_text))

def analyse_skills(text):
    prompt_text = "Detect Skills and hobbies from text and format them in a list format: "+text
    return (aiGen(prompt_text))



#Takes in Text, passes trough gpt3.5 and returns a composed section for a cv 
def compose(text,part,Keys):
    match part:
        case part.Personal:
            prompt_text = "Select key points from the personal description that would fit: "+Keys+". From text and then make it into a personal desciption:"+text

        case part.Skills:
            prompt_text = "Select the best skills to showcase from: "+text+", compared to key words : "+Keys

        case part.WorkHist:
            prompt_text = "Rewrite jobs description from: "+text+", to match the key words : "+Keys
            
        case _:
            prompt_text = "Rephrase: "+text+"in a simplistic yet formal aproach to match key points: "+Keys


    return(aiGen(prompt_text))
#takes a list to iterate trough, summarize and thn combine in one file
def combine(Iter = []):
    tempList=[]
    for i in Iter:
        tempList.append(aiGen("extract key points"+i))
    
    return(aiGen("Combine unique parts of each text, ensuring to keep key points and to make sure there are no repetitions: "+str(tempList)))
        

def rephrase(text):
    prompt="Rewrite in 3rd person as writen about myself, to make more human like, ensuring less use of difficult/rare words while keeping positive and profesional outlook: "+text
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}]
    )
    
    ai_response = response.choices[0].message.content
    return(ai_response)


