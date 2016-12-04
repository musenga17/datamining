# coding: utf-8

import csv

fichiers = ['2007:2008.csv','2008:2009.csv','2009:2010.csv','2010:2011.csv','2011:2012.csv','2012:2013.csv','2013:2014.csv','2014:2015.csv','2015:2016.csv','2016:2017.csv']

teams = []

#for fic in fichiers :
for fic in fichiers :
    teams = []
    seasonFile = open('SaisonsValides/'+fic+'','r')
    reader = csv.reader(seasonFile,delimiter=',')
    for row in reader :
        homeTeam = row[2]
        awayTeam = row[3]
        if homeTeam not in teams :
	    teams.append(homeTeam)
        if awayTeam not in teams :
	    teams.append(awayTeam)
    seasonFileTest = open('SaisonsValides/Test'+fic+'','w')
    writer = csv.writer(seasonFileTest,delimiter=',',dialect='excel',lineterminator='\n')
    numMatch = 0
    matchSeen = []
    for team in teams :
        numJ = 1
        seasonFile = open('SaisonsValides/'+fic+'','r')
        reader = csv.reader(seasonFile,delimiter=',')
        for row in reader :
            if team == row[2] or team == row[3] :
                if row[0] not in matchSeen :
                    toInsert = row
                    toInsert.insert(1,numJ)
                    writer.writerow(toInsert)
                    matchSeen.append(row[0])
                numJ = numJ + 1
