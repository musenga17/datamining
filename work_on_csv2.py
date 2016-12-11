# coding: utf-8

import csv

def moy(val,step,newval) :
	return (val*step + float(newval))/(step+1)

teams = []
dico = {}

fichiers = ['2007:2008','2008:2009','2009:2010','2010:2011','2011:2012','2012:2013','2013:2014','2014:2015','2015:2016','2016:2017']

for nomFichierInput in fichiers :
        csvfile = open('SaisonsValidesFinales/'+nomFichierInput+'_final.csv')
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader :
		homeTeam = row[3]
		awayTeam = row[4]
		if homeTeam not in teams :
			teams.append(homeTeam)
		if awayTeam not in teams :
			teams.append(awayTeam)
                        
        for team in teams :
                csvfile = open('SaisonsValidesFinales/'+nomFichierInput+'_final.csv')
		reader = csv.reader(csvfile,delimiter=',')
		L = []
		stat = {'team: ' : '' , 'match' : 0, 'journee' : 0, 'home' : True , 'diffBut' : 0, 'mtc' : 0., 'mrt' : 0., 'mCor' : 0., 'mcrDom' : 0.}
		pred = []
		step = 0
		tmpPred = []
	        nVic, nDef, nNul, nPts = 0,0,0,0
		for row in reader :
			if team == row[3] or team == row[4] :
				tmp = ['',0,0,False,0,0.,0.,0.,0.,0,0,0,0]
				tmp[0] = team
				tmp[1] = row[0]
                                tmp[2] = row[1]
				tmp[3] = True if team == row[3] else False
				if step == 0 :
					step = step + 1
					pred = row
				else :
					if team == pred[3] : # si l'equipe est celle qui joue à domicile
						tmp[3] = True
						tmp[4] = tmpPred[4] + int(pred[5])
						tmp[5] = moy(tmpPred[5],step,pred[7])
						tmp[6] = moy(tmpPred[6],step,pred[9])
						tmp[7] = moy(tmpPred[7],step,pred[11])
						tmp[8] = moy(tmpPred[8],step,pred[13])
                                                resMatch = pred[15]
                                                if resMatch == 'H' :
                                                        nVic = nVic + 1
                                                        nPts = nPts + 3
                                                elif resMatch == 'A' :
                                                        nDef = nDef + 1
                                                else :
                                                        nNul = nNul + 1
                                                        nPts = nPts + 1
					if team == pred[4] : # si l'equipe est celle qui joue à l'extérieur
						tmp[3] = False
						tmp[4] = tmpPred[4] + int(pred[6])
						tmp[5] = moy(tmpPred[5],step,pred[8])
						tmp[6] = moy(tmpPred[6],step,pred[10])
						tmp[7] = moy(tmpPred[7],step,pred[12])
						tmp[8] = moy(tmpPred[8],step,pred[14])
                                                resultMatch = pred[15]
                                                if resultMatch == 'A' :
                                                        nVic = nVic + 1
                                                        nPts = nPts + 3
                                                elif resultMatch == 'H' :
                                                        nDef = nDef + 1
                                                else :
                                                        nNul = nNul + 1
                                                        nPts = nPts + 1
                                        tmp[9] = nVic
                                        tmp[10] = nDef
                                        tmp[11] = nNul
                                        tmp[12] = nPts
				step = step + 1
				pred = row
				L.append(tmp)
				tmpPred = tmp
		dico[team] = L


        myfile = open('SaisonsStatsFinales/'+nomFichierInput+'_Stats_final.csv', 'w')
        mywriter = csv.writer(myfile, delimiter=',', dialect='excel', lineterminator='\n')
        ListFinalMatch = [] #Liste qui contiendra les matchs (c.a.d les lignes du CSV) 
        positionCurseurCSV = 0 #position du curseur dans le futur CSV
        posIDMatch = {} #clé = ID du match / valeur = position de cet ID dans ListFinalMatch

        for MatchSet in dico.values():
	        for match in MatchSet: #on parcours chaque match
		        matchTMP = match[4:]
		        indiceMatch = match[1]
                        indiceJournee = match[2]
		        if indiceMatch not in posIDMatch.keys(): #si l'id du match n'a jamais été rencontré auparavant
			        posIDMatch[indiceMatch] = positionCurseurCSV
			        matchTMP.insert(0,indiceMatch)
                                matchTMP.insert(1,indiceJournee)
			        ListFinalMatch.append(matchTMP)
			        positionCurseurCSV = positionCurseurCSV + 1
		        else : #le match existe déja => cas d'une équipe extérieure
			        positionMatch = posIDMatch[indiceMatch]
			        ListFinalMatch[positionMatch].extend(matchTMP) #on ajoute les stats de l'équipe extérieure à la suite de celles à domicile
        mywriter.writerows(ListFinalMatch)
        myfile.close()	
	
