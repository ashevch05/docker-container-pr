import unittest
from main import odd_word_processing, MAX_ARRAY_SIZE

class TestOddWordProcessing(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(odd_word_processing(""), "Пусте введення.")
    
    def test_non_alphabetic_input(self):
        self.assertEqual(odd_word_processing("hello world123"), "Неправильне слово: 'world123'. Слово має містити лише літери.")
    
    def test_array_overflow(self):
        text = "word " * (MAX_ARRAY_SIZE + 1)
        self.assertEqual(odd_word_processing(text.strip()), "Переповнення масиву. Деякі слова не будуть оброблені.")
    
    def test_no_odd_length_words(self):
        self.assertEqual(odd_word_processing("even four"), "Немає слів з непарною кількістю літер.")
        
if __name__ == "__main__":
    unittest.main()