'''
HW-
Q1- Define three classes out of which first class should take 3 numbers, second class should print the largest number and third one should display smallest num
'''
class Class:
  def __init__(self,num1,num2,num3):
    self.num1 = num1
    self.num2 = num2
    self.num3 = num3
  def display(self):
    print("Number 1 is:",self.num1)
    print("Number 2 is:",self.num2)
    print("Number 3 is:",self.num3)
  

class Largest(Class):
  def __init__(self,num1,num2,num3):
    Class.__init__(self,num1,num2,num3)

  def compare(self):
    if (self.num1 > self.num2 and self.num1 > self.num3):
      print(self.num1,"is the largest number.")
    elif (self.num2 > self.num3 and self.num2 > self.num1):
      print(self.num2,"is the largest number.")
    elif (self.num3 > self.num1 and self.num3 > self.num2):
      print(self.num3,"is the largest number.")
    else:
      print("HUH")

class Smallest(Class):
  def __init__(self,num1,num2,num3):
    Class.__init__(self,num1,num2,num3)

  def compare2(self):
    if (self.num1 < self.num2 and self.num1 < self.num3):
      print(self.num1,"is the smallest number.")
    elif (self.num2 < self.num3 and self.num2 < self.num1):
      print(self.num2,"is the smallest number.")
    elif (self.num3 < self.num1 and self.num3 < self.num2):
      print(self.num3,"is the smallest number.")
    else:
      print("HUH")

a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
c = int(input("Enter number 3:"))

obj = Largest(a,b,c)
obj2 = Smallest(a,b,c)
obj.compare()
obj2.compare2()





