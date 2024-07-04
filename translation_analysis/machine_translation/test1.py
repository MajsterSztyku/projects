import json

import pandas as pd

#Open the samples_raw_en_es.json file
with open('C:/Users/yasangi.rathnamali/Desktop/Python/projects/translation_analysis/machine_translation/raw/samples_raw_en_es.json', "r", encoding="utf-8") as file:   
    raw_data = json.load(file) #Load the json data of raw dataset

#Normalize the raw data
raw_data_df = pd.json_normalize(raw_data)
print(raw_data_df.head())


#Open the samples_cleaned_en_es.json file
with open('C:/Users/yasangi.rathnamali/Desktop/Python/projects/translation_analysis/machine_translation/cleaned/samples_cleaned_en_es.json', "r", encoding="utf-8") as file:   
    cleaned_data = json.load(file) #Load the json data of cleaned dataset

#Normalize the cleaned data
cleaned_data_df = pd.json_normalize(cleaned_data)
print(cleaned_data_df.head()) 


