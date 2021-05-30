zeroth_base = {
    "0" : " ",
    "1" : "One",
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
    "8" : "Eighty",
    "9" : "Ninety"
}

num = input("A number: ")
#laughed here -the length of num lol

if len(num) == 2:
    if int(num) < 20:
        print(zeroth_base.get(num))
    else:
        print(first_base.get(num[0]) + " " + zeroth_base.get(num[1]))
elif len(num) == 3:
    if int(num[1] + num[2]) < 20:
        if int(num[1] + num[2]) > 9:
            print(zeroth_base.get(num[0]) + " Hundred " + zeroth_base.get(num[1] + num[2]))
        elif int(num[1] + num[2]) > 0:
            print(zeroth_base.get(num[0]) + " Hundred " + zeroth_base.get(num[2]))
        else:
            print(zeroth_base.get(num[0]) + " Hundred")
    else:
        print(zeroth_base.get(num[0]) + " Hundred " + first_base.get(num[1]) + " " + zeroth_base.get(num[2]))
elif len(num) == 4:
    if int(num[1] + num[2] + num[3]) < 100:
        if int(num[2] + num[3]) > 19:
            
            print(zeroth_base.get(num[0]) + " Thousand " + first_base.get(num[2]) + " " + zeroth_base.get(num[3]))
        elif int(num[2] + num[3]) > 9:
            
            print(zeroth_base.get(num[0]) + " Thousand " + zeroth_base.get(num[2] + num[3]))
        elif int(num[2] + num[3]) > 0: 
            print(zeroth_base.get(num[0]) + " Thousand " + zeroth_base.get(num[3]))
        else:
            print(zeroth_base.get(num[0]) + " Thousand")
        
            
    elif int(num[2] + num[3]) > 19:
        print(zeroth_base.get(num[0]) + " Thousand " + zeroth_base.get(num[1]) + " Hundred " + first_base.get(num[2]) + " " + zeroth_base.get(num[3]))
    elif int(num[2] + num[3]) > 9:
        print(zeroth_base.get(num[0]) + " Thousand " + zeroth_base.get(num[1]) + " Hundred " + zeroth_base.get(num[2] + num[3]))
    elif int(num[2] + num[3]) > 0:
        print(zeroth_base.get(num[0]) + " Thousand " + zeroth_base.get(num[3]))
    else:
        print (zeroth_base.get(num[0]) + " Thousand " + zeroth_base.get(num[1]) + " Hundred")
    
    
    


