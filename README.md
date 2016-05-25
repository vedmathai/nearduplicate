# Deduplication using simhash.


This "simplish" project demonstrates the concept of feature extraction and near duplicate (or similarity detection) utilizing simhashed scores. 

One seminal source that brings together everything is [Detecting
Near-Duplicates for Web Crawling](http://www.wwwconference.org/www2007/papers/paper215.pdf) by Manku et al.

This code includes another [project](https://github.com/leonsim/simhash) which implements the simhashing algorithm as described in the Manku paper. 


## Requirements
To use the code you'd need:
* [NLTK](http://www.nltk.org/) (Natural Langugage Toolkit) 
* Simhash from the above [project](https://github.com/leonsim/simhash).
* It's written in Python. For best results run it on Linux.

## To use
* Place the text files for similarity detection in the corpus directory. All of the files will be read and each one will be mapped against the other to show the similarity score.
* The file to run is **hashtest.py**.
* The result table will appear in **results.csv**. 
* To intepret the results: Values closer to 0 indicate higher similarity levels, and further from zero in the positive direction indicates differences. A value of 0 indicates an exact match

## Inferences (so far)
* Removing stopwords and stemming give better results of differences. 
* When trying to hash on the n-gram or shingles, the results become stricter and even small changes are given high differences.


