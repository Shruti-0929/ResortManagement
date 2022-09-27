def service():
    print("  Double Bed")
    print("  Joint Cupboard")
    print("  Attached Bathroom")
    print("  T/V")
    print("  A/C")


def duplex():
    print("  1. A/C Room ----- Rs 4500.0 (One family - 4 members)")
    print("  2. Non A/C Room ----- Rs 3500.0 (One family - 4 members)")
    ask = int(input("Room Facility : "))
    l1 = [4500,3500]
    x = int(input("Number of Rooms : "))
    n = int(input("Number of Days : "))
    amt = x * n * l1[ask - 1]
    print("------------------------------------------------")
    print("Room Amount : ", amt)
    print("------------------------------------------------")
    return int(amt)

def single():
    print("  1. A/C Room ----- Rs 3500.0 (One family - 2 members)")
    print("  2. Non A/C Room ----- Rs 2500.0 (One family - 2 members)")
    ask = int(input("Room Facility : "))
    l1 = [3500, 2500]
    x = int(input("Number of Rooms : "))
    n = int(input("Number of Days : "))
    amt =  x * n * l1[ask - 1]
    print("------------------------------------------------")
    print("Room Amount : ", amt)
    print("------------------------------------------------")
    return int(amt)


def hall():
    print("  1. A/C Room ----- Rs 4000.0 (Group with 10 members)")
    print("  2. Non A/C Room ----- Rs 3000.0 (Group with 10 members)")
    ask = int(input("Room Facility : "))
    l1 = [4000, 3000]
    n = int(input("Number of Days : "))
    amt = n*l1[ask - 1]
    print("------------------------------------------------")
    print("Room Amount : ", amt)
    print("------------------------------------------------")
    return int(amt)


def Rooms():
    print("Which type of Room You want?")
    print('''1. Duplex
2. Single
3. Hall''')
    n = int(input("Enter Room type : "))
    if n == 1:
       a =  duplex()
       return int(a)
    elif n == 2:
        b = single()
        return int(b)
    else:
        c = hall()
        return int(c)


