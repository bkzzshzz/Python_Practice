def number_in_words(num):
    number_words_0 = {
        "1" : "one",
        "2" : "two",
        "3" : "three",
    }
    number_words_1 = {
        "2" : "Twenty",
        "3" : "Thirty",
        "4" : "Forty"
    }
    digit = [0, 0]
    temp_num = num
    for i in range(2):
        digit[i] = str(temp_num % 10)
        print (digit[i])
        temp_num = temp_num // 10
    return str(number_words_1.get(digit[1])) + "" + str(number_words_0.get(digit[0]))



print(number_in_words(31))        
