from bs4 import BeautifulSoup
from urllib import urlencode
from urllib2 import urlopen
from urllib2 import Request
import re
import csv
import unicodedata

def delete_blanks(s) :
    return s.replace('\n','').lstrip(' ').rstrip(' ')

j=3
#for j in range(1,38) :
url = 'http://www.lfp.fr/ligue1/competitionPluginCalendrierResultat/changeCalendrierJournee?sai=77&jour='+str(j)
f = urlopen(url)

soup = BeautifulSoup(f)

season = open('season.csv','w')
writer = csv.writer(season,delimiter=',',dialect='excel',lineterminator='\n')

for item in soup.find_all('tr') :
    row = []
    dom = item.find('td',{'class':'domicile'})
    ext = item.find('td',{'class':'exterieur'})
    score = item.find('td',{'class':'stats'})
    if dom is not None and ext is not None:
        row.append(j)
        d = delete_blanks(dom.getText())
        row.append(unicodedata.normalize('NFKD', d).encode('ascii', 'ignore'))
        e = delete_blanks(ext.getText())
        row.append(unicodedata.normalize('NFKD', e).encode('ascii', 'ignore'))
        s = delete_blanks(score.getText())
        #ss = s.replace(' ','')
        tab = s.split('-')
        row.append(tab[0])
        row.append(tab[1])
        adressStat = 'http://www.lfp.fr'+score.find({'a'}).get('href')
        ff = urlopen(adressStat)
        sousoup = BeautifulSoup(ff)
        details = sousoup.find_all('div',{'class':'details'})
        bloc_stat = details.find_all('div',{'id','bloc_statistiques'})
        table = bloc_stat.find_all('table')
        tbody = table.find_all('tr')
        for tr in tbody :
            print tr
            for statDom in tr.find_all('td',{'class':'dom'}) :
                st = statDom.find('div',{'class':'chiffre_stats'})
                row.append(delete_blanks(st.getText()))
            for statExt in tr.find_all('td',{'class':'ext'}) :
                st = statDom.find('div',{'class':'chiffre_stats'})
                row.append(delete_blanks(st.getText()))

        writer.writerow(row)
