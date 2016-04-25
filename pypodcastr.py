import feedparser
import urllib
import os
import sys

#Read what podcasts to download
f = open(".podcasts.pod", "r")
podcasts = f.readlines()
f.close()

try:
  if sys.argv[1] == "--add":
    podcasts.append(str(sys.argv[2])+"\n")
    f = open(".podcasts.pod", "w")
    for line in podcasts:
      f.write(line)
    f.close()
    
    print("Starting")
except:
  print("Starting")

#For all the podcasts download the latest
#if the latest is not in the .lastdownload file
#if it is just skip
for podcast in podcasts:
  feed = feedparser.parse(podcast)
  #Make correct podcast directories
  if not (os.path.exists("/home/bryce/Podcasts/" + feed.feed.title + "/")):
    os.mkdir("/home/bryce/Podcasts/" + feed.feed.title + "/")
  
  #Try to read in last downloaded files
  try:
    f = open(".lastdownloaded", "r")
    lastdownloaded = f.readlines()
    f.close()
  except:
    for key in feed["entries"]:
      print("Downloading: ", key["title"])
      urllib.request.urlretrieve(key["link"], "/home/bryce/Podcasts/" + feed.feed.title + "/" + key["title"] + ".mp3")
      f = open(".lastdownloaded", "a")
      f.write(key["title"] + "\n")
      f.close()
      break
    f = open(".lastdownloaded", "r")
    lastdownloaded = f.readlines()
    f.close
  
  for key in feed["entries"]:
    if (key["title"] + "\n") in lastdownloaded:
      print(key["title"] + " already downloaded...skipping")
    else:
      print("Downloading: ", key["title"])
      urllib.request.urlretrieve(key["link"], "/home/bryce/Podcasts/" + feed.feed.title + "/" + key["title"] + ".mp3")
      f = open(".lastdownloaded", "a")
      f.write(key["title"] + "\n")
      f.close()

print("Podcasts are up to date")

