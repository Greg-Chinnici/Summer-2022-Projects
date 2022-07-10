import webbrowser
import random

#main goal is to make a tv guide
"""
PLAN:
use this: https://dev.twitch.tv/docs/api/reference#get-streams
    or
    https://github.com/Teekeks/pyTwitchAPI
    
    pulls the stream title, and 
    current game of specifeid streamers, with an if online check
    also gets top recommended youtube videos
    
make the chrome path wrok for macOS too
"""
#! chrome path manual switch
currentOS = "windows"
if (currentOS == "windows"):
    chrome_path = '"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" %s' #file path to the Chrome app, otherwise it opens in IE
else:
    chrome_path = "whatever the macOS path is"#!do this later



#I should make an option to just userInput the index instead of the full name
streamerTwitch = ["valorant", "rocketleague", "playapex", "aceu", "tarik", "prod", "daltoosh", "iitztimmy", "shahzam", "hiko", "kitboga"]
def getStreamer():
    userInput = ""
    while userInput not in streamerTwitch:
        for name in streamerTwitch:
            print(name)#this is where I want to use the isLive authenitcation
        userInput = input("What stream do you want to watch: ")
        userInput = userInput.lower()
        if userInput == "random":
            return random.choice(streamerTwitch)
    return userInput

def goToTwitchLink(name):
    webbrowser.get(chrome_path).open('twitch.tv/' + name)
#! twitch only



#name : actual link address , I could also add thier main video type ie: valorant, coding, bored watch
youtubeChannels = {#had to include the "c/" and "user/" because of legacy accounts
    "Linus Tech Tips": "c/LinusTechTips", 
    "Tom Scott": "c/TomScottGo",
    "Ludwig": "c/Ludwigahgren", 
    "The Yard": "c/TheYardPodcast",
    "Ethoslab": "user/EthosLab",
    "Lashmak": "c/Lashmak", 
    "direwolf20": "user/direwolf20",
    "Binging with Babish": "c/bingingwithbabish",
    "Sebastian Lague": "c/SebastianLague",
    "MichaelReeves": "c/MichaelReeves",
    "Prod Valorant": "channel/UC_L9jCsleYEyLhycNvj-6Gw"
    }
def getYoutuber():
    userInput = ""
    while userInput not in youtubeChannels:
        for name in youtubeChannels:
            print(name)
        userInput = input("What youtuber do you want to watch: ")
        userInput = userInput.title()
        if userInput == "Random":
            return random.choice(list(youtubeChannels.values()))
    userInput = youtubeChannels[userInput]
    return userInput

def goToYoutubeLink(name):
    webbrowser.get(chrome_path).open('youtube.com/' + name)
#! Youtube only



#songname : link , timestamp can be added also just add "&t=time" (seconds) at the end
youtubeMusic = {
    "Juice WRLD FreeStyle Eminem Beats": "fSoT13msPe4&t",
    "Juice WRLD freestyle 60 mins": "igc1wYW448w" ,
    "Juice WRLD Black and White": "aQDhBNHBQUs" , 
    "Pop Smoke Shake The Room": "zd8uWVh8b8k" , 
    "Yeat Minions" : "7fX2kMaiMGI" , 
    "Big Rap Playlist": "60-l6nNyK70&list=PLD3MHnA3bEH-lPyn3I5XCbab-ULH8wn9N", 
    "Trippie Red Sleepy Hallow": "1yzZwbFGLgo"
    }
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
    timeStamp = 0 #starts at 0 seconds in
    webbrowser.get(chrome_path).open('youtube.com/watch?v=' + linkchars + "&t=" + str(timeStamp))
#! music only



def goToNetflix():
    webbrowser.get(chrome_path).open("netflix.com/browse/m/continue-watching")
#!netflix



#! all channel stuff, for random and all
allChannels = []
def sortAllChannels(allChannels):
    allChannels.extend(["netflix"])
    allChannels.extend(streamerTwitch)
    allChannels.extend(list(youtubeChannels.keys()))
    allChannels.extend(list(youtubeMusic.keys()))


def getAllChoice():
    for cnt , item in enumerate(allChannels, start = 1):
        print(str(cnt) + ": " + item)
    userchoice = int(input("Which one do you want (index): "))
    return allChannels[userchoice - 1]



#! secondary senders
def watchingYoutube():
    vidType = ""
    while vidType != "c" and vidType != "m":
        vidType = input("channel or music (c,m): ").lower()
    if vidType == "c":
        name = getYoutuber()
        goToYoutubeLink(name)
    if vidType == "m":
        linkchars = getYoutubeMusic()
        goToYoutubeMusicLink(linkchars)

def watchingRandom():
    randchoice = random.choice(allChannels)
    if randchoice in streamerTwitch:
        goToTwitchLink(randchoice)
    elif randchoice in youtubeChannels.values():
        goToYoutubeLink(randchoice)
    elif randchoice in youtubeMusic.values():
        goToYoutubeMusicLink(randchoice)
    else:
        goToNetflix()

def watchingAllChoice():
    userchoice = getAllChoice()
    if userchoice in streamerTwitch:
        goToTwitchLink(userchoice)
    elif userchoice in list(youtubeChannels.keys()):
        userchoice = youtubeChannels.get(userchoice)
        goToYoutubeLink(userchoice)
    elif userchoice in list(youtubeMusic.keys()):
        userchoice = youtubeMusic.get(userchoice)
        goToYoutubeMusicLink(userchoice)
    else:
        goToNetflix()



#! main function
watching = input("What do you want to watch (youtube, twitch, netflix)?: ").lower()#"surprise" is the secret word
sortAllChannels(allChannels)
if watching == "netflix":
    goToNetflix()
elif watching == "twitch":
    goToTwitchLink(getStreamer())
elif watching == "youtube":
    watchingYoutube()
elif watching == "random" or watching == "surprise":
    watchingRandom()
else:#All Choice Activates
    watchingAllChoice()
