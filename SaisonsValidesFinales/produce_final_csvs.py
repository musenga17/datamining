# coding: utf-8
import csv

fichiers = ['2007:2008','2008:2009','2009:2010','2010:2011','2011:2012','2012:2013','2013:2014','2014:2015','2015:2016','2016:2017']

for fic in fichiers :
    season = open('../SaisonsValides/'+fic+'.csv','r')
    reader = csv.reader(season,delimiter=',')
    new_season = open(fic+'_final.csv','w')
    writer = csv.writer(new_season,delimiter=',',dialect='excel',lineterminator='\n')

    for row in reader :
        new_row = []
        new_row.extend([row[0],row[1],row[2],row[3],row[4]])
        new_row.append(int(row[5])-int(row[6]))
        new_row.append(int(row[6])-int(row[5]))
        butMTDom, butMTExt = int(row[7]), int(row[8])
        if butMTDom > butMTExt : new_row.append('H')
        elif butMTDom < butMTExt : new_row.append('A')
        else : new_row.append('D')
        tirsDom, tirsExt = int(row[9]), int(row[10])
        tcDom, tcExt = int(row[11]), int(row[12])
        new_row.extend([tcDom,tcExt])
        ratioTirsDom, ratioTirsExt = 0, 0
        if tirsDom != 0 : ratioTirsDom = '%.3f'%(float(tcDom)/tirsDom)
        if tirsExt != 0 : ratioTirsExt = '%.3f'%(float(tcExt)/tirsExt)
        new_row.extend([ratioTirsDom,ratioTirsExt])
        new_row.extend([int(row[15]),int(row[16])])
        new_row.extend([int(row[19]),int(row[20])])
        new_row.append(row[21])
        writer.writerow(new_row)
        
