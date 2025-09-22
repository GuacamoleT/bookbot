import sys

def main():
    if len(sys.argv) >1:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = word_count(text)
        num_chars = char_count(text)
        sort_chars = sort_dict(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for item in sort_chars:
            if item["char"].isalpha():
                print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import word_count
from stats import char_count
from stats import sort_dict

main()