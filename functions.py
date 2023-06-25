import re
from stopwords import stopwords

def remove_urls(text):
    return re.sub(r'http\S+', '', text)

def remove_special_characters(dataset):
    """
    Cleans the dataset by removing special characters from the 'text' field.
    
    Args:
        dataset (list): A list of dictionaries representing the dataset.
        
    Returns:
        list: A cleaned dataset with special characters removed from the 'text' field.
    """    
    cleaned_dataset = []
    for data in dataset:
        cleaned_data = {}
        for key, value in data.items():
            if key == "text":
                value = remove_urls(value)
                cleaned_value = re.sub(r"[^a-zA-Z0-9 ]", "", value) # Remove non-alphanumeric characters
            else:
                cleaned_value = value
            cleaned_data[key] = cleaned_value.lower() # Convert cleaned value to lowercase
        if not all(key.isdigit() for key in cleaned_data.keys()):
            cleaned_dataset.append(cleaned_data)
    return cleaned_dataset

def remove_stopwords(dataset):
    """
    Cleans the dataset by removing stopwords from the 'text' field.

    Args:
        dataset (list): A list of dictionaries representing the dataset.

    Returns:
        list: A cleaned dataset with stopwords removed from the 'text' field.
    """
    cleaned_dataset = []
    for data in dataset:
        cleaned_data = {}
        for key, value in data.items():
            words = value.split()  # Split text into individual words
            filtered_words = [word for word in words if word not in stopwords]  # Filter out stopwords
            cleaned_data[key] = ' '.join(filtered_words)  # Join filtered words back into a sentence
        if not all(key.isdigit() for key in cleaned_data.keys()):  # Check if all keys are not digits
            cleaned_dataset.append(cleaned_data)
    return cleaned_dataset



def bag_of_words(dataset):
    """
    Compute word frequencies and unique words from a dataset.

    Args:
        dataset (list): A list of dictionaries representing the dataset.
            Each dictionary should contain a "text" key with the text data.

    Returns:
        tuple: A tuple containing two elements:
            - word_frequencies (dict): A dictionary where the keys are words and the values
              are the frequencies of those words in the dataset.
            - sorted_unique_words (list): A sorted list of unique words found in the dataset.
    """
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
    """
    Remove non-ASCII characters from the text values in a dataset.

    Args:
        dataset (list): A list of dictionaries representing the dataset.

    Returns:
        list: A list of dictionaries with non-ASCII characters removed from the "text" values.
    """
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
    """
    Count the occurrences of each word in the "text" values of a dataset.

    Args:
        dataset (list): A list of dictionaries representing the dataset.

    Returns:
        list: A list of dictionaries with a "Word_Count" key added to each dictionary,
            containing a dictionary of word counts.
    """
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

