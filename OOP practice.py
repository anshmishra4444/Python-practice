class Programmer:
    company = "Microsoft"
    def __init__(self,name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
harry = Programmer("Virat", "Skype")
Alka = Programmer("Alka", "GitHub")
harry.getInfo()
Alka.getInfo()

class Calculator:
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} square root is {self.number **0.5}")
    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")
    @staticmethod
    def greet():
        print("*******Hello there welcome to the best calculator of the world*******")



a=Calculator(9)
a.greet()
a.cube()
a.square()
a.squareRoot()

class Sample:
    a = "Virat"

obj = Sample()
obj.a = "Vikky"
# Sample.a = "Vikky"
print(Sample.a)
print(obj.a)


class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
    def fareInfo(self):
        print(f"The price of the ticket is Rs {self.fare}")
    def bookTicket(self):
            if(self.seats>0):
                print(f"Your ticket has been booked! Your seat number is {self.seats}")
                self.seats = self.seats -1
            else:
                print("Sorry this train is full! Kindly try in tatkal")
intercity = Train("Intercity Express: 14015", 90, 2)
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()

class Sample:

    def __init__(slf,name):
        slf.name = name

obj = Sample("Virat")
print(obj.name)

