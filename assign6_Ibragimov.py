# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:19:15 2020

@author: rusta
"""
#Question 1, Assignment 6

import csv

dicti={}


with open("alexa reviews.csv", "r",encoding="cp1252") as f1:
    
    rec=csv.DictReader(f1)
    for i in rec:
        
        ran=float(i["rating"])
        nam=i["variation"]
        if nam not in dicti:
            dicti[nam]=[1,ran]
        else:
            dicti[nam][0]=dicti[nam][0]+1
            dicti[nam][1]=dicti[nam][1]+ran
            
with open("new10.csv","w",newline="") as f2:
    Y=csv.writer(f2)
    Y.writerow(["name","number","avrating"])
    for g in dicti:
        dicti[g][1]=float(round(dicti[g][1]/dicti[g][0],1))
        
        
        Y.writerow([g,dicti[g][0],dicti[g][1]])

#%%
      
#Question 2, Assignment 6

import csv

dic={}
toRemove=[".",",","?","!",":",";"]
with open("alexa reviews.csv", "r",encoding="cp1252") as f3:
    
    reviews=csv.DictReader(f3)
    
    for review in reviews:
        text=str(review["text"]).lower().replace("!","").replace("?","")
        sentences=text.split(".")
        for elem in sentences:
            sentence=str(elem)
            if "sound" in sentence:
                theword=sentence.split()    
                for check in theword:
                    if check[-1] in toRemove:
                        dd=check[0:len(check)-1]
                    else:
                        dd=check
                        if len(dd)>=4:
                            if dd not in dic:
                                dic[dd]=1
                            else:
                                dic[dd]=dic[dd]+1
                        
del dic["sound"]

sorte=sorted(dic,key=dic.__getitem__, reverse=True)
 
del sorte[10:]

with open("new11.csv","w",newline="") as V2:
    v=csv.writer(V2)
    v.writerow(["word","count"])
    for dd in sorte:
        if dd in dic:
            v.writerow([dd,dic[dd]]) 

#%%

# Tento kod uvadi pocet filmu z kazde filmove studie ktera je uvedena v souboru MovieGross.csv
# nasledne pak pocita kolik ty filmy vydelaly kazde z tech studii
#Vysledky zapsany do noveho csv souboru

import csv
NewDict2={}
with open('MovieGross.csv','r') as f_in:
    Rows = csv.DictReader(f_in)
    for row in Rows:
        studio=row['Studio']
        domestic=float(row['Domestic'])
        if studio not in NewDict2:
            NewDict2[studio]=[1,domestic]
        else:
            NewDict2[studio][0]=NewDict2[studio][0]+ 1
            NewDict2[studio][1]=NewDict2[studio][1]+domestic
with open('MovieGrossNew.csv','w') as f_out:   
    f_out.write('Studio, NumberMovies , Total, Domestic, Overseas\n')

    for studio in NewDict2:     
        f_out.write(studio+","+str(NewDict2[studio][0])+","+ str(NewDict2[studio][1])+"\n")
#%%

# Funkce pocita kolikrat slovo "love" objevuje ve nejakem stringu. 
def countmyword(string,word):    
    string=string.replace(".","").replace(",","").replace("?","").replace("!","")    
    words=string.split()    
    count=0    
    for x in words:        
        if x.lower()==word.lower():            
            count=count+1    
    return count       
sentences=["Lovely Day","I Love You","There is so much love.", "Love, love, love!"]
for x in sentences:
    print(x)
    print(countmyword(x,"love"))
            