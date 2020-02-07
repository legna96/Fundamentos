import os

folderDownload = os.path.join(os.getcwd(), "downloads")
folderDownloadMusic = os.path.join(folderDownload,"music")
folderDownloadOnlyVideo = os.path.join(folderDownload,"only-video")
folderDownloadVideo = os.path.join(folderDownload,"video")

def checkDownloadFolder():

    global folderDownload
    global folderDownloadMusic
    global folderDownloadOnlyVideo
    global folderDownloadVideo

    if not os.path.exists(folderDownload):
        os.mkdir(folderDownload)
        os.mkdir(folderDownloadMusic)
        os.mkdir(folderDownloadVideo)
        print("all folders have been created")
    
    if not os.path.exists(folderDownloadMusic):
        os.mkdir(folderDownloadMusic)
        print("the music folder have been created")
    
    if not os.path.exists(folderDownloadOnlyVideo):
        os.mkdir(folderDownloadOnlyVideo)
        print("the only-video folder have been created")
    
    if not os.path.exists(folderDownloadVideo):
        os.mkdir(folderDownloadVideo)
        print("the video folder have been created")

def cleanConsole():
    os.system('cls')