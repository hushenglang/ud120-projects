from nltk.corpus import stopwords
sw = stopwords.words("english")
print len(sw)

# import nltk

# nltk.download('all', halt_on_error=False)



from nltk.stem.snowball import SnowballStemmer
print SnowballStemmer.languages
stemmer = SnowballStemmer("english")
print stemmer.stem("unresponsive")
