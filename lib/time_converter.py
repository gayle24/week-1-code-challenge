def time_converter(hour, min, period):
    if period == "am":
        if min < 60 and min >=0:
            if hour == 12:
                hour = 0 
        else:
            print("Invalid input of minutes")
    elif period == "pm":
        if min < 60 and min >=0:
            if hour != 12:
                hour += 12
            elif hour == 12:
                hour = 0
        else:
            print("Invalid input of minutes")
    else:
        return False
    return f"{hour:02d}{min:02d}"


# Example usage
hour = 8
min = 30
period = "am"
result = time_converter(hour, min, period)
print(result)
