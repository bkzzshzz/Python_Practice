def convert_1_digit_to_word(n):
    ones_place_words = {
        "0": "ZERO",
        "1": "ONE",
        "2": "TWO",
        "3": "THREE",
        "4": "FOUR",
        "5": "FIVE",
        "6": "SIX",
        "7": "SEVEN",
        "8": "EIGHT",
        "9": "NINE",
    }
    return ones_place_words[n]

def convert_2_digits_to_word(n):
    tens_digit_words = {
        "0": "",
        "2": "TWENTY",
        "3": "THIRTY",
        "4": "FORTY",
        "5": "FIFTY",
        "6": "SIXTY",
        "7": "SEVENTY",
        "8": "EIGHTY",
        "9": "NINETY",
    }

    ten_based_words = {
        "0": "TEN",
        "1": "ELEVEN",
        "2": "TWELVE",
        "3": "THIRTEEN",
        "4": "FOURTEEN",
        "5": "FIFTEEN",
        "6": "SIXTEEN",
        "7": "SEVENTEEN",
        "8": "EIGHTEEN",
        "9": "NINETEEN"
    }

    if len(n)<2:
        n = '0' + n

    if n[0] == '1':
        num_in_words = ten_based_words[n[1]]
    else:
        num_in_words = convert_1_digit_to_word(n[1])
        if num_in_words == "ZERO":
            num_in_words = ""
        num_in_words = tens_digit_words[n[0]] + num_in_words

    if num_in_words == "":
        num_in_words = "ZERO"

    return num_in_words

def convert_any_digit_number_to_word(number):

    place_value_words = ["ONES", "TENS", "HUNDRED", "THOUSAND", "LAKH", "CRORE", "ARAB", "KHARAB"]

    if len(number) < 3:
        return convert_2_digits_to_word(number)
    else:
        num_in_words = convert_2_digits_to_word(number[-2:])
        if num_in_words == "ZERO":
            num_in_words = ""
        this_block = '0' + number[-3]
        
        number = number[0:-3]
        place = 2 # Corresponding to HUNDRED in place value

        while place < len(place_value_words) and this_block != "":
            this_block_in_words = convert_2_digits_to_word(this_block)

            if this_block_in_words != "ZERO":
                num_in_words = this_block_in_words + " " + place_value_words[place] + " " + num_in_words
            
            place += 1
            if len(number)>=2:
                this_block = number[-2:]
                number = number[:-2]
            else:
                this_block = number
                number = ""

    if num_in_words == "":
        num_in_words = "ZERO"
    
    return num_in_words


n = input("Enter a number: ")
print (convert_any_digit_number_to_word(n))