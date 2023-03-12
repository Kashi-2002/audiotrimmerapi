from pydub import AudioSegment
# from fastapi import FastAPI
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
import os
import shutil

import json

import wave

import wget
# Define the remote file to retrieve


app=FastAPI()

def func1(filepath):
    sound = AudioSegment.from_file(file=filepath, format="wav")
    return sound

def keep(sound,start,end):
    part_1=sound[start*1000:end*1000]
    part_1.export(out_f=".venv\copied.wav", format="wav")

def remove(sound,start,end):
    part_1=sound[0:start*1000]
    part_2=sound[-(sound.duration_seconds-end)*1000:]
    part_3=part_1+part_2
    part_3.export(out_f=".venv\copied1.wav", format="wav")


@app.get("/{filepath}/{start}/{end}/{items}")
def trimmer(filepath:str,start:float,end:float,items:str):
    sound=func1("./.venv/"+filepath)
    # if(items=="keep"):
    #     keep(sound,start,end)
    # if(items=="remove"):
    remove(sound,start,end)
    # print(start)
    return {"Hello": keep(sound,start,end)}
