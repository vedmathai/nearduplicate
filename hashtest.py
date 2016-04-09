import readFiles
from simhash import Simhash, SimhashIndex
import re
from itertools import combinations
import csv

path='./corpus'




def main(path):
    corpuses = readFiles.normalize(path)
    results=[]
    for corpus in corpuses:
        hashset={}
        listofitems=[]
        for item in corpus.keys():
            if item=='desc':continue
            z=Simhash(corpus[item])
            hashset[item]=z
            listofitems+=[(item,z)]
      
        l = SimhashIndex(listofitems)
        #print(l.get_near_dups(hashset['../corpus/bbc/tech1/001.txt']))
        hashlist={}
        for i, item1 in enumerate(hashset.keys()):
            hashlist[item1]=[]
            for j, item2 in enumerate(hashset.keys()):
                if j<i:
                    hashlist[item1]+=[' ']
                    continue
                hashlist[item1]+=[hashset[item1].distance(hashset[item2])]
                #print item1, item2, hashset[item1].distance(hashset[item2])
        results+=[[hashset, hashlist, corpus['desc']]]

    
    with open('results.csv','wb') as csvfile:
        writer=csv.writer(csvfile, delimiter=',',quotechar='{')
        for hashset, hashlist, desc in results:
            writer.writerow([" "])
            writer.writerow([i for i in desc.split()])
            record=[]
            record+=[[' ']+[key for key in hashset.keys()]]
            for k in hashset.keys():
                record+=[[k]+hashlist[k]]
            for item in record:
                writer.writerow(item)

if __name__=='__main__':
    main(path)
