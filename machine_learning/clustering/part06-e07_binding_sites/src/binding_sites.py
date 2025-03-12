#!/usr/bin/env python3

# Exercise 6.7 (binding sites)
# This exercise can give three points at maximum!

# A binding site is a piece of DNA where a certain protein prefers to bind. The piece of DNA can be described as a string consisting of letters A, C, G, and T, which correspond to nucleotides Adenine, Cytosine, Guanine, and Thymine. In this exercise the length of binding sites is eight nucleotides. They are stored in the file data.seq, and the binding sites there are classified into two classes.

# Part 1. Write function toint that converts a nucleotide to an integer. Use the following mapping:


# A -> 0
# C -> 1
# G -> 2
# T -> 3
# ﻿
# Write also function get_features_and_labels that gets a filename as a parameter. The function should load the contents of the file into a DataFrame. The column X contains a string. Convert this column into a feature matrix using the above toint function. For example the column ["GGATAATA","CGATAACC"] should result to the feature matrix


# [[2,2,0,3,0,0,3,0],
# [1,2,0,3,0,0,1,1]]
# ﻿
# The function should return a pair, whose first element is the feature matrix and the second element is the label vector.

# Part 2. Create function cluster_euclidean that gets a filename as parameter. Get the features and labels using the function from part 1. Perform hierarchical clustering using the function sklearn.cluster.AgglomerativeClustering. Get two clusters using average linkage and euclidean metric. Fit the model and predict the labels. Note that you may have to use the find_permutation function again, because even though the clusters are correct, they may be labeled differently than the real labels given in data.seq. The function should return the accuracy score.

# Part 3. Create function cluster_hamming that works like the function in part 2, except now using the hamming metric. Even though it is possible to pass the function hamming to AgglomerativeClustering, let us now compute the Hamming distance matrix explicitly. We can achieve this using the function sklearn.metrics.pairwise_distances. Use the metric parameter precomputed to AgglomerativeClustering. And give the distance matrix you got from pairwise_distances, instead of the feature matrix, to the fit_predict method of the model. If you want, you can visualize the clustering using the provided plot function.

# NB! When submitting your solution, please comment away all plot function calls. This might cause tests to fail on the server.

# Which metric (or distance) do you think is theoretically more correct of these two (Euclidean or Hamming)? Why?

#%%

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import scipy
import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation

def toint(x):
    nucleotide_map = {
        "A": 0,
        "C": 1,
        "G": 2,
        "T": 3
    }
    
    result = []
    for seq in x:
        result.append([nucleotide_map[char] for char in seq])

    return np.array(result)


def get_features_and_labels(filename):

    df = pd.read_csv(filename, sep='\t')
    
    X = df.loc[:, "X"].values
    y = df.loc[:, "y"].values

    X = toint(X)

    return (X, y)

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} metric")
    plt.show()

def cluster_euclidean(filename):

    X, y = get_features_and_labels(filename)

    model = AgglomerativeClustering(n_clusters=2, metric="euclidean", linkage="average")
    model.fit_predict(X)

    permutation = find_permutation(2, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    acc = accuracy_score(y, new_labels)

    return acc

def cluster_hamming(filename):

    X, y = get_features_and_labels(filename)

    model = AgglomerativeClustering(n_clusters=2, metric="precomputed", linkage="average")
    hamming_distances = pairwise_distances(X, metric='hamming')
    model.fit_predict(hamming_distances)

    permutation = find_permutation(2, y, model.labels_)
    new_labels = [permutation[label] for label in model.labels_]
    acc = accuracy_score(y, new_labels)

    return acc


def main():
    print("Accuracy score with Euclidean metric is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming metric is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
