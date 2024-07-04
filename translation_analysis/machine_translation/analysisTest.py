import json
import pandas as pd
from collections import Counter
import re


#Open the samples_raw_en_es.json file
with open('C:/Users/yasangi.rathnamali/Desktop/Python/projects/translation_analysis/machine_translation/raw/samples_raw_en_es.json', "r", encoding="utf-8") as file:   
    raw_data = json.load(file) #Load the json data of raw dataset,

raw_data_df = pd.json_normalize(raw_data)
#print(raw_data_df)

#Open the samples_cleaned_en_es.json file
with open('C:/Users/yasangi.rathnamali/Desktop/Python/projects/translation_analysis/machine_translation/cleaned/samples_cleaned_en_es.json', "r", encoding="utf-8") as file:   
    cleaned_data = json.load(file) #Load the json data of cleaned dataset

cleaned_data_df = pd.json_normalize(cleaned_data)
#print(cleaned_data_df)

#conver the datasets to lower case and split into words(tokenization)
raw_data_df['en-IE'] = raw_data_df['en-IE'].str.lower().str.split()
raw_data_df['es-ES'] = raw_data_df['es-ES'].str.lower().str.split()
#print(raw_data_df)

cleaned_data_df['src'] = cleaned_data_df['src'].str.lower().str.split()
cleaned_data_df['mt'] = cleaned_data_df['mt'].str.lower().str.split()
#print(cleaned_data_df)

#Calculate total words count and unique words count
raw_data_df['en-IE_totalWordsCount'] = raw_data_df['en-IE'].apply(len)
raw_data_df['en-IE_uniqueWordsCount'] = raw_data_df['en-IE'].apply(set).apply(len)
raw_data_df['es-ES_totalWordsCount'] = raw_data_df['es-ES'].apply(len)
raw_data_df['es-ES_uniqueWordsCount'] = raw_data_df['es-ES'].apply(set).apply(len)
print(raw_data_df)

cleaned_data_df['src_totalWordsCount'] = cleaned_data_df['src'].apply(len)
cleaned_data_df['src_uniqueWordsCount'] = cleaned_data_df['src'].apply(set).apply(len)
cleaned_data_df['mt_totalWordsCount'] = cleaned_data_df['mt'].apply(len)
cleaned_data_df['mt_uniqueWordsCount'] = cleaned_data_df['mt'].apply(set).apply(len)
print(cleaned_data_df) 

#To get all the unique words count and it's occurences in src and mt
allUniqueWords_src = sum(cleaned_data_df['src'],[]).sort()
allUniqueWordsCounts_src = Counter(allUniqueWords_src)

allUniqueWords_mt = sum(cleaned_data_df['mt'],[]).sort()
allUniqueWordsCounts_mt = Counter(allUniqueWords_mt)

#Convert the all words count to a dataframe
allUniqueWords_src_df = pd.DataFrame(allUniqueWordsCounts_src.items(), columns=['Unique_Word', 'Occurences'])
#print("words",allUniqueWords_src)
allUniqueWords_mt_df = pd.DataFrame(allUniqueWordsCounts_mt.items(), columns=['Unique_Word', 'Occurences'])
#print("words",allUniqueWords_mt)

#Calculate the total number of unique words
totalUniqueWords_src = len(allUniqueWordsCounts_src)
totalUniqueWords_mt = len(allUniqueWordsCounts_mt)

#Calculate each word uniqueness score
allUniqueWords_src_df['word_uniqueness_score'] = allUniqueWords_src_df['Occurences'] / totalUniqueWords_src
print(allUniqueWords_src_df.head)

allUniqueWords_mt_df['word_uniqueness_score'] = allUniqueWords_mt_df['Occurences'] / totalUniqueWords_mt
print(allUniqueWords_mt_df.head)