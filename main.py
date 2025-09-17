from stats import get_num_words, count_letters

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        file_content = f.read()
    return file_content

def main():
    path = './books/frankenstein.txt'
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    letter_counts = count_letters(book_text)
    print("--------- Character Count -------")
    # Ordena por valor decrescente
    for letter, count in sorted(letter_counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{letter}: {count}")
    print("============= END ===============")

if __name__ == '__main__':
    main()