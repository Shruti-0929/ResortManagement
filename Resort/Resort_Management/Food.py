def breakfast():
    print("Menu:")
    print("1. Thepla ------- Rs 20 per item")
    print("2. Bread with Butter or Jam ------- Rs 30 per item")
    print("3. Khaman ------- Rs 45 per dish(6 pieces)")
    print("4. Bhakri ------- Rs 15 per item")
    print("5. Gathiya ------- Rs 100 per dish")
    print("6. Phaphda ------- Rs 100 per dish")
    print("7. Tea ----- Rs 10 per cup")
    print("8. Coffee ----- Rs 15 per cup")
    print("9. Milk ----- Rs 10 per cup")
    print("0. For no items!!!")
    poi = {"Thepla":20, 'Bread with Butter or Jam':30, 'Khaman':45, 'Bhakri':15, 'Gathiya':100, 'Phaphda':100, 'Tea':10, 'Coffee':15, 'Milk':10}
    print("Select Food Items!!!")
    item = []
    n = []
    amt = 0
    a = int(input("Enter item number : "))
    while a != 0:
        i = str(input("Enter Item Name : "))
        item.append(i)
        n_i = int(input("Enter number of item : "))
        n.append(n_i)
        a = int(input("Enter other item number : "))
    dic = {}
    for key in item:
        for value in n:
            dic[key] = value
            if key in poi:
                amt += dic[key] * poi[key]

            n.remove(value)
            break
    print(dic)
    return amt


def get_Breakfast_amt():
    amt = breakfast()
    print("Breakfast Amount : ", amt)
    print("------------------------------------------------")
    return amt


def lunch():
    print("Fixed Lunch ------- Rs 150 per Dish")
    print("Menu:")
    print("Roti(unlimited)")
    print("Kathawadi Sabji")
    print("Buttermilk(unlimited)")
    print("Salad")
    print("One Sweet")
    print("Papad")
    print("Achar")
    print("------------------------------------------------")
    n = int(input("Enter Number of Dishes : "))
    amt = 150*n
    return amt

def get_Lunch_amt():
    amt = lunch()
    print("Lunch Amount : ", amt)
    print("------------------------------------------------")
    return amt

def dinner():
    print("Fixed Lunch ------- Rs 150 per Dish")
    print("Menu:")
    print("Paratha/ Roti/ Bhakri")
    print("Special Kathawadi Sabji")
    print("Salad")
    print("Buttermilk(unlimited)")
    print("Papad")
    print("------------------------------------------------")
    n = int(input("Enter Number of Dishes : "))
    amt = 150 * n
    return amt

def get_Dinner_amt():
    amt = dinner()
    print("Dinner Amount : ", amt)
    print("------------------------------------------------")
    return amt

def snakes():
    print("1. French Fries ------ Rs 90 pre dish")
    print("2. Samosa ------ Rs 50 pre dish (3 items)")
    print("3. Sandwich ------ Rs 60 pre item")
    print("0. For no items!!!")
    poi = {"French Fries": 90, 'Samosa': 50, 'Sandwich': 60}
    print("Select Food Items!!!")
    item = []
    n = []
    amt = 0
    a = int(input("Enter item number : "))
    while a != 0:
        i = str(input("Enter Item Name : "))
        item.append(i)
        n_i = int(input("Enter number of item : "))
        n.append(n_i)
        a = int(input("Enter other item number : "))
    dic = {}
    for key in item:
        for value in n:
            dic[key] = value
            if key in poi:
                amt += dic[key] * poi[key]

            n.remove(value)
            break
    print(dic)
    return amt


def get_Snakes_amt():
    amt = snakes()
    print("Snakes Amount : ", amt)
    print("------------------------------------------------")
    return amt

