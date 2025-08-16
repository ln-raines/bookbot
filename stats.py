def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def chars_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for char in chars_dict:
        if char.isalpha():
            sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(char):
    return char["num"]