# -------------------------------------------------------------------------
# AUTHOR: Ahmad Alkadi
# FILENAME: similarity
# SPECIFICATION: the following code finds the cosine similarity between the documents that were given.
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: around 30 min
# -----------------------------------------------------------*/

# Importing some Python libraries
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Defining the documents
doc1 = "soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"

# Use the following words as terms to create your document-term matrix
# [soccer, favorite, sport, like, one, support, olympic, games]
# --> Add your Python code here
docs = [doc1, doc2, doc3, doc4]
terms = ["soccer", "favorite", "sport", "like", "one", "support", "olympic", "games"]
document_term_matrix = np.zeros((len(docs), len(terms)))
for i, doc in enumerate(docs):
    for j, term in enumerate(terms):
        document_term_matrix[i, j] = doc.split().count(term)

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors only
# Use cosine_similarity([X, Y, Z]) to calculate the pairwise similarities between multiple vectors
# --> Add your Python code here
# Calculate all the similarities
similarities = cosine_similarity(document_term_matrix)

function1 = (np.array([document_term_matrix[0]]))
function2 = (np.array([document_term_matrix[1]]))
function3 = (np.array([document_term_matrix[2]]))
function4 = (np.array([document_term_matrix[3]]))
# calculate the similarities between 2 vectors only
cos_sim_XY = cosine_similarity(function1, function2)
check = ["docs1","docs2"]
similarity = cos_sim_XY
cos_sim_XZ = cosine_similarity(function1, function3)
if(similarity < cos_sim_XY):
    check = ["docs1","docs3"]
    similarity = cos_sim_XZ 
cos_sim_XW = cosine_similarity(function1, function4)
if(similarity < cos_sim_XW):
    check = ["docs1","docs4"]
    similarity = cos_sim_XW  
cos_sim_YZ = cosine_similarity(function2, function3)
if(similarity < cos_sim_YZ):
    check = ["docs2","docs3"]
    similarity = cos_sim_YZ
cos_sim_YW = cosine_similarity(function2, function4)
if(similarity < cos_sim_YW):
    check = ["docs2","docs4"]
    similarity = cos_sim_YW 
cos_sim_ZW = cosine_similarity(function3, function4)
if(similarity < cos_sim_ZW):
    check = ["docs3","docs4"]
    similarity = cos_sim_ZW
    
# calculate the pairwise similarities between multiple vectors
function5 = np.vstack([function1, function2, function3])
function6 = np.vstack([function2, function3, function4])
function7 = np.vstack([function1, function3, function4])
function8 = np.vstack([function1, function2, function4])
cos_sim_XYZ = cosine_similarity(function5)
cos_sim_YZW = cosine_similarity(function6)
cos_sim_XWZ = cosine_similarity(function7)
cos_sim_XYW = cosine_similarity(function8)

# Print the highest cosine similarity following the information below
# The most similar documents are: doc1 and doc2 with cosine similarity = x
# --> Add your Python code here
print(f"The most similar documents are: {check[0]} and {check[1]} with cosine similarity = {similarity}")