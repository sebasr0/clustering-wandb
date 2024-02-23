import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import wandb
import argparse
from sklearn.cluster import KMeans
from sklearn import datasets, metrics

parser = argparse.ArgumentParser()
parser.add_argument('--IdExecution', type=str, help='ID of the execution')
args = parser.parse_args()

def load_and_train():
    #initialize wandb
    with wandb.init(
        project="clustering-wandb",
        name=f"Load iris data and train Kmeans ExecId-{args.IdExecution}", job_type="load-train") as run:
            
        # Load data
        iris = datasets.load_iris()
        X, y = iris.data, iris.target
        names = iris.target_names

        def get_label_ids(classes):
            return np.array([names[aclass] for aclass in classes])
        labels = get_label_ids(y)

        # Train model
        kmeans = KMeans(n_clusters=4, random_state=1)
        cluster_labels = kmeans.fit_predict(X)
        
        # Log the model parameters
        wandb.config.update(kmeans.get_params())
        
        # plots
        #wandb.sklearn.plot_elbow_curve(kmeans, X) #elow plot
        #wandb.sklearn.plot_silhouette(kmeans, X, labels) #Silhouette plot
        wandb.sklearn.plot_clusterer(kmeans, X, cluster_labels, labels, 'KMeans')
        
        
#execute second exec
load_and_train()