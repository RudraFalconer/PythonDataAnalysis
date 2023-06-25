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
# Ej 1.1
with open('twitter_reduced.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        twitter_cleaned.append(row)
        
# Ej 1.1 Mostrar los 5 primeros registros
print("Show the 5 first entries of the dataset: ")

for i in range(5):
    print(twitter_cleaned[i])
          
print("-----------------------------------------------")
   
# Ej 2
#Eliminamos caracteres especiales y urls
twitter_cleaned = remove_special_characters(twitter_cleaned)
#for i in range(5):
#    print(twitter_cleaned[i])
    

#use non ascii function and apply to twitter_cleaned, then print the last 5 entries
twitter_cleaned = remove_non_ascii(twitter_cleaned)
#show last 5 entries of twitter_cleaned
print("Print the last 5 entries of the dataset after removing stopwords: ")
twitter_cleaned = remove_stopwords(twitter_cleaned)
for i in range(len(twitter_cleaned)-5, len(twitter_cleaned)):
    print(twitter_cleaned[i])

print("-----------------------------------------------")

#Ej 3
#bag of words 

print("Print 5 first entrys of word count dictionary")

word_frequencies, unique_words = functions.bag_of_words(twitter_cleaned)
count = 0
for key, value in word_frequencies.items():
    print(key, value)
    count += 1
    if count == 5:
        break

print("-----------------------------------------------")

print("Print 10 first entries of the word frequencies dictionary:")

sorted_keys = sorted(word_frequencies.keys())  # Sort keys alphabetically
for key in sorted_keys[:10]:
    print(key)

print("-----------------------------------------------")    
    
#Ej 4
#save the twitter_cleaned_counts list of dictionaries to a csv file. Column names should be "sentiment", "id", "query", "user", "date", "Word_Count"
twitter_cleaned_counts = functions.count_words(twitter_cleaned)

print("Element 20 with new word count column generated")
print(twitter_cleaned_counts[19])
print("-----------------------------------------------")

with open('twitter_cleaned_counts.csv', 'w', encoding='utf-8') as csv_file:
    fieldnames = ['sentiment', 'id', 'query', 'user', 'date', 'Word_Count', "text"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in twitter_cleaned_counts:
        writer.writerow(data)
        
#conver twitter_cleaned_counts to a pandas dataframe and print the first 5 entries
twitter_cleaned_counts_df = pd.DataFrame(twitter_cleaned_counts)


# Ej 5.1
#Showing the unique counts of "sentiment" column
print("Unique counts of sentiment column, which indicate existing clusters:")
print(twitter_cleaned_counts_df["sentiment"].value_counts()) #2 clusters, 1 indica tweet positivo y otro negativo.
print("-----------------------------------------------")
#identify if there are NAs in the "text" column in twitter_cleaned_counts_df
print("Identify if there are NAs in the text column in twitter_cleaned_counts_df:")
print(twitter_cleaned_counts_df.isna().sum()) #no hay NAs
print("-----------------------------------------------")   
#generate a wordcloud with the "text" column in twitter_cleaned_counts_df based on the clusters given by the "sentiment" column

# Create a list of words after selecting only sentiment = 0

sentiment0_df = twitter_cleaned_counts_df[twitter_cleaned_counts_df["sentiment"] == "0"]

text = " ".join(review for review in sentiment0_df.text)

# Create the wordcloud object
wordcloud = WordCloud(width=600, height=600, margin=0).generate(text)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

plt.savefig("WrodCloud0.png", format='png') #not working, only saving blank image, dont know why

# Create a list of words after selecting only sentiment = 4

sentiment4_df = twitter_cleaned_counts_df[twitter_cleaned_counts_df["sentiment"] == "4"]

# Create the wordcloud object
wordcloud = WordCloud(width=600, height=600, margin=0).generate(text)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
plt.savefig("WrodCloud0.png", format='png')
#transform filtered_word_frequencies to a pandas dataframe
#transform filtered_word_frequencies to a pandas dataframe

filtered_word_frequencies_df = pd.DataFrame(word_frequencies.items(), columns=['word', 'frequency'])
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
