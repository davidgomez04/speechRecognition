import webbrowser

def openWebsite(site):

    print("Inside browser function")

    url = 'http://docs.python.org/'

    # MacOS
    #chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

    # Windows
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

    # Linux
    # chrome_path = '/usr/bin/google-chrome %s'

    webbrowser.get(chrome_path).open(url)

openWebsite()