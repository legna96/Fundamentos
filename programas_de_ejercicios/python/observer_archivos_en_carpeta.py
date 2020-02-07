import os, time, sys, fnmatch, datetime

path_to_watch = "C:\Users\pc1\Desktop\pruebas"

def findCoffeeFiles():
  matches = []
  for root, dirnames, filenames in os.walk(path_to_watch):
    for filename in fnmatch.filter(filenames, '*.*'):
      matches.append(os.path.join(root, filename))
  return matches


def out(str):
  print str
  sys.stdout.flush()



out("Monitoring folder GL's CTRL's" + path_to_watch)

before = dict ((f, os.path.getmtime(f)) for f in findCoffeeFiles())

while 1:
  time.sleep (1)
  after = dict ((f, os.path.getmtime(f)) for f in findCoffeeFiles())
  added = [f for f in after.keys() if not f in before.keys()]
  removed = [f for f in before.keys() if not f in after.keys()]
  if added: out(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Added: " + ", ".join (added))
  if removed: out(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " Removed: " + ", ".join (removed))
  before = after
