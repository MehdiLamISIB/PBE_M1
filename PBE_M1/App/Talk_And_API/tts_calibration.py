import subprocess
text="espeak -v mb-fr1 -s 150 -a 100 "
lst_text=text.split()
lst_text.append('"ceci est un message"')
#lst_text.pop()
subprocess.run(lst_text)
print("fin")

"""
import pyttsx3
engine = pyttsx3.init(driverName='espeak')

voices=engine.getProperty('voices')
engine.setProperty('voice','french')


engine.setProperty('rate',200)
engine.setProperty('volume',0.8)

engine.say("bonjour ceci est un test 1 2 3")
engine.runAndWait()
print("hello world")
"""