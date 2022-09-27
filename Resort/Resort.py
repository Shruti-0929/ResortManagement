from Resort_Management import About
from Resort_Management import Food
from Resort_Management import Room
from Resort_Management import General
from Resort_Management import Pool_And_Wellness

print("Information of Resort")
About.info()
print("\nRules of Resort")
General.rules()

class Total_Amt():

    def __init__(self):
        pass
    def Food_Total(self):
        pass
    def Room_Total(self):
        pass
    def Pool_and_Wellness_Total(self):
        pass


class Food_Amt(Total_Amt):
      def Food_Total(self):
          print("\nWelcome to the world of food")
          a = Food.get_Breakfast_amt()
          b = Food.get_Lunch_amt()
          c = Food.get_Dinner_amt()
          d = Food.get_Snakes_amt()
          total = a + b + c + d
          print("Total Food Bill : ", total)
          print("------------------------------------------------")
          return total

class Room_Amt(Total_Amt):

    def Room_Total(self):
        print("\nRoom Service of Resort")
        total = Room.Rooms()
        return total


class Pool_And_Wellness_Amt(Total_Amt):
    def Pool_and_Wellness_Total(self):
        print("Welcome to Cool Day Packages")
        total = Pool_And_Wellness.Package()
        return total





y = Room_Amt()
z = Pool_And_Wellness_Amt()
x = Food_Amt()

t1 = y.Room_Total()
t2 = z.Pool_and_Wellness_Total()
t3 = x.Food_Total()

total = t1+t2+t3
print("Total Bill : ", total)
