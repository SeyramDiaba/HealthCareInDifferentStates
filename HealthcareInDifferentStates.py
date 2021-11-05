import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt

healthcare = pd.read_csv("healthcare.csv")

# Inspecting healthcare dataframe
print(healthcare.head(500))

# Checking all unique dianoses in our dataset
print(healthcare['DRG Definition'].unique())

# Grabbing only the rows in the dataset that are about chest pain.
chest_pain = healthcare[healthcare['DRG Definition']== '313 - CHEST PAIN']

# Every chest pain diagnosis in Alabama
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == 'AL'] 

# Average cost of those diagnoses
costs = alabama_chest_pain[' Average Covered Charges '].values
print(costs)

# Visualising data using a boxplot
#plt.boxplot(costs)
#plt.show()

# Boxplot for every state
# states = chest_pain['Provider State'].unique()
# print(states)

# Separate the dataset into a dataset for each state.
# datasets = []
# for state in states:
#   datasets.append(chest_pain[chest_pain['Provider State']== state][' Average Covered Charges '].values)

# 50 boxplots for each state

# plt.figure(figsize = (20,6)) # this will make our figure long to allow room for so many boxplots!
# plt.boxplot(datasets, labels = states)
# plt.show()

# analysing data for '069 - TRANSIENT ISCHEMIA'
trans= healthcare[healthcare['DRG Definition'] == '069 - TRANSIENT ISCHEMIA']

# States grouped by region
states = trans['Provider State'].unique()
#print(states)
container = []
for state in states:
  container.append(trans[trans['Provider State']== state][' Average Total Payments '].values)
# for state in states:
#   datasets.append(chest_pain[chest_pain['Provider State']== state][' Average Covered Charges '].values)



print(container)
# boxplot from California of  069 - TRANSIENT ISCHEMIA costs
plt.figure(figsize = (20,6))
plt.boxplot(container, labels= states)
plt.show()