def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_number_of_words(text):
    return len(text.split())

def get_character_occurence(text):
    character_count = {}
    for char in text:
        if char.isalpha():
            character_lower = char.lower()
            if character_lower in character_count:
                character_count[character_lower] += 1
            else:
                character_count[character_lower] = 1

    return character_count

def print_book_report(book_path):
    text = get_book_text(book_path)
    words = get_number_of_words(text)
    chars = get_character_occurence(text)

    chars_sorted = dict(sorted(chars.items(), key=lambda x: x[1], reverse=True))


    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for char in chars_sorted:
        print(f"The '{char}' character was found {chars[char]} times")
    print("--- End report ---")

def main():
    book_path = 'books/frankenstein.txt'

    print_book_report(book_path)    

main()






