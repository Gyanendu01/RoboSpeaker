import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker created by Gyanendu.")
    while True:
        engine = pyttsx3.init()

        x = input("Enter what you want me to pronounce and press q to exit: ") 
        if x == "q":
            engine.say("Have a nice day!")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()