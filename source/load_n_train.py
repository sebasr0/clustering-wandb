import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import wandb
import argparse
from sklearn.cluster import KMeans
from sklearn import datasets, cluster

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
        
#execute
load_and_train()