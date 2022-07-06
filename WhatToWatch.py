import webbrowser
import random

"""
PLAN:
    pulls the stream title, and 
    current game of specifeid streamers, with an if online check
    also gets top recommended youtube videos
"""

#I should make an option to just userInput the index instead of the full name

streamerTwitch = ["valorant", "rocketleague", "aceu", "tarik", "iitztimmy", "daltoosh", "shahzam"]
def getStreamer():
    userInput = ""
    while userInput not in streamerTwitch:
        for name in streamerTwitch:
            print(name)
        userInput = input("What stream do you want to watch: ")
        userInput = userInput.lower()
        if userInput == "random":
            return random.choice(streamerTwitch)
    return userInput

def goToTwitchLink(name):
    chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s' #file path to the Chrome app, otherwise it opens in IE
    webbrowser.get(chrome_path).open('twitch.tv/' + name)

#TO GET TO TWITCH STREAMERS ONLY



#name : actual link address
youtubeChannels = {"Ludwig": "Ludwigahgren", "Lashmak": "Lashmak", "Linus Tech Tips": "LinusTechTips", "Tom Scott": "TomScottGo"}
def getYoutuber():
    userInput = ""
    while userInput not in youtubeChannels:
        for name in youtubeChannels:
            print(name)
        userInput = input("What youtuber do you want to watch: ")
        userInput = userInput.title()
        if userInput == "Random":
            return random.choice(youtubeChannels)
    userInput = youtubeChannels[userInput]
    return userInput

def goToYoutubeLink(name):
    chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s' #file path to the Chrome app, otherwise it opens in IE
    webbrowser.get(chrome_path).open('youtube.com/c/' + name)
#Youtube only



#songname : link , timestamp can be added also just add "&t=time" (seconds) at the end
youtubeMusic = {"Juice WRLD FreeStyle 60 mins": "fSoT13msPe4&t" , "Juice WRLD Black and White": "aQDhBNHBQUs" , "Pop Smoke Shake The Room": "zd8uWVh8b8k" , "Yeat Minions" : "7fX2kMaiMGI"}
def getYoutubeMusic():
    userInput = -1
    while userInput not in range(len(youtubeMusic) + 1) or userInput == 0:
        for index , songName in enumerate(youtubeMusic, start=1): #more user friendly
            print(str(index) + ": " + songName)
        userInput = input("What Song do you want to listen to (index please): ")
        if userInput == "random":
            return random.choice(list(youtubeMusic.values()))
        userInput = int(userInput)
    return list(youtubeMusic.values())[userInput - 1]

def goToYoutubeMusicLink(linkchars):
    chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s' #file path to the Chrome app, otherwise it opens in IE
    webbrowser.get(chrome_path).open('youtube.com/watch?v=' + linkchars)
    
    
    
allChannels = []#used for the surprise me hidden feature
allChannels.extend(streamerTwitch)
allChannels.extend(youtubeChannels.values())
allChannels.extend(youtubeMusic.values())



watching = input("What do you want to watch (youtube or twitch)?: ")#"surprise" is the secret word
if watching == "twitch":
    name = getStreamer()
    goToTwitchLink(name)
if watching == "youtube":
    vidType = input("video or music (v,m): ").lower()
    if vidType == "v":
        name = getYoutuber()
        goToYoutubeLink(name)
    if vidType == "m":
        linkchars = getYoutubeMusic()
        goToYoutubeMusicLink(linkchars)
if watching == "surprise":
    randchoice = random.choice(allChannels)
    if randchoice in streamerTwitch:
        goToTwitchLink(randchoice)
    if randchoice in youtubeChannels.values():
        goToYoutubeLink(randchoice)
    if randchoice in youtubeMusic.values():
        goToYoutubeMusicLink(randchoice)