# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:19:15 2020

@author: rusta
"""


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


