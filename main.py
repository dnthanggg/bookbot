def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_text = count_words(text)
    print(f"{count_text} words in the document")
    
    char_dict = count_char(text)
    sort_dict_by_value(char_dict)



def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    alphabet_dict = {chr(i): 0 for i in range(97, 123)}
    lowered_string = text.lower()
    for word in lowered_string:
        if word in alphabet_dict:
            alphabet_dict[word] += 1
    return (alphabet_dict)        

def sort_dict_by_value(dict):
    sort_by_value = sorted(dict.items(), reverse=True, key= lambda x:x[1])
    for tup in sort_by_value:
        print(f"the {tup[0]} character was found {tup[1]} times")


main()