import pandas as pd

# Define program constants and variables:
DATA_DIRECTORY = 'data/'
OUTPUT_DIRECTORY = 'output/'
RESPONSES_PATH = DATA_DIRECTORY + 'responses.csv'
OUTPUT_PATH = DATA_DIRECTORY + OUTPUT_DIRECTORY + 'rowStatistics.csv'
EVALUATOR_COUNT = 7

def calculateStatistics(row):
    frequencies = row.value_counts() # Count occurrences per category in row.
    highestFrequency = frequencies.max() # Find the most frequent category.
    agreementProportion = highestFrequency / EVALUATOR_COUNT

    return pd.Series({'Frequencies': frequencies.tolist(), 'Category with highest count': highestFrequency, 'Agreement proportion': agreementProportion})

responsesDF = pd.read_csv(RESPONSES_PATH, header=None)

# Calculate statistics and export them to a CSV file:
rowStatistics = responsesDF.apply(calculateStatistics, axis=1)

rowStatistics.to_csv(OUTPUT_PATH, index=False)
