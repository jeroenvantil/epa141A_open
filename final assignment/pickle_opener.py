import pickle
import pandas as pd

path = "final assignment/"

filename_outcomes = "saved_outcomes.pkl"
filename_experiments = "saved_experiments.pkl"

with open(filename_outcomes, 'rb') as file:
    outcomes = pickle.load(file)
    # print(outcomes)

outcomes_df = pd.DataFrame(outcomes)

outcomes_df.to_csv('outcomes.csv', index_label='index')

with open(filename_experiments, 'rb') as file:
    experiments = pickle.load(file)
    # print(outcomes)

experiments_df = pd.DataFrame(experiments)

experiments_df.to_csv('experiments.csv', index_label='index')