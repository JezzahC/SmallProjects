from datetime import datetime
from word2number import w2n
import speech_recognition as sr, pyttsx3, wikipedia, random, pyjokes, time, reminder, calculation, PyDictionary

# Initialise reminder notification
reminder.notifyReminders()

# Constants and variables
ACTIVATION_WORDS: str = "hey computer"
COMPLETE = ["complete", "remove"]
EDIT = ["edit", "change", "modify"]
ENGINE = pyttsx3.init()
JOKE_STARTERS = ["I've got a joke that'll crack you up!", "Here's a joke for you...", "I've got a joke that will make you laugh!", "Try not to laugh!"]
VERIFICATION = ["check", "verify"]
VOICES = ENGINE.getProperty("voices")

# pyttsx3 voice ID initialisation
ENGINE.setProperty("voice", VOICES[14].id)

# Computer Speech Function
def speak(text, rate=120): # 
    ENGINE.setProperty("rate", rate)
    ENGINE.say(text)
    ENGINE.runAndWait()

# Parsing Speech
def parseCommand() -> str:
    listener = sr.Recognizer()
    
    with sr.Microphone() as source:
        listener.pause_threshold = 2
        inputSpeech = listener.listen(source)

    try:
        query = listener.recognize_google(inputSpeech, language="en_gb")
        print(query)
    except Exception as exception:
        query = "None"
        speak("I didn't quite catch that.")
        print(exception)

    return query

#*  ASSISTANT'S MAIN FUNCTIONS
#* -----------------------------

# Generate a joke
def generateJoke():
    return pyjokes.get_joke()

# Generate, retrieve and delete todo tasks
def todoList(query):
    if query in VERIFICATION:
        with open("toDo.txt", "r") as toDo:
            speak(f"Your to do list is as following: {toDo.read()}")
    elif query in EDIT:
        speak("Please enunciate the task you would like to add.")
        task = parseCommand().lower()
        with open("toDo.txt", "r") as toDo:
            try:
                line = toDo.read()
                print(line)
                number = int(line[0])
            except IndexError:
                number = 0
        with open("toDo.txt", "a+") as toDo:
            toDo.write(f"{number + 1} - {task}\n")
    elif query in COMPLETE:
        with open("toDo.txt", "r") as toDo:
            speak("What task would you like to remove?")
            index = w2n.word_to_num(parseCommand().lower().split(" ")[-1])
            todoList = toDo.readlines()
            removedItem = todoList.pop(index - 1)
        with open("toDo.txt", "w") as toDo:
            toDo.writelines(todoList)
            speak(f"Removed {removedItem}")
    else:
        speak("No valid action provided.")

# Wikipedia Search
def wikiSearch(query: str):
    if "summarise" in query:
        try:
            speak(wikipedia.summary(" ".join(query.split("on")[-1]), sentences=3))
        except Exception as error:
                speak(f"The error {error} was thrown.")

    elif "random" in query:
        try:
            speak(wikipedia.summary(wikipedia.random(1), sentences=3))
        except Exception as error:
            speak(f"The error {error} was thrown.")

    elif "search" in query:
        try:
            searchQuery = wikipedia.search(query.split(" ")[-1])
            for results in searchQuery:
                speak(results)
        except Exception as error:
            speak(f"The error {error} was thrown.")

# Main Function
def main():
    speak("Initialising all systems...")
    time.sleep(1)
    speak("Systems initialised.")

    while True:
        reminder.notifyReminders()
        query = parseCommand().lower().split()

        if " ".join(query[:2]) == ACTIVATION_WORDS:
            for i in range(2):
                query.pop(0)

            if "to-do" in query:
                todoList(query[query.index("to-do") - 1])

            elif "random number between" in " ".join(query):
                numbers = query[query.index("between") + 1:query.index("between") + 4]
                num1, num2 = w2n.word_to_num(numbers[0]), w2n.word_to_num(numbers[2])
                speak(f"A random number between {num1} and {num2} is {random.randint(num1, num2)}.")

            elif "set reminder" in " ".join(query):
                speak("What is the name of your reminder?")
                name = parseCommand().lower()
                speak("When would you like to set it off?")
                noteTime = parseCommand().lower()
                reminder.makeReminder(name, noteTime)

            elif "tell me a joke" in " ".join(query):
                speak(JOKE_STARTERS[random.randint(0, len(JOKE_STARTERS) - 1)])      
                speak(generateJoke())

            elif query[0] == "what" and query[1] == "is" and query[2] == "the" and query[3] == "date" and query[4] == "today":
                speak(f"The current date is: {datetime.now().strftime('%d %m %Y')}")

            elif query[0] == "what" and query[1] == "time" and query[2] == "is" and query[3] == "it":
                speak(f"The current time is: {datetime.now().strftime('%H %M')}")

            elif "calculate" in query:
                print("yes")
                for elements in query:
                    index = query.index(elements)
                    query.pop(index)
                    try:
                        elements = w2n.word_to_num(elements)
                    except ValueError:
                        pass
                    query.insert(index, elements)
                speak(str(calculation.maths(query)))
main()