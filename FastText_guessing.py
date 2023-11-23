import re
import fasttext
import random
import string
from collections import Counter

model = fasttext.load_model('cc.en.300.bin')
all_words = model.get_words()
def guess(word):
    try:
        pattern = re.compile(word.replace('_', r'\w'))
        similarity_scores = [(model.get_word_vector(word_vec), word_vec) for word_vec in all_words]
        matching_words = [words for vector, words in similarity_scores if pattern.match(words) and len(words) == len(word)]
        matching_words.sort(key=lambda words: model.get_word_vector(words).dot(model.get_word_vector(word)))

        prob_letters = []
        for words in matching_words:
            for letter, predicted_letter in zip(word, words):
                if letter == '_' and predicted_letter:
                    prob_letters.append(predicted_letter)
        
        letter_counts = Counter(prob_letters)
        most_common_letters = letter_counts.most_common(4)
        top_four_letters = [letter for letter, count in most_common_letters]
        return random.choice(top_four_letters)
    
    except:
        return random.choice(string.ascii_uppercase)

#for i in range(10):
#    masked_word = '_____t__n'
#    word_length = len(masked_word)
#    matching_words = guess(masked_word)
#    print(matching_words)
