#!/usr/bin/env python3
import feedparser
import urllib
import os
import sys

podcastdir = os.getenv("HOME")+"/Podcasts/"

#Add a podcast
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

#try to read what podcasts to download
try:
  f = open(".podcasts.pod", "r")
  podcasts = f.readlines()
  f.close()
except:
  print("Please add some podcasts to catch")
  sys.exit()

#For all the podcasts download the latest
#if the latest is not in the .lastdownload file
#if it is just skip
for podcast in podcasts:
  feed = feedparser.parse(podcast)

  #Make sure there is a podcast folder
  if not(os.path.exists(podcastdir)):
    os.mkdir(podcastdir)

  #Make correct podcast directories
  if not (os.path.exists(podcastdir + feed.feed.title + "/")):
    os.mkdir(podcastdir + feed.feed.title + "/")
  
  #Try to read in last downloaded files
  try:
    f = open(".lastdownloaded", "r")
    lastdownloaded = f.readlines()
    f.close()
  except:
    lastdownloaded = []
  
  for key in feed["entries"]:
    if (key["title"] + "\n") in lastdownloaded:
      print(key["title"] + " already downloaded...skipping")
    else:
      print("Downloading: ", key["title"])
      urllib.request.urlretrieve(key["link"], podcastdir + feed.feed.title + "/" + key["title"] + ".mp3")
      f = open(".lastdownloaded", "a")
      f.write(key["title"] + "\n")
      f.close()
    break
print("Podcasts are up to date")

