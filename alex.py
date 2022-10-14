import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.runAndWait()
for voice in voices:
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s\n" %voice.languages)
    engine.setProperty('voice', voice.id)
    engine.say("Justin is depressed")
    engine.runAndWait() 