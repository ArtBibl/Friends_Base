def size_table(data, head_main):
    head_size = []
    for word in head_main:
        count = 0
        for i in word:
            count += 1
        head_size.append(count)
    count_column = 0
    for i in data:
        count_column = (len(i) - 1)
        break
    count_let = 0
    length = 0
    for i in str(data):
        # if i == '[' or i == '(' or i == ')' or i == ']' or i == ',' or i == "'":
        #     continue
        if i == ' ':
            number = head_size
            if number[length] < count_let:
                number.insert(length, count_let)
                number.pop(length + 1)
            count_let = 0
            length += 1
            if length > count_column:
                length = 0
        else:
            count_let += 1
    return number


def write_head(size, words):
    head_string = ""
    number_words = 0
    head_string += "| "
    for word in words:
        length = 0
        for e in str(word):
            if e == '[' or e == '(' or e == ')' or e == ']' or e == ',' or e == "'":
                continue
            else:
                head_string += e
                length += 1
        while length < size[number_words]:
            head_string += " "
            length += 1
        number_words += 1
        head_string += " | "
    print(head_string)
    return head_string


def table_for_friends(data, head_main):
    # head_main = ('Name:', 'Second name:', 'Phone number:', 'Age:')
    size_of_table = size_table(data, head_main)
    count_column = 0
    for i in data:
        count_column = (len(i) - 1)
    big_length = 0
    for i in size_of_table:
        big_length += i
    big_length = big_length + ((count_column + 1) * 3) + 1
    total_friends = 0
    print("\n")
    print('-' * big_length)
    write_head(size_of_table, head_main)
    print('-' * big_length)
    for row in data:
        write_head(size_of_table, row)
        total_friends += 1
    print('-' * big_length, "\n")
    print("Totally you have a lot of friends:", total_friends)
