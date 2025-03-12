#!/usr/bin/env python3

# Exercise 6.5 (plant clustering)
# Using the same iris data set that you saw earlier in the classification, apply k-means clustering with 3 clusters. Create a function plant_clustering that loads the iris data set, clusters the data and returns the accuracy_score.

# %%
import scipy
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
#%%

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation
#%%
def plant_clustering():

    #%%
    X, y = load_iris(return_X_y=True)
    plt.scatter(X[:, 0], X[:, 1], c=y)

    #%%
    model = KMeans(n_clusters=3, random_state=0, n_init=10)
    model.fit(X)
    print("Clusters centers:\n", model.cluster_centers_)

    #%%
    plt.scatter(X[:, 0], X[:, 1], c=model.labels_)
    plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=100, color="red")
    plt.xlabel("X")
    plt.ylabel("Y")

    #%%
    permutation = find_permutation(3, y, model.labels_)
    permutation

    #%%
    new_labels = [permutation[label] for label in model.labels_]
    acc = accuracy_score(y, new_labels)

    #%%
    return acc

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
