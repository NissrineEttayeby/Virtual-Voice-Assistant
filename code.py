while True:
    try:
        text = audio()
        speak = ""
        if call(text):
            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today
                print("Assistant : ", speak)

            elif "time" in text:
                now = datetime.datetime.now()
                n = ""
                if now.hour >= 12:
                    n = "pm"
                    hour = now.hour - 12
                else:
                    n = "am"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + n + " ."
                print("Assistant : ", speak)

            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is" in text:
                    info = wiki(text)
                    wiki = wikipedia.summary(info, sentences=2)
                    speak = speak + " " + wiki
                    print("Assistant : ", speak)

            elif "where is" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)
                print("Assistant : ", speak)

            elif "your name" in text:
                speak = speak + "My name is Assistant"
                print("Assistant : ", speak)

            elif "who are you" in text or "define yourself" in text:
                speak = speak + "Hello, I am a virtual assistant. I am here to make your life easier."
                print("Assistant : ", speak)

            elif "made you" in text or "created you" in text:
                speak = speak + "I was created by Nissrine Ettayeby"
                print("Assistant : ", speak)

            elif "who am I" in text:
                speak = speak + "You must probably be a human"
                print("Assistant : ", speak)

            elif "why do you exist" in text or "why did you come to this world" in text:
                speak = speak + "To help you in your daily tasks"
                print("Assistant : ", speak)

            elif "how are you" in text:
                speak = speak + "I am awesome, Thank you"
                speak = speak + "\nHow are you?"
                print("Assistant : ", speak)

            elif "fine" in text or "good" in text or "great" in text:
                speak = speak + "It's good to know that your fine"
                print("Assistant : ", speak)

            elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
                talk("for how many seconds do you want me to stop")
                a = int(audio())
                time.sleep(a)
                speak = speak + str(a) + " seconds completed. Now you can ask me anything"
                print("Assistant : ", speak)

            elif "thanks" in text or "thank you" in text :
                talk("you are welcome!")

            elif "exit" in text or "quit" in text:
                speak = "Good bye!"
                print("Assistant : ", speak)
                exit()

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"
                    print("Assistant : ",speak)
                    os.startfile(
                        r"C:\...\chrome.exe"
                    )

                elif "word" in text.lower():
                    speak = speak + "Opening Microsoft Word"
                    print("Assistant : ",speak)
                    os.startfile(
                        r"C:\...\WINWORD.EXE"
                    )

                elif "excel" in text.lower():
                    speak = speak + "Opening Microsoft Excel"
                    print("Assistant : ",speak)
                    os.startfile(
                        "C:\...\EXCEL.EXE"
                    )

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube\n"
                    webbrowser.open("https://youtube.com/")
                    print("Assistant : ", speak)

                elif "google" in text.lower():
                    speak = speak + "Opening Google\n"
                    print("Assistant : ", speak)
                    webbrowser.open("https://google.com/")

                elif "github" in text.lower():
                    speak = speak + "Opening Github"
                    print("Assistant : ", speak)
                    webbrowser.open("https://github.com/")

                else:
                    speak = speak + "Application not available"
                    print("Assistant : ",speak)

            elif "on youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.youtube.com/results?search_query="+"+".join(search)
                )
                speak = speak + "Opening " + str(search) + " on youtube"
                print("Assistant : ", speak)

            elif "search" in text.lower() or "on google" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"
                print("Assistant : ", speak)

            elif "joke" in text.lower():
                speak = speak + pyjokes.get_joke()
                print("Assistant : ", speak)

            elif "empty recycle bin" in text.lower():
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "Recycle Bin Emptied"
                print("Assistant : ", speak)

            elif "mail" in text or "email" in text or "gmail" in text:
                try:
                    talk("What should I say?")
                    content = audio()
                    talk("whom should i send")
                    to = input("Enter To Address: ")
                    send_email(to, content)
                    speak = speak + "Email has been sent !"
                    print("Assistant : ", speak)
                except Exception as e:
                    print(e)
                    speak = speak + "I am not able to send this email"
                    print("Assistant : ", speak)

            elif "note" in text.lower():

                talk("What would you like me to write down?")
                note_text = audio()
                note_text = note_text.lower()
                with open("notes.txt", "a") as f:
                    f.write(note_text + "\n")
                talk("Got it. I've made a note of that.")
                print("Assistant: I have made a note of that.")

            elif "calculate" in text.lower():
                calculate(text)

            elif "ip address" in text.lower():
                ip_address = get_ip()
                speak= "Your IP address is " + ip_address
                print("Assistant : ", speak)


            # Assistant Audio speak
            response(speak)

    except:
          talk("I don't know what you want! , Please try again ")
