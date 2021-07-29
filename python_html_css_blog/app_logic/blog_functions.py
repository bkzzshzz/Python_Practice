def valid_name(name):

    result = ""

    for each_letter in name:
        if each_letter == "+" or each_letter.isalpha():
            result =  True
        else:    
            result = False
            break

    return result


def proper_name(name):

    words_in_name = name.split("+")
    temp_name = []

    for each_word in words_in_name:

        if each_word != "":
            temp_name.append(each_word)

    words_in_name = temp_name.copy()
    temp_name = []

    for each_word in words_in_name:
        temp_word = each_word.lower()
        temp_word = temp_word[0].upper() + temp_word[1:]
        temp_name.append(temp_word)

    words_in_name = temp_name.copy()

    return " ".join(words_in_name)


def email_okay(email, variable):

    if email not in variable:
        return True


def password_match(password, re_password):

    if password == re_password:
        return True
    else:
        return False
