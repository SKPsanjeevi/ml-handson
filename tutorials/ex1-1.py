import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.linear_model as sklin

# Load the data
oecd_bli        = pd.read_csv("../datasets/lifesat/oecd_bli_2015.csv", thousands=",")
gdp_per_capita  = pd.read_csv("../datasets/lifesat/gdp_per_capita.csv", thousands=",")

