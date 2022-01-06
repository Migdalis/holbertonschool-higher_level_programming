#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    int_number = 0
    if (type(roman_string) != str) or (roman_string is None):
        return 0
    if len(roman_string) == 1:
        return (roman_dic.get(roman_string))
    x = 0
    while x < len(roman_string):
        if roman_string[x] in roman_dic:
            if x < len(roman_string) - 1:
                current = roman_dic.get(roman_string[x])
                next = roman_dic.get(roman_string[x + 1])
                if current < next:
                    int_number += (next - current)
                    x += 2
                    continue
            int_number += roman_dic.get(roman_string[x])
            x += 1
        else:
            break
    return (int_number)
