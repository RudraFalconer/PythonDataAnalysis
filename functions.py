import re
from stopwords import stopwords

def remove_urls(text):
    return re.sub(r'http\S+', '', text)

def remove_special_characters(dataset):
    cleaned_dataset = []
    for data in dataset:
        cleaned_data = {}
        for key, value in data.items():
            if key == "text":
                value = remove_urls(value)
                cleaned_value = re.sub(r"[^a-zA-Z0-9 ]", "", value)
            else:
                cleaned_value = value
            cleaned_data[key] = cleaned_value.lower()
        if not all(key.isdigit() for key in cleaned_data.keys()):
            cleaned_dataset.append(cleaned_data)
    return cleaned_dataset

def remove_stopwords(dataset):
    cleaned_dataset = []
    for data in dataset:
        cleaned_data = {}
        for key, value in data.items():
            words = value.split()
            filtered_words = [word for word in words if word not in stopwords]
            cleaned_data[key] = ' '.join(filtered_words)
        if not all(key.isdigit() for key in cleaned_data.keys()):
            cleaned_dataset.append(cleaned_data)
    return cleaned_dataset


def bag_of_words(dataset):
    word_frequencies = {}
    unique_words = set()

    for data in dataset:
        if "text" in data:
            text = data["text"]
            words = text.split()
            for word in words:
                if word not in word_frequencies:
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
                unique_words.add(word)

    # Sort unique words alphabetically
    sorted_unique_words = sorted(list(unique_words))

    return word_frequencies, sorted_unique_words


#create a function to remove all non ASCII characters from a list of dictionaries, targeting a single key, which is "text"

def remove_non_ascii(dataset):
    cleaned_dataset = []
    for data in dataset:
        cleaned_data = {}
        for key, value in data.items():
            if key == "text":
                cleaned_value = value.encode("ascii", "ignore").decode()
            else:
                cleaned_value = value
            cleaned_data[key] = cleaned_value
        if not all(key.isdigit() for key in cleaned_data.keys()):
            cleaned_dataset.append(cleaned_data)
    return cleaned_dataset

#create function to count words in a text contained in a list of dictionaries. Output is a dictionary with words as keys and counts as values

def count_words(dataset):
    for data in dataset:
        text = data.get("text", "")
        if isinstance(text, list):
            text = " ".join(text)
        words = text.split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        data["Word_Count"] = word_counts
    return dataset

