MAX_ARRAY_SIZE = 100  # Максимальний розмір масиву

def odd_word_processing(text):
    if not text.strip():
        return "Пусте введення."
    
    words = text.split()
    words_array = []
    for word in words:
        if not word.isalpha():
            return f"Неправильне слово: '{word}'. Слово має містити лише літери."
        if len(words_array) < MAX_ARRAY_SIZE:
            words_array.append(word)
        else:
            return "Переповнення масиву. Деякі слова не будуть оброблені."
    
    processed_words = []
    for word in words_array:
        if len(word) % 2 != 0:
            processed_word = word[1:-1] + "," if len(word) > 1 else word + ","
            processed_words.append(processed_word)
    
    if not processed_words:
        return "Немає слів з непарною кількістю літер."
    
    result = " ".join(processed_words)
    return result