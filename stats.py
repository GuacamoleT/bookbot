def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = text.lower()
    count = {}
    for char in chars:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(item):
    return item["num"]

def sort_dict(count):
    dict_list = []
    for k, v in count.items():
        dict_list.append({"char": k, "num": v})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
    
