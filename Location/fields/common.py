
def separate_by_capital_letters(string):
    separated_set = []
    separated_string = ""
    last = "a"
    for char in string:
        if char == ' ' and last == ' ':
            continue
        if (char.isupper() and separated_string and (('z' >= last >= 'a') or last == ' ')) \
                or char == '.' or char == ',' or char == '-' or char == '(' or char == ')':
            if separated_string != '':
                separated_set.append(separated_string)
            separated_string = ""
        elif char.isupper() == 0 and last == ' ' and separated_string != '':
            separated_set.append(separated_string)
            separated_string = ""
        if char != '(' and char != ')' and char != '.' and char != ' ' and char != ',' and char != '-' and char != '(' and char != ')':
            separated_string += char
        last = char
    if separated_string:
        separated_set.append(separated_string)
    return separated_set
