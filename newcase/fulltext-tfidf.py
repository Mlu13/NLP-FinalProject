from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from nltk.tokenize import RegexpTokenizer
import glob,os,re, nltk
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

# Reading each file from trimtxt
content = []
path = "/Users/Maggie/Documents/NlpProject/pymetamap-master/pymetamap/newcase/trimtxt"

count = 0
for filename in glob.glob(os.path.join(path, '*.txt')):
    # print(filename)
    count += 1
    f = open(filename,"r")
    result = f.read()
    content.append(result)

# Tokenizer, stopwords and stemmer.
tokenizer = RegexpTokenizer(r'\w+')
en_stop = get_stop_words('en')
en_stop.extend(["follow",'exercise','medication','tablet','increased','months','days','history','fasting','disease','results','will'])
p_stemmer = PorterStemmer()

texts = []
sents = []


# loop through document list
# clean and tokenize document string
for i in content:

    raw = i.lower()
    raw = re.sub('[0-9]+', '', raw)

    tokens = tokenizer.tokenize(raw)
    # print(tokens)
    newtokens = []
    for elem in tokens:
        if len(elem) > 4:
            if elem not in en_stop:
                newtokens.append(elem)

#remove number in the text
for elem in newtokens:
    elem = re.sub('[0-9]+', '', elem)
# print(newtokens)




# tag each word in the text
wordlist = []
pos_tagged = nltk.pos_tag(newtokens)
print("    ")


# loop through text with tagged, and filtered the text, keep type of NN, JJ, NNP, NNS, VBN
taglist = ['NN', 'JJ', 'NNP', 'NNS','VBN']
for elem in pos_tagged:
    # print(elem[1])
    if elem[1] in taglist:
        wordlist.append(elem[0])
#         print(elem)
print(wordlist)
#
print(len(newtokens))
print(len(wordlist))

# used built in function to convert text into number with TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(wordlist)

# use k-means for clustering
true_k = 5
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
