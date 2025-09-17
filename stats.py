def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts