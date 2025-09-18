def get_day_name(num):
    days={
        
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(num,"Invalid Day")

print(get_day_name(3))
print(get_day_name(10))