# -*- coding: utf-8 -*-
"""Nightlife Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_vO2KG29h6V9Iqz7YMtG9QD6DdrP0gDq
"""

"""Installing the required packages"""
#!pip install pywit
#!pip install wit
import random
from pandas._libs import index
import numpy as np
from wit import Wit
import re
import pandas as pd
import random

"""Our dataset of bars, their locations, genres they play and addresses"""
nl_data = pd.read_csv("ling360 project FINAL_VER venues genres data - Sayfa1.csv")
nl_data
nightlife_data = nl_data.set_index('VENUE')
nightlife_data

"""We have a small dataset of artists and their genres to make it easier for the user to search for a venue by the artist name"""
"""We turned to information into a dictionary to use in our functions"""
artist_genre = pd.read_csv("ling 360 proje FINAL_VER top 50 artists genres - Sayfa1.csv")
artist_data = artist_genre.set_index("Artist")
artists = list(artist_data.index.values)
a_genres = list(artist_data["Genre"])
artist_genre_dict = {}
for i in range(len(artists)):
  artist_genre_dict[artists[i]] = a_genres[i]

#artist_genre_dict

"""Our lists of elements which makes it easier to check if the findings in the input matches any items in our lists to classify them."""
genress = ["r&b", "metal", "rock", "hip-hop", "pop", "electronic", "blues", "jazz", "punk", "k-pop", "latin", "rap"]
provinces = ["taksim", "beşiktaş", "kadıköy", "beyoğlu", "levent", "bebek", "şişli"]
venue = list(nightlife_data.index.values)

access_token = "5O6MM3BQBVCZHYIV5OMCFPDOO3NTH3AG"
person = Wit(access_token)
person.message("Let's go crazy with rock tonight!")

def find_genre(venue):
  """Finds the genre of a venue"""
  venue = venue.lower()
  return nightlife_data.loc[[venue], ["GENRE"]]

find_genre("kastel")

def find_venue(string):
  """Finds venues given genre or province"""
  string = string.lower()
  if string in genress:
    return nightlife_data.loc[nightlife_data["GENRE"] == string]
  elif string in provinces:
    return nightlife_data.loc[nightlife_data["PROVINCE"] == string]

find_venue("pop")

def find_venue_gp(string1, string2):
  """Finds venues given both genre and province"""
  string1 = string1.lower()
  string2 = string2.lower()
  if string1 in genress and string2 in provinces:
    return nightlife_data.loc[(nightlife_data["GENRE"] == string1) & (nightlife_data["PROVINCE"] == string2)]
  elif string2 in genress and string1 in provinces:
    return nightlife_data.loc[(nightlife_data["GENRE"] == string2) & (nightlife_data["PROVINCE"] == string1)]

find_venue_gp("electronic", "beyoğlu")

def InputAnalysis(text):
  """Extracts the province and genre entities as well as the intent of the input from the wit.ai output"""
  """It works with the length of the output, first chekcing if the code was able to find the intent and then if there are one or multiple entities"""
  resp = person.message(text)
  if len(resp["intents"]) > 0:
    intents = "intent"
    intent = resp["intents"][0]["name"]
    if len(resp["entities"]) == 2:
      entity0 = list(resp["entities"])[0]
      value0 = resp["entities"][entity0][0]["value"]
      entity0 = re.sub(r"\w+:", "", entity0)
      entity1 = list(resp["entities"])[1]
      value1 = resp["entities"][entity1][0]["value"]
      entity1 = re.sub(r"\w+:", "", entity1)
      return ([intents, intent, entity0, value0, entity1, value1])
    elif len(resp["entities"]) == 1:
      entity0 = list(resp["entities"])[0]
      value0 = resp["entities"][entity0][0]["value"]
      entity0 = re.sub(r"\w+:", "", entity0)
      return ([intents, intent, entity0, value0])
  else:
    if len(resp["entities"]) == 2:
      entity0 = list(resp["entities"])[0]
      value0 = resp["entities"][entity0][0]["value"]
      entity0 = re.sub(r"\w+:", "", entity0)
      entity1 = list(resp["entities"])[1]
      value1 = resp["entities"][entity1][0]["value"]
      entity1 = re.sub(r"\w+:", "", entity1)
      return ([entity0, value0, entity1, value1])
    elif len(resp["entities"]) == 1:
      entity0 = list(resp["entities"])[0]
      value0 = resp["entities"][entity0][0]["value"]
      entity0 = re.sub(r"\w+:", "", entity0)
      return ([entity0, value0])
    

InputAnalysis('what can I listen in baylo?')

InputAnalysis("where can I listen to pop?")

InputAnalysis("ritim")

"""List of the variations of the same response sentence with slight alterations for a more enjoyable experience"""
sentence_list = [
                 "For {genre}, go to {bars}. All the cool people are there.",
                 "If you are into {genre}, {bars} is just what you're looking for.", 
                 "If you want to enjoy {genre}, the best place to go is {bars}. Thank me later.", 
                 "When I'm in the mood for {genre}, I always go to {bars}.", 
                 "{bars} is the place where {genre} fans meet. See you there!",
                 "I really like {genre} too. You can prefer {bars}.",
                 "Here you go {genre} fan! You can find your kind of music at {bars}.",
                 "I don't really get why people love {genre}, but I know {bars} might be worth checking out. Have fun!",
                 "It's tough to find good {genre} music these days, isn't it? Thankfully there are places like {bars}."]

def NightBot(text):
  
  """Taking the input of the user to give the suitable response"""
  """First transforming the artists into genre with the dictionary"""
  """The input is then analysed with wit ai to find the intents and entities"""
  """According to the intent and information of the wit ai output the required function works"""
  """If there are enough information to work with one function, the response that is randomly chosen from a list of natural sounding sentences."""
  """The response is printed with the results."""
  for i in artists:
    if len(re.findall(i, text)) > 0:
      text = text + artist_genre_dict[i]
      text = text.replace(i, " ")
  returnlist = InputAnalysis(text)
  try:
    if returnlist[0] == "intent":
      try:
        if len(returnlist) == 6:
          intents, intent, entity0, value0, entity1, value1 = InputAnalysis(text)
          if intent == "find_venue":
            result = find_venue_gp(value1, value0)
            bars = ", ".join([(str(i)[0].upper()+str(i)[1:]) for i in result.index.values])
            print(f"The findings for {value1} and {value0} are these bars: {bars}")
        elif len(returnlist) == 4:
          intents, intent, entity0, value0 = InputAnalysis(text)
          if intent == "find_venue":
            result = find_venue(value0)
            bars = ", ".join([(str(i)[0].upper()+str(i)[1:]) for i in result.index.values])
            print(random.choice(sentence_list).format(genre=value0, bars =bars))
        elif intent == "find_genre":
          result = find_genre(value0)
          venue_genre = result["GENRE"].iloc[0]
          print(f"They have the genre {venue_genre} in {value0}")
      except:
        print("Sorry to tell you that, this is out of my scope, for now...")
    else:
      try:
        if len(returnlist) == 4:
          entity0, value0, entity1, value1 = InputAnalysis(text)
          result = find_venue_gp(value1, value0)
          bars = ", ".join([(str(i)[0].upper()+str(i)[1:]) for i in result.index.values])
          print(f"The findings for {value1} and {value0} are these bars: {bars}")
        elif len(returnlist) == 2:
          entity0, value0 = InputAnalysis(text)
          result = find_venue(value0)
          bars = ", ".join([(str(i)[0].upper()+str(i)[1:]) for i in result.index.values])
          print(random.choice(sentence_list).format(genre=value0, bars =bars))
      except:
        print("I am working on myself for now, so that I can answer all your questions, even this one!")
  except:
    print("I am not yet capable of understanging and answering this, accept my apologies...")

#NightBot("What is available for rock?") 
#evaluation metric:
#percentage of fails
#percentage of queries
#successful interactions, customer satisfaction

user_input = input("What do you feel like for a night out?")
exit = True
while exit:
  NightBot(user_input)
  print("***Write 'exit' to exit the program please***")
  user_input = input()
  if user_input == "exit":
    print("Okay, that was it then, see you later and have lots of fun!")
    exit = False
  else:
    continue
