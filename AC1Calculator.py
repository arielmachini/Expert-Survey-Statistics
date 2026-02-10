from irrCAC.raw import CAC
import pandas as pd

# Define program constants and variables:
DATA_DIRECTORY = 'data/'
RESPONSES_PATH = DATA_DIRECTORY + 'responses.csv'

CATEGORIES_LIST = ['Yes', 'No', 'Not sure']
METRIC_COUNT = 52

responsesDF = pd.read_csv(RESPONSES_PATH, header=None)

# Calculate AC1 for the whole DataFrame:
globalAC1Coefficient = CAC(responsesDF, categories=CATEGORIES_LIST, weights='identity').gwet() # Varies between -1 (complete disagreement) and 1 (perfect agreement).

print(f'Calculated AC1 coefficient: {globalAC1Coefficient['est']['coefficient_value']}.')

# (Optional) Calculate Fleiss' Kappa for the whole DataFrame:
# fleissKappaCoefficient = CAC(responsesDF, categories=CATEGORIES_LIST, weights='identity').fleiss()
# print(f'Calculated Kappa coefficient: {fleissKappaCoefficient['est']['coefficient_value']}.')
