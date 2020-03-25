from api import *
import time
from multiprocessing import Process

def menu():

    opt = -1

    while opt is -1:

        cleanConsole()

        print("Fili arl - Youtube Downloader", end="\n\n")
        
        try:
            # input the youtube url
            url = input("Insert a youtube's url: ")
            pf = pafy.new(url) 

        except Exception:
            print("Option Invalid.!, Try again.")
            opt = retard(1)
            continue

        # show video's information
        try:
            print(f"Title: {pf.title}")
            print(f"Duration: {round( pf.length/60, 2)} min")
            print(f"Date: {pf.published}")
            print(f"Description:\n{pf.description}", end="\n\n")
            
        except Exception:
            print("not all information have been found", end="\n\n")

        # show menu's options
        
        print("1.- Download Only Video")
        print("2.- Download Only Audio")
        print("3.- Download Video")
        print("4.- Download Mp3")
        print("5.- Exit")

        try:
            opt = int(input("Option: "))

            if opt is 1:
                download(pf.videostreams, "Download Only Video")
                opt = retard(5)
            
            elif opt is 2:
                download(pf.audiostreams, "Download Only Audio")
                opt = retard(5)

            elif opt is 3:
                download(pf.streams, "Download Video")
                opt = retard(5)

            elif opt is 4:
                bestmp4 = pf.getbest(preftype="mp4")
                downloadMp3(bestmp4,"Download Mp3")
                opt = retard(5)
            
            elif opt is 5:
                print("Good Bye..!")
                opt = retard(1)
            
            else:
                print("Option Invalid.!, Try again.")
                opt = retard(1)

        except Exception:
            print("Option Invalid.!, Try again.")
            opt = retard(1)
            
def retard(s):
    time.sleep(s)
    return -1

def downloadMp3(bestmp4, titleOption):
    cleanConsole() 
    # show info
    print(f"-- {titleOption} --", end="\n\n")
    title = f"{bestmp4.title}.{bestmp4.extension}"
    # download video and get his filename

    folderMusic = getFolder("audio")

    if os.path.exists( os.path.join(folderMusic, f"{bestmp4.title}.mp3") ):
        print(f"\n\nYou have already downloaded this before, check the folder {folderMusic}")

    else:
        filename = downloadStream(bestmp4, "audio", title)
        # create child process for convert mp4 to mp3
        p = Process(target=convertMp4toMp3, args=(filename,bestmp4.title))
        p.start()
        p.join()
        # when child process terminated, process parent remove video mp4
        removeMp4(filename)
        print(f"\n\nDownload Complete!. Check the in path: {folderMusic}")

def download(streams, titleOption):

    opt = -1

    while opt is -1:
        cleanConsole() 
        print(f"-- {titleOption} --", end="\n\n")
        printOptions(streams)
        numStreams = sizeStreams(streams)

        try:
            opt = int(input("insert option: "))
        
            if opt > 0 and opt <= numStreams:
                stream = streams[opt-1]
                title = f"{stream.title}.{stream.extension}"
                downloadStream(stream, stream.mediatype, title)
            else:
                print("Option Invalid, Try again.")
                opt = retard(1)

        
        except Exception:
            print("Option Invalid, Try again.")
            opt = retard(1)

if __name__ == "__main__":
    menu()