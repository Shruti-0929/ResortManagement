def fullday():
    print("Full day package for adult Rs 750")
    print("Full day package for children between 4 - 12 years Rs 400")
    print("Full day package for children smaller than 4 years are free")
    a = int(input("Number of adult : "))
    c = int(input("Number of children (age between 4 - 12 years) : "))
    amt = a * 750 + c * 400
    print("------------------------------------------------")
    print("Pool_&_Wellness Amount : ", amt)
    print("------------------------------------------------")
    return amt

def halfday():
    print("Half day package for adult Rs 400")
    print("Half day package for children between 4 - 12 years Rs 200")
    print("Half day package for children smaller than 4 years are free")
    a = int(input("Number of adult : "))
    c = int(input("Number of children (age between 4 - 12 years) : "))
    amt = a * 400 + c * 200
    print("------------------------------------------------")
    print("Pool_&_Wellness Amount : ", amt)
    print("------------------------------------------------")
    return amt

def Package():
    print("Select Package : ")
    print('''1. Full Day
2. Half Day''')
    s = int(input("Enter Package Type : "))
    if s == 1:
        f = fullday()
        return int(f)
    else:
        h = halfday()
        return int(h)

