# coding: utf-8
import csv

fichiers = ['2007:2008','2008:2009','2009:2010','2010:2011','2011:2012','2012:2013','2013:2014','2014:2015','2015:2016','2016:2017']
Xfile = open('X_final.csv','w')
Yfile = open('Y_final.csv','w')

Xwriter = csv.writer(Xfile,delimiter=',',dialect='excel',lineterminator='\n')
Ywriter = csv.writer(Yfile,delimiter=',',dialect='excel',lineterminator='\n')

for fic in fichiers :
    seasonFile = open('SaisonsStatsFinales/'+fic+'_Stats_final.csv','r')
    reader = csv.reader(seasonFile,delimiter=",")
    for row in reader :
        Xwriter.writerow(row[1:len(row)-1])
        Ywriter.writerow(row[len(row)-1:])
