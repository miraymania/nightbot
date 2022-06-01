# NightBot
`NightBot` is a chatbot that provides you venues according to your genre preference.
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
`NightBot(text)`: Takes the input of the user to give a suitable response with the desired result. (ie. venue names or genre)
<br></br>
<i> Example: </i>
```python
NightBot("I want to listen to rock music in Taksim tonight?")
```
# How the NightBot works:
<i> Example: </i>
<br></br>
After getting the first input, the while loop starts working. The input is the argument of `NightBot()` function. With each new input the function works again. 
The loop is executed with the exit command.
<br></br>
```python
What do you feel like for a night out?I'm going to şişli tonight!
When I'm in the mood for şişli, I always go to Kozmonot pub bomonti, Kozmonot pub topağacı, Divine brasserie & jazz club, Hunhar topağacı, The muse, Wu bomonti.
***Type 'exit' to exit the program please***
What about rnb in şişli tho?
The findings for r&b and şişli are these bars: The muse
***Type 'exit' to exit the program please***
exit
Okay, that was it then, see you later and have lots of fun!
```
