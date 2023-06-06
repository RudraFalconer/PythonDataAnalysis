import re
from stopwords import stopwords

def remove_urls(text):
    return re.sub(r'http\S+', '', text)

def remove_special_characters(dataset):
    for data in dataset:
        for key, value in data.items():
            if key == "text":
                value = remove_urls(value)    
                cleaned_value = re.sub(r"[^a-zA-Z0-9 ]", "", value)
            else:
                cleaned_value = value
            data[key] = cleaned_value.lower()
    return dataset

def remove_stopwords(dataset):
    for data in dataset:
        for key, value in data.items():
            words = value.split()
            filtered_words = [word for word in words if word not in stopwords]
            data[key] = ' '.join(filtered_words)
    return dataset


def bag_of_words(dataset):
    word_frequencies = {}
    unique_words = set()

    for data in dataset:
        for value in data.values():
            words = value.split()
            for word in words:
                if word not in word_frequencies:
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
                unique_words.add(word)

    # Sort unique words alphabetically
    sorted_unique_words = sorted(list(unique_words))

    return word_frequencies, sorted_unique_words