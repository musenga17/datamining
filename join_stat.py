# coding: utf-8
import csv

fichiers = ['2007:2008_Stats.csv','2008:2009_Stats.csv','2009:2010_Stats.csv','2010:2011_Stats.csv','2011:2012_Stats.csv','2012:2013_Stats.csv','2013:2014_Stats.csv','2014:2015_Stats.csv','2015:2016_Stats.csv','2016:2017_Stats.csv']

Xfile = open('X.csv','w')
Yfile = open('Y.csv','w')

Xwriter = csv.writer(Xfile,delimiter=',',dialect='excel',lineterminator='\n')
Ywriter = csv.writer(Yfile,delimiter=',',dialect='excel',lineterminator='\n')

for fic in fichiers :
    seasonFile = open('saisonsStatsCSV/'+fic+'','r')
    reader = csv.reader(seasonFile,delimiter=",")
    for row in reader :
        Xwriter.writerow(row[1:len(row)-1])
        Ywriter.writerow(row[len(row)-1:])
