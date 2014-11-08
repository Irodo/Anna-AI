import time
import os

print ("Hello My Name Is Anna")

while True:
    comp = input()
    if comp =="Anna":
        os.system("start C:/Users/Nathan/AI/speech/atcommand.mp3")
        instr = input("I'm at your command")
    else:
        os.system("start C:/Users/Nathan/AI/speech/cannot_interpret.mp3")
    if instr == "Play The Next Episode":
        os.system("start C:/Users/Nathan/AI/speech/playingtne.mp3")
        time.sleep(3.0)
        os.system("start C:/Users/Nathan/AI/music/TheNextEpisode.mp3")
    elif instr == "Who is your creator?":
        os.system("start C:/Users/Nathan/AI/speech/nathan_blake.mp3")
    elif instr == "What are you up to Anna?":
        print ("Not much")
    elif instr == "Do you want to build a snowman?":
        print ("Does it have to be a snowman?")
    elif instr == "Play Cant Hold Us":
        os.system("start C:/Users/Nathan/AI/speech/playing_cant_hold_us_by_macklemore.mp3")
        time.sleep(3.0)
        os.system("start C:/Users/Nathan/AI/music/cantholdus.mp3")
    elif instr == "Show me some cats":
        os.system("start C:/Users/Nathan/AI/speech/showing_pictures_of_cats.mp3")
        time.sleep(1.0)
        os.system("start C:/Users/Nathan/AI/images/cat.jpg")
    elif instr == "Open Google Chrome":
        os.system("start C:/Users/Nathan/AI/speech/opening_google_chrome.mp3")
        os.system("start C:/Users/Nathan/AI/browsers/google")
    elif instr == "Open Internet Explorer":
        os.system("start C:/Users/Nathan/AI/speech/opening_internet_explorer.mp3")
        os.system("start C:/Users/Nathan/AI/browsers/internetexplorer")
    elif instr == "Open Minecraft":
        os.system("start C:/Users/Nathan/AI/speech/running_minecraft.mp3")
        os.system("start C:/Users/Nathan/AI/apps/Minecraft")
    elif instr == "Open Tekkit":
        os.system("start C:/Users/Nathan/AI/speech/running_tekkit.mp3")
        os.system("start C:/Users/Nathan/AI/apps/TechnicLauncher")
    elif instr == "Open Skype":
        os.system("start C:/Users/Nathan/AI/speech/running_skype.mp3")
        os.system("start C:/Users/Nathan/AI/apps/Skype")
    elif instr == "Play Flight":
        os.system("start C:/Users/Nathan/AI/speech/playingf.mp3")
        time.sleep(3.0)
        os.system("start C:/Users/Nathan/AI/music/flight.mp3")
    elif instr == "Play Rap God":
        os.system("start C:/Users/Nathan/AI/speech/playingrg.mp3")
        time.sleep(2.0)
        os.system("start C:/Users/Nathan/AI/music/rapgod.mp3")
    else:
        os.system("start C:/Users/Nathan/AI/speech/cannotinterpret.mp3")

    
       

