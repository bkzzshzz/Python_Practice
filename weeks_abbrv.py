def week_abbrv(day):
    all_days = {
        "Sunday" : "Sun",
        "Monday" : "Mon",
        "Tuesday" : "Tue",
        "Wednesday" : "Wed",
        "Thursday" : "Thu",
        "Friday" : "Fri",
        "Saturday" : "Sat"
    }
    print(all_days.get(day))

week_abbrv(input("Give a day: "))