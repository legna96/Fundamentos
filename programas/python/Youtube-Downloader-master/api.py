from helpers import *
import pafy
from moviepy.video.io.VideoFileClip import VideoFileClip

def myCallback(total, downloaded, ratio, rate, eta):
    print(f"Total:{round(total/(1024*1024),2)}MB, Download:{round(downloaded/(1024*1024),2)}MB, {int(ratio*100)}%, {round(rate,2)} kbps, {round(eta,2)}s")

def printOptions(streams):
    option = 0
    for stream in streams:
        option += 1
        print(f"{option}.- Resolution:{stream.resolution}, Extension:{stream.extension},  Size:{round(stream.get_filesize()/(1024*1024),2)}MB")
    print(end="\n\n")

def sizeStreams(streams):
    return len(streams)

def downloadStream(stream, type, title):

    global folderDownloadMusic
    global folderDownloadOnlyVideo
    global folderDownloadVideo

    checkDownloadFolder()
    
    if type is "audio":
        folder = folderDownloadMusic
    elif type is "video":
        folder = folderDownloadOnlyVideo
    else:
        folder = folderDownloadVideo

    if os.path.exists( os.path.join(folder, title) ):
        print(f"\n\nYou have already downloaded this before, check the folder {folder}")
    
    else:
        filename = stream.download( filepath=os.path.join(folder, title), quiet=True, callback=myCallback )
        print(f"\n\nDownload Complete!. Check the in path: {filename}")
        return filename

def getFolder(type):
    
    global folderDownloadMusic
    global folderDownloadOnlyVideo
    global folderDownloadVideo 

    if type is "audio":
        folder = folderDownloadMusic
    elif type is "video":
        folder = folderDownloadOnlyVideo
    else:
        folder = folderDownloadVideo

    return folder

def convertMp4toMp3(filenamemp4, title):
    video = VideoFileClip(filenamemp4)
    video.audio.write_audiofile(os.path.join(os.getcwd(), "downloads","music",f"{title}.mp3"))

def removeMp4(filename):
    os.remove(filename)