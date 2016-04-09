from os import listdir, getcwd
from os.path import isfile, join, abspath
from nltk.corpus import stopwords
from itertools import combinations
from nltk.stem.porter import *
from nltk.stem.snowball import SnowballStemmer

path='/corpus'
mypath=abspath(join(getcwd(), path))


def getFileNames(mypath):
    return [(abspath(join(mypath,f)),f) for f in listdir(mypath) if isfile(join(mypath, f)) and f[-1]!='~']

def readFile(name):
    with open(name, 'r') as f:
        return unicode(f.read(), "utf-8")

def normalize(mypath):
    corpus={}
    corpus1={}
    corpus2={}
    corpus3={}
    corpus4={}
    corpus5={}
    for item in getFileNames(mypath):
        f=readFile(item[0]).split()
        stop = stopwords.words('english')
        stemmer = PorterStemmer()
        stemmer2 = SnowballStemmer("english")
        corpus[item[1]]=f
        corpus['desc']="Unfiltered direct corpus."
        corpus1[item[1]] = [stemmer2.stem(stemmer.stem(w)) for w in f]
        corpus1['desc']="Stopwords not removed and but stemmed first with Porter stemmer and then Snowball stemmer."
        corpus2[item[1]] = [w for w in f if w.lower() not in stop]
        corpus2['desc']="Stemming not done. But stopwords removed with nltk stopword list."
        corpus3[item[1]] = [stemmer2.stem(stemmer.stem(w)) for w in f if w.lower() not in stop]
        corpus3['desc']= "Stopwords removed and then both stemmers used."
        corpus4[item[1]] = [corpus3[item[1]][i]+" "+corpus3[item[1]][i+1] for i in range(len(corpus3[item[1]])-1)]
        corpus4['desc'] = "Stopwords removed and stemmed and then bigrams taken."
        corpus5[item[1]] = [corpus3[item[1]][i]+" "+corpus3[item[1]][i+1]+" " + corpus3[item[1]][i+2] for i in range(len(corpus3[item[1]])-2)]
        corpus5['desc'] = "Stopwords removed and stemmed and then trigrams taken."
        #print item, float(len(corpus[item]))/len(f)
    return [corpus, corpus1, corpus2, corpus3, corpus4, corpus5]
    
def test():
    corpus = normalize(mypath)
    for item1, item2 in combinations(corpus.keys(),2):
        set1 = set(corpus[item1])
        set2 = set(corpus[item2])
        print item1, item2, float(len(set1 & set2))/len(set1|set2)
if __name__=='__main__':
    corpus=normalize(mypath)
    print corpus[0]
