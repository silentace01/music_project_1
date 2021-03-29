#Author      :> Abhishek Das
#Code Writer :> silentace(Author)
#Date        :> 02/03/2021
#Location    :> India/West Bengal

from playsound import playsound #import play sound to play msuic 
from os import listdir #import listdir for music search and print the list
option = input("Add Music Path: ")+"\\"
option = option.replace("\\","\\\\")
path = option
#path = "C:\\Users\\silentace\\Documents\\silentace\\python\\music_search\\" 
#music path folder need to chanage  
music_list = listdir()

error = "Something wrong try again ------> "
while True:
    number_count = 0
    option = input("1 For Search\n2 For Number\n3 For Music List\n4 For Exit\n:> ")
    #asking user for mode
    if(option=="1"):
        #entered song name will directly play 
        while True:
            try:
             song_name = input("Song Name :> ")+".mp3"
             final_music = path+song_name
             break

            except Exception as e:  
                print(error)
                continue
    elif(option=="2"): 
        #find the music list number and play The music
        while True:
            print("Music List")
            for item in music_list:
                number_count = 1+number_count
                print(number_count,":",item)
            try:
                song_number = int(input("Song Number :> "))
                song_name =  music_list[song_number-1]
                final_music = path+song_name
                break
            except Exception as e:
                print(error)
                continue
    elif(option=="3"):
        #printing music lsit for user 
        print("Music List")
        for item in music_list:
            number_count = 1+number_count
            print(number_count,":",item)
        print("")
        continue
    elif(option=="4"): 
        #exit program
        print("Thanks For Using\nCode By silentace")
        break
    else:
        print(error)
        continue
    try:
        print("Playing Music : "+song_name)
        print("code by silentace") 
        #player
        playsound(final_music)
    except Exception as e :
        print(error)
        continue
