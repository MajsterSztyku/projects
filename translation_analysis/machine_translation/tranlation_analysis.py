import json
import pandas as pd
from collections import Counter

#Open the samples_raw_en_es.json file
with open('C:/Users/yasangi.rathnamali/Desktop/Python/projects/translation_analysis/machine_translation/raw/samples_raw_en_es.json', "r", encoding="utf-8") as file:   
    raw_data = json.load(file) #Load the json data of raw dataset

#Normalize the raw data
raw_data_df = pd.json_normalize(raw_data)
#print(raw_data_df.head())


#Open the samples_cleaned_en_es.json file
with open('C:/Users/yasangi.rathnamali/Desktop/Python/projects/translation_analysis/machine_translation/cleaned/samples_cleaned_en_es.json', "r", encoding="utf-8") as file:   
    cleaned_data = json.load(file) #Load the json data of cleaned dataset

#Normalize the cleaned data
cleaned_data_df = pd.json_normalize(cleaned_data)
#print(cleaned_data_df.head()) 

#raw_data_df.info()
#cleaned_data_df.info()

# to see all the words count in Raw data - en-IE column
#raw_data_df['AllRawWordCount'] = raw_data_df['en-IE'].str.split().str.len()
#print("All raw data words count is ",sum(raw_data_df['AllRawWordCount']))

'''
#To get All raw data words count for en-IE column
allRawWordCount_en = raw_data_df['en-IE'].str.split().str.len()
print("All raw data words count for en-IE column is ",sum(allRawWordCount_en))

#To get All raw data words count for es-ES column
allRawWordCount_es = raw_data_df['es-ES'].str.split().str.len()
print("All raw data words count for es-ES column is ",sum(allRawWordCount_es))

#To get All cleaned data words count for src column
allCleanedWordCount_src = cleaned_data_df['src'].str.split().str.len()
print("All raw data words count for src column is ",sum(allCleanedWordCount_src))

#To get All cleaned data words count for mt column
allCleanedWordCount_mt = cleaned_data_df['mt'].str.split().str.len()
print("All raw data words count for mt column is ",sum(allCleanedWordCount_mt))


#To get Unique words count for raw dataset en-IE column
uniqueWordsCount = set(raw_data_df['en-IE'].str.lower().str.split().sum())
print(uniqueWordsCount)
'''

#To get all words
#raw_data_df['allWordsCount'] = raw_data_df['en-IE'].apply(len)

#To get all unique words count for en in raw dataset
raw_data_df['uniqueWordsCount_en'] = raw_data_df['en-IE'].str.lower().str.split().apply(set).apply(len)

#To get all unique words count for es in raw dataset
raw_data_df['uniqueWordsCount_es'] = raw_data_df['es-ES'].str.lower().str.split().apply(set).apply(len)

print(raw_data_df)
#raw_data_df.head(20).to_csv('C:/Users/yasangi.rathnamali/Desktop/Python/projects/translation_analysis/machine_translation/raw/raw_analyzed.csv',sep='\t',encoding='utf-8')

#To get all unique words count for src in cleaned dataset
cleaned_data_df['uniqueWordsCount_src'] = cleaned_data_df['src'].str.lower().str.split().apply(set).apply(len)

#To get all unique words count for mt
cleaned_data_df['uniqueWordsCount_mt'] = cleaned_data_df['mt'].str.lower().str.split().apply(set).apply(len)
print(cleaned_data_df)

#eachWordCount_src = Counter(cleaned_data_df['src'])
#print(eachWordCount_src.items())

cleaned_data_df['src'].apply(lambda x: pd.value_counts(x.split(" ")).sum(axis=0))