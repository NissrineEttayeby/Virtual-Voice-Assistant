import speech_recognition as sr
import os
import time
import datetime
import pyjokes
import warnings
import webbrowser
import calendar
import pyttsx3
import random
import smtplib
import wikipedia
import wolframalpha
import winshell
import subprocess
import pickle
import socket
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')

'''For a female voice / if we want a male voice use voices[0]'''
engine.setProperty('voice', voices[1].id)

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

