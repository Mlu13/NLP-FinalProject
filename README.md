# NLP-FinalProject
Followed instruction and installed Metamap wrapper for python from https://github.com/smujjiga/pymm
Used clean.scala file to extract text from each file inside txtcopy folder and saved output into a folder called trimtext.
Under the folder pymetamap-maste — pymetamap, created a new Python project called newcase with two Python files, then should be able to run the two python files.  
The first approach that using full text and TF-IDF to do clustering does not always show meaningful result. Sometimes it shows more words related to medical term but sometimes the result shows more words that are not related to medical term or disease. 
The second approach that use One-Hot-Encoding, I manually created the matrix based on the number of file and the number of unique CUI and filled the matrix. However, when I apply the k-means, I had problem on setting the number of cluster and showing the result. I’ve looked through many resources online and still wasn’t sure how to solve the problem. 
