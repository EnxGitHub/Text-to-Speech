from gtts  import gTTS
import os
from playsound import playsound
while True:
    language = "en"
    if language.lower().strip() == "tr" or language.lower().strip() == "en": 
        break
    else:
        print("Please enter a valid language!")
        continue

    mytext = str(input("\nPlease enter a text:\t"))
    output = gTTS(text=mytext,lang=language,slow=False)
    output.save("output.mp3")
    playsound("output.mp3")
    os.remove("output.mp3")
