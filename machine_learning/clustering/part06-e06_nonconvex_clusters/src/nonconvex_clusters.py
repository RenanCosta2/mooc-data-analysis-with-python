#!/usr/bin/env python3

# Exercise 6.6 (nonconvex clusters)
# This exercise can give four points at maximum!

# Read the tab separated file data.tsv from the src folder into a DataFrame. The dataset has two features X1 and X2, and the label y. Cluster the feature matrix using DBSCAN with different values for the eps parameter. Use values in np.arange(0.05, 0.2, 0.05) for clustering. For each clustering, collect the accuracy score, the number of clusters, and the number of outliers. Return these values in a DataFrame, where columns and column names are as in the below example.

# Note that DBSCAN uses label -1 to denote outliers , that is, those data points that didn't fit well in any cluster. You have to modify the find_permutation function to handle this: ignore the outlier data points from the accuracy score computation. In addition, if the number of clusters is not the same as the number of labels in the original data, set the accuracy score to NaN.


#      eps   Score  Clusters  Outliers                             
# 0    0.05      ?         ?         ?
# 1    0.10      ?         ?         ?
# 2    0.15      ?         ?         ?
# 3    0.20      ?         ?         ?
# ﻿
# Before submitting the solution, you can plot the data set (with clusters colored) to see what kind of data we are dealing with.

# Points are given for each correct column in the result DataFrame.

# %%
import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation

#%%

def nonconvex_clusters():

    #%%
    df = pd.read_csv("src/data.tsv", sep='\t')

    X = df.loc[:, ["X1", "X2"]]
    y = df.loc[:, "y"]

    #%%

    clustering = pd.DataFrame(columns=["eps", "Score", "Clusters", "Outliers"])
    clustering

    #%%
    eps_array = np.arange(0.05, 0.2, 0.05)
    
    for eps in eps_array:

        model_dbscan = DBSCAN(eps=eps)
        model_dbscan.fit(X)
        labels = model_dbscan.labels_

        clusters = len(set(labels)) - (1 if -1 in labels else 0)
        outliers = list(labels).count(-1)

        if clusters != 2:
            acc = np.nan
        else:
            
            valid_labels = labels != -1
            filtered_y = y[valid_labels]
            filtered_labels = labels[valid_labels]
            
            permutation = find_permutation(2, filtered_y, filtered_labels)
            new_labels = [permutation[label] for label in filtered_labels]
            acc = accuracy_score(filtered_y, new_labels)


        eps_row = pd.DataFrame([[eps, acc, clusters, outliers]], columns=["eps", "Score", "Clusters", "Outliers"])
        clustering = pd.concat([clustering, eps_row], ignore_index=True)

    #%%
    clustering = clustering.astype("float")
    clustering

    #%%

    return clustering

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
