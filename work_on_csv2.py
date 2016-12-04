# coding: utf-8

import csv

def moy(val,step,newval) :
	return (val*step + float(newval))/(step+1)

teams = []
dico = {}

fichiers = ['2007:2008','2008:2009','2009:2010','2010:2011','2011:2012','2012:2013','2013:2014','2014:2015','2015:2016','2016:2017']

for nomFichierInput in fichiers :
        csvfile = open('SaisonsValides/'+nomFichierInput+'.csv')
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader :
		homeTeam = row[3]
		awayTeam = row[4]
		if homeTeam not in teams :
			teams.append(homeTeam)
		if awayTeam not in teams :
			teams.append(awayTeam)
                        
        for team in teams :
                csvfile = open('SaisonsValides/'+nomFichierInput+'.csv')
		reader = csv.reader(csvfile,delimiter=',')
		L = []
		#mBmf : moyenne buts marques fin match #mBef : ------- ---- encaisses --- ----- #mBmh : moyenne buts marques mi temps #mBeh : ------- ---- encaisses -- ----- #ms : moyenne shoot #msc : moyenne shoot conscedes #mst : moyenne shoot target #mstc : moyenne shoot target conscedes #mfc : moyenne fautes commises #mfo : moyenne fautes obtenues #mc : moyenne corners #mcc : moyenne corners conscedes #my : moyenne cartons jaunes #mr : moyenne cartons rouges
		stat = {'team: ' : '' , 'match' : 0, 'journee' : 0, 'home' : True , 'mBmf' : 0., 'mBef' : 0., 'mBmh' : 0., 'mBeh' : 0., 'ms' : 0., 'msc' : 0., 'mst' : 0., 'mstc' : 0., 'mfc' : 0., 'mfo' : 0., 'mc' : 0., 'mcc' : 0., 'my' : 0., 'mr' : 0.}
		pred = []
		step = 0
		tmpPred = []
		nbPoints, nVDom, nVExt, nDDom, nDExt, nNDom, nNExt, nVCons, nDCons, nNCons, nVDomCons, nVExtCons, nDDomCons, nDExtCons, nNDomCons, nNExtCons = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
		for row in reader :
			if team == row[3] or team == row[4] :
				tmp = ['',0,0,False,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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
						tmp[16] = moy(tmpPred[16],step,pred[17])
						tmp[17] = moy(tmpPred[17],step,pred[19])
                                                if pred[21] == 'H' :
                                                        nbPoints = nbPoints + 3
                                                        nVDom = nVDom + 1
                                                        nVCons = nVCons + 1
                                                        nDCons = 0
                                                        nNCons = 0
                                                        nVDomCons = nVDomCons + 1
                                                        nDDomCons = 0
                                                        nNDomCons = 0
                                                if pred[21] == 'A' :
                                                        nDDom = nDDom + 1
                                                        nVCons = 0
                                                        nDCons = nDCons + 1
                                                        nNCons = 0
                                                        nVDomCons = 0
                                                        nDDomCons = nDDomCons + 1
                                                        nNDomCons = 0
                                                if pred[21] == 'D' :
                                                        nNDom = nNDom + 1
                                                        nNCons = nNCons + 1
                                                        nVDomCons = 0
                                                        nDDomCons = 0
                                                        nNDomCons = nNDomCons + 1
					if team == pred[4] : # si l'equipe est celle qui joue à l'extérieur
						tmp[3] = False
						tmp[4] = moy(tmpPred[4],step,pred[6])
						tmp[5] = moy(tmpPred[5],step,pred[5])
						tmp[6] = moy(tmpPred[6],step,pred[8])
						tmp[7] = moy(tmpPred[7],step,pred[7])
						tmp[8] = moy(tmpPred[8],step,pred[10])
						tmp[9] = moy(tmpPred[9],step,pred[9])
						tmp[10] = moy(tmpPred[10],step,pred[12])
						tmp[11] = moy(tmpPred[11],step,pred[11])
						tmp[12] = moy(tmpPred[12],step,pred[14])
						tmp[13] = moy(tmpPred[13],step,pred[13])
						tmp[14] = moy(tmpPred[14],step,pred[16])
						tmp[15] = moy(tmpPred[15],step,pred[15])
						tmp[16] = moy(tmpPred[16],step,pred[18])
						tmp[17] = moy(tmpPred[17],step,pred[20])
                                                if pred[21] == 'A' :
                                                        nbPoints = nbPoints + 3
                                                        nVExt = nVExt + 1
                                                        nVCons = nVCons + 1
                                                        nDCons = 0
                                                        nNCons = 0
                                                        nVExtCons = nVExtCons + 1
                                                        nDExtCons = 0
                                                        nNExtCons = 0
                                                if pred[21] == 'H' :
                                                        nDExt = nDExt + 1
                                                        nVCons = 0
                                                        nDCons = nDCons + 1
                                                        nNCons = 0
                                                        nVExtCons = 0
                                                        nDExtCons = nDExtCons + 1
                                                        nNExtCons = 0
                                                if pred[21] == 'D' :
                                                        nNExt = nNExt + 1
                                                        nNCons = nNCons + 1
                                                        nVExtCons = 0
                                                        nDExtCons = 0
                                                        nNExtCons = nNExtCons + 1
                                        if pred[21] == 'D' :
                                                nbPoints = nbPoints + 1
                                        tmp[18] = nbPoints
                                        tmp[19] = nVDom
                                        tmp[20] = nVExt
                                        tmp[21] = nDDom
                                        tmp[22] = nDExt
                                        tmp[23] = nNDom
                                        tmp[24] = nNExt
                                        tmp[25] = nVCons
                                        tmp[26] = nDCons
                                        tmp[27] = nNCons
                                        tmp[28] = nVDomCons
                                        tmp[29] = nVExtCons
                                        tmp[30] = nDDomCons
                                        tmp[31] = nDExtCons
                                        tmp[32] = nNDomCons
                                        tmp[33] = nNExtCons
				step = step + 1
				pred = row
				L.append(tmp)
				tmpPred = tmp
		dico[team] = L


        myfile = open('saisonsStatsCSV/'+nomFichierInput+'_Stats.csv', 'w')
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
	
