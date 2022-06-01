# NightBot
`NightBot` is a chatbot that provides you venues according to your genre preference. Although its main aim is to find venues, it is also capable of finding provinces and genres.
# Wit.ai
`Wit.ai` is used to extract data from utterances with `entity` and `intent` classification. 
<br></br>
<b>How Wit.ai works:</b>
<br></br>
  <b>Intents:</b> 
  <br></br>
  `find_genre`: Finds the `genre` of a `venue`.
  <br></br>
   `find_venue`: Finds `venues` given `genre` or `province`.
   <br></br>
  Entities: `genre`, `province`, `venue`
# How to use functions
`find_venue(string)`: Finds venues given genre or province.
<br></br>
<i> Example: </i>
```python
find_venue("pop")
```
`find_venue_gp(string1, string2)`: Finds venues given both genre and province.
<br></br>
<i> Example: </i>
```python
find_venue_gp("electronic","beyoğlu")
```
`find_genre(venue)`: Finds the genre of a venue.
<br></br>
<i> Example: </i>
```python
find_genre("Kastel")
```
`InputAnalysis(text)`: Extracts the province and genre entities as well as the intent of the input from the wit.ai output. It works with the length of the output, first checking if the code was able to find the intent and then if there are one or multiple entities.
<br></br>
<i> Example: </i>
```python
InputAnalysis("Where can I listen to R&B?")
```
`NightBot(text)`: Takes the input of the user to give a suitable response.
<br></br>
<i> Example: </i>
```python
NightBot("I want to listen to rock music in Taksim tonight?")
```
# How the NightBot works:
<i> Example: </i>
```python
user_input = input("What do you feel like for a night out?")
exit = True
while exit:
  NightBot(user_input)
  print("***Type 'exit' to exit the program please***")
  user_input = input()
  if user_input == "exit":
    print("Okay, that was it then, see you later and have lots of fun!")
    exit = False
  else:
    continue
```
