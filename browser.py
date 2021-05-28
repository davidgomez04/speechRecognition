import webbrowser
from search_engine_parser import GoogleSearch

CHROME_PATH = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def createURL(webpage):
    url = 'http://' + webpage + '.com/'
    return url

def parseSpeech(audio):
    command = audio.split()
    action = command[0]
    text = command[1:]
    print("Query: ", text)

    app = ""
    action = action.lower()

    if action == "search":
        openWebsite(text)
    if action == "open":
        openApp(app)
    if action == "google":
        googleSearch(text)

def openApp(app):
    print("Inside app")

def googleSearchResults(query):
    gsearch = GoogleSearch()
    results = gsearch.search(query)
    return results
    #print(results['links'])
    #print(GoogleSearch(query, num_results=20))

def googleSearch(query):
    googleSearchResults(query)
    #TODO: Improve the query for the google search
    url = 'https://www.google.com/search?q='
    for q in query:
        url += q + "+" #https://www.google.com/search?q=mic+for+airpods
    print("Url: ", url)
    webbrowser.get(CHROME_PATH).open(url)

def openWebsite(webpage):

    url = createURL(webpage)

    #TODO: setup chrome path for different OS
    # MacOS
    #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # Windows
    #chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'

    webbrowser.get(CHROME_PATH).open(url)