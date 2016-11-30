# coding: utf-8

import csv

def moy(val,step,newval) :
	return (val*step + float(newval))/(step+1)

teams = []
dico = {}

with open('SaisonsValides/2007:2008.csv') as csvfile :
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader :
			homeTeam = row[2]
			awayTeam = row[3]
			if homeTeam not in teams :
				teams.append(homeTeam)
			if awayTeam not in teams :
				teams.append(awayTeam)

                        
for team in teams :
	with open('SaisonsValides/2007:2008.csv') as csvfile :
		reader = csv.reader(csvfile,delimiter=',')
		L = []
		#mBmf : moyenne buts marques fin match #mBef : ------- ---- encaisses --- ----- #mBmh : moyenne buts marques mi temps #mBeh : ------- ---- encaisses -- ----- #ms : moyenne shoot #msc : moyenne shoot conscedes #mst : moyenne shoot target #mstc : moyenne shoot target conscedes #mfc : moyenne fautes commises #mfo : moyenne fautes obtenues #mc : moyenne corners #mcc : moyenne corners conscedes #my : moyenne cartons jaunes #mr : moyenne cartons rouges
		stat = {'team: ' : '' , 'match' : 0, 'home' : True , 'mBmf' : 0., 'mBef' : 0., 'mBmh' : 0., 'mBeh' : 0., 'ms' : 0., 'msc' : 0., 'mst' : 0., 'mstc' : 0., 'mfc' : 0., 'mfo' : 0., 'mc' : 0., 'mcc' : 0., 'my' : 0., 'mr' : 0.}
		pred = []
		step = 0
		tmpPred = []
		
		for row in reader :
			if team == row[2] or team == row[3] :
				tmp = ['',0,False,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.]
				tmp[0] = team
				tmp[1] = row[0]
				tmp[2] = True if team == row[2] else False
				if step == 0 :
					step = step + 1
					pred = row
				else :
					if team == pred[2] :
						tmp[2] = True
						tmp[3] = moy(tmpPred[3],step,pred[4])
						tmp[4] = moy(tmpPred[4],step,pred[5])
						tmp[5] = moy(tmpPred[5],step,pred[6])
						tmp[6] = moy(tmpPred[6],step,pred[7])
						tmp[7] = moy(tmpPred[7],step,pred[8])
						tmp[8] = moy(tmpPred[8],step,pred[9])
						tmp[9] = moy(tmpPred[9],step,pred[10])
						tmp[10] = moy(tmpPred[10],step,pred[11])
						tmp[11] = moy(tmpPred[11],step,pred[12])
						tmp[12] = moy(tmpPred[12],step,pred[13])
						tmp[13] = moy(tmpPred[13],step,pred[14])
						tmp[14] = moy(tmpPred[14],step,pred[15])
						tmp[15] = moy(tmpPred[15],step,pred[16])
						tmp[16] = moy(tmpPred[16],step,pred[18])
					if team == pred[3] :
						tmp[2] = False
						tmp[3] = moy(tmpPred[3],step,pred[5])
						tmp[4] = moy(tmpPred[4],step,pred[4])
						tmp[5] = moy(tmpPred[5],step,pred[7])
						tmp[6] = moy(tmpPred[6],step,pred[6])
						tmp[7] = moy(tmpPred[7],step,pred[9])
						tmp[8] = moy(tmpPred[8],step,pred[8])
						tmp[9] = moy(tmpPred[9],step,pred[11])
						tmp[10] = moy(tmpPred[10],step,pred[10])
						tmp[11] = moy(tmpPred[11],step,pred[13])
						tmp[12] = moy(tmpPred[12],step,pred[12])
						tmp[13] = moy(tmpPred[13],step,pred[15])
						tmp[14] = moy(tmpPred[14],step,pred[14])
						tmp[15] = moy(tmpPred[15],step,pred[17])
						tmp[16] = moy(tmpPred[16],step,pred[19])
				step = step + 1
				pred = row
				L.append(tmp)
				tmpPred = tmp
		dico[team] = L
print dico

 

 
"""myfile = open('csv-test.csv', 'w')
mywriter = csv.writer(myfile, delimiter=',', dialect='excel', lineterminator='\n')
 
for MatchSet in dico.values():
        for match in MatchSet: #on parcours chaque match
                matchTmp = match[3:]
                indiceMatch = match[1]
                matchTmp.insert(0,indiceMatch)
                mywriter.writerow(matchTmp)
 
myfile.close()"""


myfile = open('csv-test2.csv', 'w')
mywriter = csv.writer(myfile, delimiter=',', dialect='excel', lineterminator='\n')
ListFinalMatch = [] #Liste qui contiendra les matchs (c.a.d les lignes du CSV) 
positionCurseurCSV = 0 #position du curseur dans le futur CSV
posIDMatch = {} #clé = ID du match / valeur = position de cet ID dans ListFinalMatch

for MatchSet in dico.values():
	for match in MatchSet: #on parcours chaque match
		matchTMP = match[3:]
		indiceMatch = match[1]
		if indiceMatch not in posIDMatch.keys(): #si l'id du match n'a jamais été rencontré auparavant
			posIDMatch[indiceMatch] = positionCurseurCSV
			matchTMP.insert(0,indiceMatch)
			ListFinalMatch.append(matchTMP)
			positionCurseurCSV = positionCurseurCSV + 1
		else : #le match existe déja => cas d'une équipe extérieure
			positionMatch = posIDMatch[indiceMatch]
			ListFinalMatch[positionMatch].extend(matchTMP) #on ajoute les stats de l'équipe extérieure à la suite de celles à domicile
mywriter.writerows(ListFinalMatch)
myfile.close()			
