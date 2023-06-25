import unittest
import re
from functions import remove_urls
from functions import remove_special_characters
from main import twitter_cleaned
import coverage
#Extract some of the texts that contain urls from the csv


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

class TestRemoveSpecialCharacters(unittest.TestCase):
    def test_remove_special_characters(self):
        dataset = twitter_cleaned

        cleaned_dataset = remove_special_characters(dataset)

        # Verify that special characters and numbers are removed
        self.assertEqual(cleaned_dataset[0]["text"], "this is a text with special characters ")
        self.assertEqual(cleaned_dataset[1]["text"], "another text with numbers ")
        self.assertEqual(cleaned_dataset[2]["text"], "text without any special characters or numbers")

        # Verify that other keys and values are preserved
        self.assertEqual(cleaned_dataset[0]["id"], 1)
        self.assertEqual(cleaned_dataset[0]["label"], "positive")

        self.assertEqual(cleaned_dataset[1]["id"], 2)
        self.assertEqual(cleaned_dataset[1]["label"], "negative")

        self.assertEqual(cleaned_dataset[2]["id"], 3)
        self.assertEqual(cleaned_dataset[2]["label"], "neutral")

        # Verify that dictionaries with all-digit keys are excluded
        dataset_with_digit_key = [{"123": "Value with numbers"}]
        cleaned_dataset = remove_special_characters(dataset_with_digit_key)
        self.assertEqual(len(cleaned_dataset), 0)

if __name__ == '__main__':
    unittest.main()
    
    
