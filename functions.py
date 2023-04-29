def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def audio():

    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold = 1
        listener.adjust_for_ambient_noise(source, duration=1)
        voice = listener.listen(source)
        data = " "
        try:
            data = listener.recognize_google(voice)
            print("You said: " + data)

        except sr.UnknownValueError:
            print("Assistant could not understand the audio")
        except sr.RequestError as ex:
            print("Request Error from Google Speech Recognition" + ex)
    return data


def response(command):
        engine.say(command)
        engine.runAndWait()


def call(command):
    action_call = ""
    command = command.lower()
    if action_call in text:
        return True
    return False


def today_date():
    timer = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = timer.month
    day_now = timer.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."


def say_hello(command):
    req = ["hi", "hey", "hola", "greetings", "wassup", "hello"]
    resp = ["hi", "hey", "hola", "hello", "hey there"]

    for word in command.split():
        if word.lower() in req:
            return random.choice(resp) + "."

    return ""


# Function to retrieve IP address
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def wiki(command):
    list_wiki = command.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "search" and list_wiki[i + 1].lower() == "":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


def send_email(t, cont):
    server = smtplib.SMTP("smtp.gmail.com", 123)
    server.ehlo()
    server.starttls()
    server.login("email", "pass")
    server.sendmail("email", t, cont)
    server.close()


def note(command):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])


def calculate(text):
    app_id = "YK2Y63-46W8GJWYYU"
    client = wolframalpha.Client(app_id)
    ind = text.lower().find("calculate")
    query = text[ind + 10:]
    res = client.query(query)
    answer = next(res.results).text
    speak = "The answer is " + answer
    print("Assistant: " + speak)


def google_calendar():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '../../VirtualAssistant/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def calendar_events(num, service):

    talk(f'Hey ! Have a good Day. Hope you are doing fine. These are the events to do today')
    # Call the Calendar API
    timer = datetime.datetime.utcnow().isoformat() + 'Z'
    print(f'Getting the upcoming {num} events')
    events_result = service.events().list(calendarId='primary', timeMin=timer, maxResults=num, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        talk('No upcoming events found!')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        events_today = (event['summary'])
        start_time = str(start.split("T")[1].split("-")[0])  # get the hour the event starts
        if int(start_time.split(":")[0]) < 12:  # if the event is in the morning
            start_time = start_time + "am"
        else:
            start_time = str(int(start_time.split(":")[0]) - 12)
            start_time = start_time + "pm"
        talk(f'{events_today} at {start_time}')
try:
    service = google_calendar()
    calendar_events(10, service)
except:
    talk("Please try again later.")
