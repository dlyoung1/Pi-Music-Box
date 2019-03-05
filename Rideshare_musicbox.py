from guizero import App, Text, PushButton, Picture, Combo, CheckBox, Window, yesno
from pygame import*
import pygame.mixer
import os
import random

app = App(title="RIDESHARE MUSIC BOX", bg="RoyalBlue3", height="320", width="480")

pygame.init()
pygame.mixer.init()

#----------------------------------------------------Get Rock Directories------------------------
def rock_out():
    window = Window(app, title="ROCK", height="320", width="480", bg="firebrick4", layout="grid")  
    def close_rock_out():
        window.hide()
    welcome_message = Text(window, text="ROCK", size=30, font="Courier New", color="white", grid=[3, 0])
    classicrock_button = PushButton(window, width=14, command=play_classicrock, text="Classic Rock", grid=[1, 2])
    classicrock_button.text_color = "white"
    classicrock_button.text_size = "12"
    classicrock_button.font = "Courier New"
    alternative_button = PushButton(window, width=14, command=play_alternative, text="Alternative", grid=[3, 2])
    alternative_button.text_color = "white"
    alternative_button.text_size = "12"
    alternative_button.font = "Courier New"
    industrial_button = PushButton(window, width=14, command=play_industrial, text="Industrial", grid=[5, 2])
    industrial_button.text_color = "white"
    industrial_button.text_size = "12"
    industrial_button.font = "Courier New"
    metal_button = PushButton(window, width=14, command=play_metal, text="Metal", grid=[1, 4])
    metal_button.text_color = "white"
    metal_button.text_size = "12"
    metal_button.font = "Courier New"
    indie_button = PushButton(window, width=14, command=play_indie, text="Indie", grid=[3, 4])
    indie_button.text_color = "white"
    indie_button.text_size = "12"
    indie_button.font = "Courier New"
    pop_button = PushButton(window, width=14, command=play_pop, text="Pop", grid=[5, 4])
    pop_button.text_color = "white"
    pop_button.text_size = "12"
    pop_button.font = "Courier New"
    
    close_rock_out = PushButton(window, text="go back", command=close_rock_out, grid=[3, 6])
    close_rock_out.text_color = "white"
    close_rock_out.font = "Courier New"
    
def play_alternative():
    get_files(directories[0])
def play_classicrock():
    get_files(directories[1])
def play_industrial():
    get_files(directories[2])
def play_metal():
    get_files(directories[3])
def play_indie():
    get_files(directories[4])
def play_pop():
    get_files(directories[5])

#--------------------------------------------Get R&B Directories----------------------------------------
def get_hip():
    window = Window(app, title="R&B", height="320", width="480", bg="light slate blue")
    def close_get_hip():
        window.hide()
    welcome_message = Text(window, text="R&B", size=30, font="Arial", color="white", align="top")
    hiphop_button = PushButton(window, command=play_hiphop, text="Hip Hop", align="left")
    hiphop_button.text_color = "purple4"
    hiphop_button.text_size = "12"
    hiphop_button.font = "Arial"
    hiphop_button.bg = "white"
    classicrb_button = PushButton(window, command=play_classicrb, text="Classic R & B", align="right")
    classicrb_button.text_color = "purple4"
    classicrb_button.text_size = "12"
    classicrb_button.font = "Arial"
    classicrb_button.bg = "white"
    close_get_hip = PushButton(window, text="go back", command=close_get_hip, align="bottom")
    close_get_hip.text_color = "purple4"
    close_get_hip.text_size = "12"
    close_get_hip.font = "Arial"
    close_get_hip.bg = "white"

def play_hiphop():
    get_files(directories[6])
def play_classicrb():
    get_files(directories[7])

#------------------------------------Other Music Directories-----------------------------------------------
def be_different():
    window = Window(app, title="OTHER", height="320", width="480", bg="mint cream", layout="grid")
    def close_other():
        window.hide()
    welcome_message = Text(window, text="Other Genres", size=24, font="Arial", color="dark slate gray", grid=[3, 0])
    techno_button = PushButton(window, width=13, command=play_techno, text="Techno", grid=[1, 1])
    techno_button.text_color = "dark slate gray"
    techno_button.text_size = "12"
    techno_button.font = "Arial"
    techno_button.bg = "white"
    classical_button = PushButton(window, width=13, height=2, command=play_classical, text="Classical", grid=[3, 1])
    classical_button.text_color = "dark slate gray"
    classical_button.text_size = "12"
    classical_button.font = "Arial"
    classical_button.bg = "white"
    jazz_button = PushButton(window, width=13, command=play_jazz, text="Jazz", grid=[5, 1])
    jazz_button.text_color = "dark slate gray"
    jazz_button.text_size = "12"
    jazz_button.font = "Arial"
    jazz_button.bg = "white"
    blues_button = PushButton(window, width=13, height=2, command=play_blues, text="Blues", grid=[1, 2])
    blues_button.text_color = "dark slate gray"
    blues_button.text_size = "12"
    blues_button.font = "Arial"
    blues_button.bg = "white"
    country_button = PushButton(window, width=13, command=play_country, text="Country", grid=[3, 2])
    country_button.text_color = "dark slate gray"
    country_button.text_size = "12"
    country_button.font = "Arial"
    country_button.bg = "white"
    folk_button = PushButton(window, width=13, height=2, command=play_folk, text="Folk", grid=[5, 2])
    folk_button.text_color = "dark slate gray"
    folk_button.text_size = "12"
    folk_button.font = "Arial"
    folk_button.bg = "white"
    latin_button = PushButton(window, width=13, command=play_latin, text="Latin", grid=[1, 3])
    latin_button.text_color = "dark slate gray"
    latin_button.text_size = "12"
    latin_button.font = "Arial"
    latin_button.bg = "white"
    new_age_button = PushButton(window, width=13, height=2, command=play_new_age, text="New Age", grid=[3, 3])
    new_age_button.text_color = "dark slate gray"
    new_age_button.text_size = "12"
    new_age_button.font = "Arial"
    new_age_button.bg = "white"
    spiritual_button = PushButton(window, width=13, command=play_spiritual, text="Spiritual", grid=[5, 3])
    spiritual_button.text_color = "dark slate gray"
    spiritual_button.text_size = "12"
    spiritual_button.font = "Arial"
    spiritual_button.bg = "white"
    close_other = PushButton(window, width=13, text="go back", command=close_other, grid=[5, 5])
    close_other.text_color = "dark slate gray"
    close_other.text_size = "12"
    close_other.font = "Arial"
    close_other.bg = "white"

def play_techno():
    get_files(directories[8])
def play_classical():
    get_files(directories[9])
def play_jazz():
    get_files(directories[10])
def play_blues():
    get_files(directories[11])
def play_country():
    get_files(directories[12])
def play_folk():
    get_files(directories[13])
def play_latin():
    get_files(directories[14])
def play_new_age():
    get_files(directories[15])
def play_spiritual():
    get_files(directories[16])

#------------------------------------------Random Directory----------------------------
def randomize():
    get_files(directories[(random.randint(0, 16))])
    
#-------------------------------------------Get Files----------------------------------
def get_files(directory):
    files=[]
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            files.append(filename)
    playMusic(files, directory)

def playMusic(files, directory):
    if shuffle_checkbox.value == 1:
        song = files.pop(random.randint(0,len(files)-1))
    else:
        song = files.pop()
    pygame.mixer.music.load(directory + song)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    pygame.mixer.music.play()
    print("Now Playing: " + song[3:len(song)-4])
    continue_playing(files, directory, song)
    
def continue_playing(files, directory, song):
    continue_alert = yesno("Song", "Title:\n" + song[3:len(song)-4] + "\n\n-Do you like this song?")
    if continue_alert == False:
        app.update()
    else:
        running = True
        app.update()
        play_next(files, directory, running)

def play_next(files, directory, running):
    while running:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if files:
                    if shuffle_checkbox.value == 1:
                        song = files.pop(random.randint(0,len(files)-1))
                    else:
                        song = files.pop()
                    pygame.mixer.music.load(directory + song)
                    pygame.mixer.music.play()
                    print("Now Playing: " + song[3:len(song)-4])
                    continue_playing(files, directory, song)

directories = ["/home/pi/Music/Alternative/", "/home/pi/Music/Classic Rock/", "/home/pi/Music/Industrial/", "/home/pi/Music/Metal/", "/home/pi/Music/Indie/", "/home/pi/Music/Pop/",
                "/home/pi/Music/Funk/", "/home/pi/Music/Funk/",
                "/home/pi/Music/Techno/", "/home/pi/Music/Classical/", "/home/pi/Music/Jazz/", "/home/pi/Music/Blues/", "/home/pi/Music/Country/", "/home/pi/Music/Folk/",
                 "/home/pi/Music/Latin/", "/home/pi/Music/New Age/", "/home/pi/Music/Spiritual/"]

welcome_message = Text(app, text="PICK YOUR PLAYLIST", size = 30, font="Georgia", color="midnight blue")

rock_button = PushButton(app, width="fill", height=2, command=rock_out, text="ROCK")
rock_button.text_color = "white"
rock_button.text_size = "12"
rock_button.font = "Georgia"

rb_button = PushButton(app, width="fill", height=2, command=get_hip, text="R & B")
rb_button.text_color = "white"
rb_button.text_size = "12"
rb_button.font = "Georgia"

other_button = PushButton(app, width="fill", height=2, command=be_different, text="OTHER")
other_button.text_color = "white"
other_button.text_size = "12"
other_button.font = "Georgia"

random_button = PushButton(app, width="fill", height=2, command=randomize, text="RANDOM")
random_button.text_color = "white"
random_button.text_size = "12"
random_button.font = "Georgia"

shuffle_checkbox = CheckBox(app, width=20, text="shuffle")
shuffle_checkbox.text_color = "white"
shuffle_checkbox.text_size = "12"
shuffle_checkbox.font = "Georgia"

app.display()
