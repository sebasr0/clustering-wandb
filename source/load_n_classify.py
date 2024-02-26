import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import wandb
import argparse
import joblib
from sklearn.cluster import KMeans
from sklearn import datasets, metrics

parser = argparse.ArgumentParser()
parser.add_argument('--IdExecution', type=str, help='ID of the execution')
args = parser.parse_args()

#set the Kmeans Params
n_clusters = 4
random_state = 1

def load_and_classify():
    #initialize wandb
    with wandb.init(
        project="clustering-wandb",
        name=f"Load iris data and train Kmeans ExecId-{args.IdExecution}", job_type="load-train") as run:
            
        # Load data
        iris = datasets.load_iris()
        X, y = iris.data, iris.target
        names = iris.target_names

        # get labels gunction
        def get_label_ids(classes):
            return np.array([names[aclass] for aclass in classes])
        labels = get_label_ids(y)

        # Train model
        kmeans = KMeans(n_clusters, random_state=1)
        cluster_labels = kmeans.fit_predict(X)
        
        # plots
        #wandb.sklearn.plot_elbow_curve(kmeans, X) #elow plot
        #wandb.sklearn.plot_silhouette(kmeans, X, labels) #Silhouette plot
        wandb.sklearn.plot_clusterer(kmeans, X, cluster_labels, labels, 'KMeans') #All in one plot wandb function
        
        # Create a wandb Artifact for the model
        model_artifact = wandb.Artifact('kmeans-model', type='model', description='KMeans clustering model')

        # Add model parameters to the artifact
        model_params = kmeans.get_params()
        model_artifact.metadata['parameters'] = model_params

        # Save model to a file (temporarily, for artifact purposes)
        model_file = 'kmeans_model.pkl'
        joblib.dump(kmeans, model_file)
        
        # Add the model file to the artifact
        model_artifact.add_file(model_file)

        # Log the artifact to wandb
        run.log_artifact(model_artifact)
        
        # Log the model parameters
        wandb.config.update(kmeans.get_params())
        

#execute
load_and_classify()