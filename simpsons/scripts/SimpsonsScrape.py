#!/usr/local/var/pyenv/shims/python

import pandas as pd
import csv
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Only use a few episodes
# 14 Bart gets an F
# 39 Bart the Murderer
# 60 Kamp Krusty
# 66 Marge Gets a Job
# 130 Radioactive Man
# 133 Lisa the Vegetarian
# 189 All Singing, All Dancing
#episodes = [14, 39, 60, 66, 130, 133, 189]

stop_words = set(stopwords.words('english'))

episodeTexts = {}
episodes = []
episodeLabels = {}
episodeSeasons = {}

episodeData = pd.read_csv('simpsons_episodes.csv')
for index, row in episodeData.iterrows():
  #epTitle = episodeData.loc[(episodeData['number_in_series'] == epID), 'title']
  epTitle = row['title']
  epID = row['id']
  seasonID = row['season']
  episodeLabels[str(epID)] = str(seasonID) + "_" + str(epID) + "_" + epTitle
  episodeSeasons[str(epID)] = "Season " + str(seasonID)
  print(epID, epTitle)
  if (epID not in episodes):
    episodes.append(epID)
    episodeTexts[str(epID)] = ""

episodes = sorted(episodes)

with open('simpsons_script_lines.csv', newline='') as scriptFile:
  reader = csv.reader(scriptFile)
  for line in reader:
    if(len(line) < 12):
      print("row too short: " + str(line))
    #lineA = line.strip().split()
    if (line[0] == 'id'):
      continue
    epID = line[1]
    #if (int(epID) in episodes):
    normText = line[11]
    if (normText.strip() != ""):
      episodeTexts[epID] += normText + " "

labelsFile = open("episode_labels.txt", 'w')
seasonsFile = open("episode_seasons.txt", 'w')

with open("parsed_episodes.txt", 'w') as episodeFile:
  for epID in episodes:
    epText = episodeTexts[str(epID)].strip()
    epTitle = episodeLabels[str(epID)]
    epSeason = episodeSeasons[str(epID)]
    if (epText == ''):
      print("EMPTY EPISODE TEXT:",epID,epTitle)
      continue

    # This section removes English stopwords from the text
    #epTokens = word_tokenize(epText)
    #epTextFiltered = [w for w in epTokens if not w in stop_words]
    #episodeFile.write(" ".join(epTextFiltered) + "\n")

    episodeFile.write(epText + "\n")

    labelsFile.write(epTitle + "\n")
    seasonsFile.write(epSeason + "\n")
