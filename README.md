# NightBot
`NightBot` is a chatbot that collects data on bars and provides you with venues according to your genre or province preference. Learning the genre of the venues is also possible.
# Dataset
Our data set `nightlife_data` includes 27 bars in Istanbul with their addresses and genres they play.
```python
>>> nightlife_data.tail(10)
                                                                        ADDRESS  PROVINCE       GENRE
VENUE
yazı tura barcade                           Sinanpaşa Mh. Şht. Asım Cd. No: 38   beşiktaş       k-pop
rocknrolla beşiktaş                           Cihannüma Mh. Barbaros Blv. No:65  beşiktaş        punk
kozmonot pub bomonti                            Cumhuriyet Mh. Düzoğlu Sk. No:2     şişli  electronic
kozmonot pub topağacı                          Teşvikiye Mh. Poyracık Sk No:9/A     şişli  electronic
divine brasserie & jazz club  Topağacı Mh. Nişantaşı Ihlamur Yolu Sk. No: 34...     şişli       blues
hunhar topağacı                             Topağacı Mh. Ihlamur Yolu Sk. No:28     şişli         pop
the muse                                          Harbiye Mh. Atiye Sk. No: 2/B     şişli         r&b
wu bomonti                                    Cumhuriyet Mh. Düzoğlu Sk. No:2/B     şişli  electronic
dorock xl kadıköy                           Caferağa Mh. Neşet Ömer Sk. No: 3/C   kadıköy        rock
rocknrolla kadıköy                                  Caferağa Mh. Moda Cd. No:20   kadıköy        rock
```
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
>>>find_venue("pop")
                                                           ADDRESS PROVINCE GENRE
VENUE
baylo                     Asmalımescit Mh. Meşrutiyet Cd. No:107/A  beyoğlu   pop
eskici                           Kuloğlu Mh. Fuat Uzkınay Sk. No:8  beyoğlu   pop
taps bebek                           bebek Cevdet Paşa Cd. No: 119    bebek   pop
l'eclipse bar    Cengiz Topel Cd. No: 39 Le Meridien Istanbul H...   etiler   pop
hunhar topağacı                Topağacı Mh. Ihlamur Yolu Sk. No:28    şişli   pop
```
`find_venue_gp(string1, string2)`: Finds venues given both genre and province.
<br></br>
<i> Example: </i>
```python
>>>find_venue_gp("pop","beyoğlu")
                                         ADDRESS PROVINCE GENRE
VENUE
baylo   Asmalımescit Mh. Meşrutiyet Cd. No:107/A  beyoğlu   pop
eskici         Kuloğlu Mh. Fuat Uzkınay Sk. No:8  beyoğlu   pop
```
<br></br>
`find_genre(venue)`: Finds the genre of a venue.
<br></br>
<i> Example: </i>
```python
>>> find_genre("Eskici")
       GENRE
VENUE
eskici   pop
```
<br></br>
`InputAnalysis(text)`: Extracts the province and genre entities as well as the intent of the input from the wit.ai output. It works with the length of the output, first checking if the code was able to find the intent and then if there are one or multiple entities.
<br></br>
<i> Example: </i>
```python
>>> InputAnalysis("Where can I listen to R&B in Beşiktaş?")
['intent', 'find_venue', 'province', 'Beşiktaş', 'genre', 'r&b']
```
<br></br>
`NightBot(text)`: Takes the input of the user to give a suitable response with the desired result. (ie. venue names or genre)
<br></br>
<i> Example: </i>
```python
>>> NightBot("I want to listen to pop music in Beyoğlu tonight.")
The findings for pop and Beyoğlu are these bars: Baylo, Eskici
```
# How the NightBot works:
<i> Example: </i>
<br></br>
After getting the first input, the while loop starts working. The input is the argument of `NightBot()` function. With each new input the function works again. 
The loop is executed with the exit command.
<br></br>
```python
I am going to Şişli tonight!!
When I'm in the mood for şişli, I always go to Kozmonot pub bomonti, Kozmonot pub topağacı, Divine brasserie & jazz club, Hunhar topağacı, The muse, Wu bomonti.
***Write 'exit' to exit the program please***
What about rnb in şişli tho??
The findings for r&b and şişli are these bars: The muse
***Write 'exit' to exit the program please***
exit
Okay, that was it then, see you later and have lots of fun!
```
