"""Homework # 9"""
# Task #1


def editing_string(value):
    """Delete "#" and symbol before"""
    lst = list(value)
    index_lst = 0
    while "#" in lst:
        if lst[index_lst] == "#":
            lst.pop(index_lst)
            if index_lst == 0:
                continue
            if index_lst == 1:
                lst.pop(index_lst - 1)
                index_lst -= 1
            else:
                lst.pop(index_lst - 1)
                index_lst -= 2
        index_lst += 1
    new_string = "".join(lst)
    return new_string


assert editing_string("a#bc#d") == "bd"
assert editing_string("abc#d##c") == "ac"
assert editing_string("abc##d######") == ""
assert editing_string("#######") == ""
assert editing_string("") == ""


# Task #2


def burn_candles(candles, make_new):
    """Count the total number of candles burned"""
    remainder = 0
    total_burn_candles = 0
    while candles > 0:
        remainder += candles
        total_burn_candles += candles
        candles = remainder // make_new
        remainder = remainder % make_new
    return total_burn_candles


assert burn_candles(5, 2) == 9
assert burn_candles(1, 2) == 1
assert burn_candles(15, 5) == 18
assert burn_candles(12, 2) == 23
assert burn_candles(6, 4) == 7
assert burn_candles(13, 5) == 16
assert burn_candles(2, 3) == 2

# Task #3


def modify_text(text):
    """Count letter and modify string"""
    current_letter = ""
    index_i = -1
    modified_text = ""

    for i in text:
        index_i += 1
        if i == current_letter:
            continue
        current_letter = text[index_i]
        counter = 1
        next_index = index_i + 1

        if next_index == len(text):
            if counter == 1:
                counter = ""
            modified_text += (current_letter + str(counter))
            break

        while text[index_i] == text[next_index]:
            counter += 1
            next_index += 1
            if next_index == len(text):
                break

        if counter == 1:
            counter = ""
        modified_text += (current_letter + str(counter))

    return modified_text


assert modify_text("cccbba") == "c3b2a"
assert modify_text("abeehhhhhccced") == "abe2h5c3ed"
assert modify_text("aaabbceedd") == "a3b2ce2d2"
assert modify_text("abcde") == "abcde"
assert modify_text("aaabbdefffff") == "a3b2def5"
