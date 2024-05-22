
def get_book_text(path :str) -> str: 
    try:
        with open(path) as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file from {path}: {e}")
    
def get_book_wordcount(book_text: str) -> int:
    try:
        words = book_text.split()
        return len(words)
    except Exception as e:
        print(f"Error retrieving word count: {e}")

def get_book_letter_count(book_text :str) -> dict:
    try:
        text = book_text.lower()
        letter_count = {}
        letters = ''.join(filter(str.isalpha, text))

        for letter in letters: 
            if letter_count.get(letter) is None:
                letter_count[letter] = 1
            else:
                letter_count[letter] = letter_count[letter] + 1
        return letter_count
    except Exception as e:
        print(f"Error retrieving letter count: {e}")

def generate_lettercount_report(book_text: str) -> dict: 
    try:
        letter_count = get_book_letter_count(book_text)
        letter_count_report_list = []

        letter_count_report_list = sorted(letter_count.items(), key = lambda x:x[1], reverse=True)

        return dict(letter_count_report_list)
    except Exception as e:
        print(f"Error generating letter count report: {e}")

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    wordcount = get_book_wordcount(text)  
    lettercount_dict = get_book_letter_count(text) 
    lettercount_report_dict = generate_lettercount_report(text) 
    #print(text)
    #print(wordcount)
    #print(lettercount_dict)
    print(lettercount_report_dict)

if __name__ == '__main__':
    main()




