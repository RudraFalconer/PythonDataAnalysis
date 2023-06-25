import unittest
import re
from functions import remove_urls
from functions import remove_special_characters
from functions import remove_non_ascii
from functions import count_words
from functions import remove_stopwords
from functions import bag_of_words
#from main import twitter_cleaned
import coverage
#Extract some of the texts that contain urls from the csv

cov = coverage.Coverage()
cov.start()

class TestRemoveURLs(unittest.TestCase):
    def test_remove_urls(self):
        # Test case 1: URL in the middle of the string
        input_text = "http://twitpic.com/4gvdi - You would have a hard time getting out of bed too, if this is what you had in it!"
        expected_output = " - You would have a hard time getting out of bed too, if this is what you had in it!"
        self.assertEqual(remove_urls(input_text), expected_output)

        # Test case 2: URL at the beginning of the string
        input_text = "http://twitpic.com/4gwou - And his daughter! omg.... so cute... Sharina"
        expected_output = " - And his daughter! omg.... so cute... Sharina"
        self.assertEqual(remove_urls(input_text), expected_output)

        # Test case 3: URL at the end of the string
        input_text = "damn good weather!!! it's cool to be walking in park   http://twitpic.com/4gwj5"
        expected_output = "damn good weather!!! it's cool to be walking in park   "
        self.assertEqual(remove_urls(input_text), expected_output)

        # Test case 4: Multiple URLs in the string
        input_text = "Check out these websites: http://example1.com and http://example2.com"
        expected_output = "Check out these websites:  and "
        self.assertEqual(remove_urls(input_text), expected_output)

        # Test case 5: No URLs in the string
        input_text = "This is a regular text without any URLs"
        expected_output = "This is a regular text without any URLs"
        self.assertEqual(remove_urls(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()
    
#remove special charachters test

class RemoveSpecialCharactersTest(unittest.TestCase):
    def test_remove_special_characters(self):
        # Sample dataset
        dataset = [
            {"text": "This is a sample sentence with special characters: @#$%"},
            {"text": "Some numbers: 1234567890"},
            {"text": "No special characters here."},
            {"text": "Another example with !@^&* special characters."},
        ]

        expected_result = [
            {"text": "this is a sample sentence with special characters "},
            {"text": "some numbers "},
            {"text": "no special characters here "},
            {"text": "another example with  special characters "},
        ]

        cleaned_dataset = remove_special_characters(dataset)
        self.assertEqual(cleaned_dataset, expected_result)

if __name__ == '__main__':
    unittest.main()
    
class RemoveNonAsciiTest(unittest.TestCase):
    def test_remove_non_ascii(self):
        # Sample dataset with non-ASCII characters
        dataset = [
            {"text": "Hello, World!"},
            {"text": "Hëllö, Wörld!"},
            {"text": "こんにちは、世界！"},
            {"text": "你好，世界！"},
            {"text": "안녕하세요, 세계!"},
        ]

        expected_result = [
            {"text": "Hello, World!"},
            {"text": "Hll, Wrld!"},
            {"text": "       !"},
            {"text": "   , !"},
            {"text": ",   !"},
        ]

        cleaned_dataset = remove_non_ascii(dataset)
        self.assertEqual(cleaned_dataset, expected_result)

if __name__ == '__main__':
    unittest.main()

class CountWordsTest(unittest.TestCase):
    def test_count_words(self):
        # Sample dataset
        dataset = [
            {"text": "Hello, World!"},
            {"text": "Hello, Python!"},
            {"text": "Python is great."},
            {"text": "Hello, Hello, Hello!"},
        ]

        expected_result = [
            {"text": "Hello, World!", "Word_Count": {"Hello,": 1, "World!": 1}},
            {"text": "Hello, Python!", "Word_Count": {"Hello,": 1, "Python!": 1}},
            {"text": "Python is great.", "Word_Count": {"Python": 1, "is": 1, "great.": 1}},
            {"text": "Hello, Hello, Hello!", "Word_Count": {"Hello,": 3}},
        ]

        counted_dataset = count_words(dataset)
        self.assertEqual(counted_dataset, expected_result)
        
if __name__ == '__main__':
    unittest.main()
    
class RemoveStopwordsTest(unittest.TestCase):
    def test_remove_stopwords(self):
        # Sample dataset
        dataset = [
            {"text": "This is a sample sentence."},
            {"text": "I love coding in Python."},
            {"text": "Stopwords should be removed."},
            {"text": "Keep important words only."},
        ]

        expected_result = [
            {"text": "This sample sentence."},
            {"text": "love coding Python."},
            {"text": "Stopwords removed."},
            {"text": "Keep important words only."},
        ]

        stopwords = ['is', 'a', 'in', 'should', 'be', 'I']
        cleaned_dataset = remove_stopwords(dataset, stopwords)
        self.assertEqual(cleaned_dataset, expected_result)
        
if __name__ == '__main__':
    unittest.main()
    
    
class BagOfWordsTest(unittest.TestCase):
    def test_bag_of_words(self):
        # Sample dataset
        dataset = [
            {"text": "This is a sample sentence."},
            {"text": "Another sentence with more words."},
            {"text": "This is the third sentence."},
        ]

        expected_word_frequencies = {
            "This": 2,
            "is": 2,
            "a": 1,
            "sample": 1,
            "sentence.": 3,
            "Another": 1,
            "with": 1,
            "more": 1,
            "words.": 1,
            "the": 1,
            "third": 1,
        }

        expected_sorted_unique_words = [
            "Another",
            "This",
            "a",
            "is",
            "more",
            "sentence.",
            "sample",
            "the",
            "third",
            "with",
            "words.",
        ]

        word_frequencies, sorted_unique_words = bag_of_words(dataset)
        self.assertEqual(word_frequencies, expected_word_frequencies)
        self.assertEqual(sorted_unique_words, expected_sorted_unique_words)

if __name__ == '__main__':
    unittest.main()
    
cov.stop()
cov.report()
cov.save()