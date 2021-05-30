zeroth_base = {
    "1" : "one",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "10" : "Ten",
    "11" : "Eleven",
    "12" : "Twelve",
    "13" : "Thirteen",
    "14" : "Fourteen",
    "15" : "Fifteen", 
    "16" : "Sixteen",
    "17" : "Seventeen",
    "18" : "Eighteen",
    "19" : "Nineteen"
}

first_base = {
    "2" : "Twenty",
    "3" : "Thirty",
    "4" : "Forty",
    "5" : "Fifty",
    "6" : "Sixty",
    "7" : "Seventy",
    "8" : "Eight",
    "9" : "Ninety"
}

num = input("A number: ")
if int(num) < 20:
    print(zeroth_base.get(num))
elif (int(num) % 10) == 0:
    print(first_base.get(num[0]))
else:
    print(first_base.get(num[0]) + " " + zeroth_base.get(num[1]))
