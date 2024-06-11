import pandas as pd
import numpy as np
import openpyxl
from scipy.cluster.vq import kmeans,vq, whiten
def read_File():
    # Read the Excel file
    data = pd.read_excel('cars.xlsx')
    # Print the original data
    print("Original Data:\n", data, "\n\n")
    # Select numerical columns for clustering (assumption: all columns are numerical)
    numerical_data = data.select_dtypes(include=[np.number])
    # Check if there are numerical columns
    if numerical_data.empty:
        print("No numerical data found for clustering.")
        return
    # Normalize the data
    whitened_data = whiten(numerical_data)

    # Perform k-means clustering
    centroid, _ = kmeans(whitened_data, 3)
    idx, _ = vq(whitened_data, centroid)

    # Print the clustering result
    print("Cluster Indexes:\n", idx)



read_File()