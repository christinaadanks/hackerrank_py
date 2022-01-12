def time_conversion(s):
    arr = s.split(":")
    if "PM" in arr[2]:
        arr[2] = arr[2].replace("PM", "")
        if arr[0] == "12":
            time = arr[0] + ":" + arr[1] + ":" + arr[2]
        else:
            hour = int(arr[0])
            hour += 12
            arr[0] = str(hour)
            time = arr[0] + ":" + arr[1] + ":" + arr[2]
    if "AM" in arr[2]:
        arr[2] = arr[2].replace("AM", "")
        if arr[0] == "12":
            time = "00:" + arr[1] + ":" + arr[2]
        else:
            time = arr[0] + ":" + arr[1] + ":" + arr[2]
    return time


if __name__ == '__main__':
    s = "07:05:45PM"
    print(time_conversion(s))
    t = "12:38:29AM"
    print(time_conversion(t))
