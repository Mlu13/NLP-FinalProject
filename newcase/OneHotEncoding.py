from numpy import argmax
from numpy import array
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.cluster import KMeans
import glob
import os, sys
import numpy as np
from sklearn.cluster import KMeans

#
from pymetamap import MetaMap
#

mm = MetaMap.get_instance('/Users/Maggie/Documents/NlpProject/public_mm/bin/metamap18')

path = "/Users/Maggie/Documents/NlpProject/pymetamap-master/pymetamap/newcase/trimtxt"

filename = []
sents = []

# #
doc_set = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.txt'):
            # print(file)
            filename.append(file)
eachFileCui = []
cuiNameTuple = []
cuilist = []
tmp = []

for filename in glob.glob(os.path.join(path, '*.txt')):
    # print(filename)

    f = open(filename,"r")
    content = f.read()
    sents.append(content)
    concepts, error = mm.extract_concepts(sents, [0, len(sents)])

    for concept in concepts:
        # print(concept)
        if concept[5] == '[dsyn]':

            tuple = (concept[4].lower(),concept[3])
            cuiNameTuple.append(tuple)
            tmp.append(concept[4])

    eachFileCui.append(tmp)
    tmp = []
    sents = []



for elem in eachFileCui:
    for item in elem:
        # if item not in cuilist:
        cuilist.append(item)
# #
print("  CuiName Tuple         ")
print(cuiNameTuple)
print("      ")
print(" eachFileCui    ")
print(eachFileCui)
#
print("      ")
print("  cuilist      ")
print(cuilist)
for elem in eachFileCui:
        if len(elem) == 0:
                eachFileCui.remove(elem)
# define example
data = cuilist
data1 = eachFileCui
#
# data1 = [['C0406656', 'C1956415', 'C0406636', 'C0406636'], ['C0406898', 'C0009450', 'C0406898', 'C4552766', 'C0406898', 'C1384666'],
# ['C0149871', 'C0038454', 'C0011884', 'C0038454', 'C0242339', 'C0038454', 'C0406898', 'C0038454', 'C0270724']]
#
# data = ['C0406656', 'C1956415', 'C0406636', 'C0028754', 'C0406898', 'C0009450', 'C0020538', 'C4552766', 'C0406636', 'C1384666',
# 'C0149871', 'C0038454', 'C0011884', 'C3250443', 'C0242339', 'C0406636', 'C0406898', 'C2930619', 'C0270724']

#row = number of document, column of unique cui

uniqlist = []

for elem in data:
    if elem not in uniqlist:
        uniqlist.append(elem)
print("uniq cui list")
print(uniqlist)
print('')

# manage features

values = array(uniqlist)

label_encoder = LabelEncoder()
integer_encoded = label_encoder.fit_transform(values)
print('uniq cui converted ')
print(integer_encoded)
print('')
#cui not uniq in coded

intNotUniq = label_encoder.fit_transform(array(data))
print("all cui in converted code")
print(intNotUniq)
print("")


#tuple to keep trakc of code & cui
tuplelist = []

for i in range(len(uniqlist)):
    t = (uniqlist[i], integer_encoded[i])
    tuplelist.append(t)

print("tuple to keep track of code & cui")
print(tuplelist)
print("       ")
# for elem in tuplelist:
#     if elem[0] == 'C0406898':
#         print(elem[1])
#

# # create N * M matrix
N = len(uniqlist) # number of document
M = len(data1) # number of unique cui
x = np.zeros((M,N)) # create matrix
print("initialize matrix")
print(x)
print("")


#dictlist to count appearance of each cui in the file
dict = {}
dictlist = []
for lst in data1:
    for word in lst:
        if word not in dict:
            dict[word] = 1
        elif word in dict:
            dict[word] += 1
    dictlist.append(dict)
    dict = {}
print("dictlist to count appearance of each cui in the file")
print(dictlist)
print("")


# converted cui in dictlist into uniq int code
dictInCodeInt = []
list1 = []


for lst in dictlist:

    for item in lst.items():

        for j in range(len(tuplelist)):
            if item[0] == tuplelist[j][0]:

                result = tuplelist[j][1],item[1]
                list1.append(result)
print("converted cui in dictlist into uniq int code")
print(list1)
print("")


# sublist = [[(9, 1), (12, 1), (8, 2)],
#            [(10, 3), (0, 1), (15, 1), (11, 1)],
#            [(5, 1), (4, 4), (1, 1), (6, 1), (10, 1), (7, 1)]]
#
#len of each file:
lenlist = []
tmp = []
for elem in eachFileCui:
    tmp = len(elem)
    lenlist.append(tmp)
print("len of each file")
print(lenlist)
print("")


# sublist the cui in dictlist based on the number of each file
finallist = []
tmplist = []

i = 0
s = 0
e = lenlist[0]
# print(len(lenlist))

while i < len(lenlist):
    # print(s,e)
    tmplist = list1[s:e]
    finallist.append(tmplist)
    # print(tmplist)

    s = e
    i += 1
    try:
        if e <= len(list1):
            e = e + lenlist[i]
    except:
        break
print("sublist the cui in dictlist based on the number of each file")
print(finallist)
print("")

# fill matrix
for i in range(len(finallist)):
    for j in range(len(finallist[i])):
        # print(sublist[i][j])
        index = finallist[i][j][0]
        # print(index)
        if index == 0 or index == 1:
            index = index
        else:
            index = index - 1
        # print(index)
        value = finallist[i][j][1]
        # print(index)
        # print(x[i][index])
        x[i][index] = value

print("filled matrix")
print(x)


# unique(integer_encoded)
# give each cui a interger code

# binary encode
# onehot_encoder = OneHotEncoder(sparse=False)
# integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
# onehot_encoded = onehot_encoder.fit_transform(integer_encoded)

# print(onehot_encoded[1:30])
# invert first example
# inverted = label_encoder.inverse_transform([argmax(onehot_encoded[10:, :])])
# print(inverted)
num = len(eachFileCui)
model = KMeans(n_clusters = num, random_state=0).fit(x)
result = model.labels_
print(result)








