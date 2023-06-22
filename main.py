import csv
import pandas as pd
import matplotlib.pyplot as plt
from functions import remove_special_characters
from stopwords import stopwords
from functions import remove_stopwords
from functions import remove_non_ascii
from functions import remove_urls
import functions
import re
import numpy as np
from wordcloud import WordCloud
import coverage
cov = coverage.Coverage()
cov.start()

twitter_cleaned = []
#Ej 1.1
with open('twitter_reduced.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        twitter_cleaned.append(row)
        
# Mostrar los 5 primeros registros
for i in range(5):
    print(twitter_cleaned[i])      
    

#Eliminamos caracteres especiales y urls
twitter_cleaned = remove_special_characters(twitter_cleaned)
for i in range(5):
    print(twitter_cleaned[i])
    

#use non ascii function and apply to twitter_cleaned, then print the first 5 entries
twitter_cleaned = remove_non_ascii(twitter_cleaned)
for i in range(5):
    print(twitter_cleaned[i])

print("stopwords")
twitter_cleaned = remove_stopwords(twitter_cleaned)
for i in range(5):
    print(twitter_cleaned[i])

#bag of words 

word_frequencies, unique_words = functions.bag_of_words(twitter_cleaned)

first_10_word_frequencies = dict(list(word_frequencies.items())[:5])
print(first_10_word_frequencies)

word_frequencies_total = dict(list(word_frequencies.items()))
word_frequencies_total = dict(sorted(word_frequencies_total.items()))

filtered_word_frequencies = {key: value for key, value in word_frequencies_total.items() if not key.isdigit()}

first_10_entries = list(filtered_word_frequencies.items())[:10]

print(first_10_entries)
#print(first_10_word_frequencies)

#i want to count the number of words that appears in each "text" key in the twitter_cleaned list of dictionaries, and then print the first 5 entries

twitter_cleaned_counts = functions.count_words(twitter_cleaned)

print(twitter_cleaned_counts[0])
    
#save the twitter_cleaned_counts list of dictionaries to a csv file. Column names should be "sentiment", "id", "query", "user", "date", "Word_Count"

with open('twitter_cleaned_counts.csv', 'w', encoding='utf-8') as csv_file:
    fieldnames = ['sentiment', 'id', 'query', 'user', 'date', 'Word_Count', "text"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in twitter_cleaned_counts:
        writer.writerow(data)
        
#conver twitter_cleaned_counts to a pandas dataframe and print the first 5 entries

twitter_cleaned_counts_df = pd.DataFrame(twitter_cleaned_counts)
print(twitter_cleaned_counts_df["sentiment"])

#Showing the unique counts of "sentiment" column

print(twitter_cleaned_counts_df["sentiment"].value_counts()) #2 clusters, 1 indica tweet positivo y otro negativo.

#identify if there are NAs in the "text" column in twitter_cleaned_counts_df
print(twitter_cleaned_counts_df.isna().sum()) #no hay NAs

#generate a wordcloud with the "text" column in twitter_cleaned_counts_df based on the clusters given by the "sentiment" column

# Create a list of words after selecting only sentiment = 0

sentiment0_df = twitter_cleaned_counts_df[twitter_cleaned_counts_df["sentiment"] == "0"]

text = " ".join(review for review in sentiment0_df.text)
#what to do next
# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

# Create a list of words after selecting only sentiment = 4

sentiment4_df = twitter_cleaned_counts_df[twitter_cleaned_counts_df["sentiment"] == "4"]


#what to do next
# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

#transform filtered_word_frequencies to a pandas dataframe

filtered_word_frequencies_df = pd.DataFrame(filtered_word_frequencies.items(), columns=['word', 'frequency'])
#make a histogram with the filtered_word_frequencies_df dataframe frequency column
# Calculate the number of bins using the Freedman-Diaconis rule
q75, q25 = np.percentile(filtered_word_frequencies_df['frequency'], [75 ,25])
iqr = q75 - q25
bin_width = 2 * iqr * (len(filtered_word_frequencies_df['frequency']) ** (-1/3))
num_bins = int((filtered_word_frequencies_df['frequency'].max() - filtered_word_frequencies_df['frequency'].min()) / bin_width)
plt.hist(filtered_word_frequencies_df['frequency'], bins=2500)
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Frequency Histogram')
plt.xlim(0, 1000)
plt.yscale('log')
plt.show()

cov.stop()
cov.save()
