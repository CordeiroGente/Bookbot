# python
from stats import get_num_words, count_letters
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    letter_counts = count_letters(book_text)
    print("--------- Character Count -------")
    for letter, count in sorted(letter_counts.items(), key=lambda item: item[1], reverse=True):
        if not letter.isalpha():
            continue
        print(f"{letter}: {count}")
    print("============= END ===============")

if __name__ == '__main__':
    main()