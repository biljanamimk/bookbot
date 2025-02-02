
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    freq_char = get_freq_char(text)
    #print(f"{num_words} words found in the document")
    #print(f"{freq_char}")
    #print("-----------------------------------")
    get_dict(freq_char)


def get_freq_char(text):
    new_text = text.lower()
    freq = {}
    for char in new_text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def get_dict(dict_freq):
    list_dict = []
    for key, value in dict_freq.items():
        if key.isalpha():
            #print(f"key: {key}, num: {value}")
            list_dict.append({'key': key, 'num': value})

    list_dict.sort(reverse=True, key=sort_on)
    #print(list_dict)
    for dict in list_dict:
        print(f"The '{dict["key"]}' character was found {dict["num"]} times")


main()
