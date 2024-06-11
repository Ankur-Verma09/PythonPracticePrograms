import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import value_counts


def barOnCustomerChurn():
    customer = pd.read_csv('customer_churn.csv')
    # print(customer.head())
    # print(customer['Churn'].value_counts())
    # print(customer['InternetService'].value_counts())
    # print(customer['InternetService'].value_counts().keys())
    plt.barh(customer['InternetService'].value_counts().keys().tolist(), customer['InternetService'].value_counts().tolist())
    plt.title('Customer Churns Details')
    plt.ylabel('Count of Categories')
    plt.xlabel('Category of Internt Service')
    plt.show()


def scatterOnCustomerChurn():
    customer = pd.read_csv('customer_churn.csv')
    # print(customer.head())
    # print(customer['Churn'].value_counts())
    # print(customer['InternetService'].value_counts())
    # print(customer['InternetService'].value_counts().keys())
    plt.scatter(customer['InternetService'].value_counts().keys().tolist(), customer['InternetService'].value_counts().tolist())
    plt.title('Customer Churns Details')
    plt.ylabel('Count')
    plt.xlabel('Churn Name')
    plt.show()

def stackOnCustomerChurn():
    customer = pd.read_csv('customer_churn.csv')
    # print(customer.head())
    # print(customer['Churn'].value_counts())
    # print(customer['InternetService'].value_counts())
    # print(customer['InternetService'].value_counts().keys())
    plt.stackplot(customer['InternetService'].value_counts().keys().tolist(), customer['InternetService'].value_counts().tolist())
    plt.title('Customer Churns Details')
    plt.ylabel('Count of Categories')
    plt.xlabel('Category of Internt Service')
    plt.show()

def histogramOnCustomerChurn():
    customer = pd.read_csv('customer_churn.csv')
    plt.hist(customer['tenure'], bins=80)
    plt.title('Distrubition of tenure')
    plt.ylabel('Count of Categories')
    plt.xlabel('Category of Internt Service')
    plt.show()



histogramOnCustomerChurn()
# stackOnCustomerChurn()
# violinOnCustomerChurn()
# scatterOnCustomerChurn()
# barOnCustomerChurn()