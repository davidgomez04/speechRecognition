import webbrowser

def createURL(webpage):
    url = 'http://' + webpage + '.com/'
    return url


def parseSpeech(audio):
    command = audio.split()
    action = command[0]
    webpage = command[1]
    app = ""
    if action == "search":
        openWebsite(webpage)
    if action == "open":
        openApp(app)

def openApp(app):
    print("Inside app")

def openWebsite(webpage):

    #url = 'http://docs.python.org/'

    url = createURL(webpage)

    # MacOS
    #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'

    webbrowser.get(chrome_path).open(url)

#openWebsite()