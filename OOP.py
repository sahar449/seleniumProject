
# בנינו מחלקה
class Dog:
    dogsCounter = 0  # משתנה של המחלקה, יהיה רק אחד כזה בלבדלכל העצמים ביחד

#בנאי של המחלקה והגדרת מאפייני המחלקה
    def __init__(self, color, weight, name="Default"):
        self.dogColor = color
        self.weight = weight
        self.name = name
        print("In Constructor")
        Dog.dogsCounter += 1  # dogsCounter = dogsCounter+ 1

# לקבל צבע
    def getColor(self):
        return self.dogColor
# להגדיר צבע
    def setColor(self, color):
        self.dogColor = color

    def getWeight(self):
        return self.weight

    def setWeight(self, weight):
        self.weight = weight

    def getName(self):
        return self.name

    def setName(self, Name):
        self.Name = Name
# בניית פונקציה ללא גט וסט
    def bark(self):
        print("Dog ", self.name, " is barking")

    @classmethod
    def printDogsAmount(cls):
        print("Amount of dogs: ", cls.dogsCounter)

# יצירת העצם, השמה למאפייני הכלב
dog = Dog("White", 50)
print(dog.getColor())
dog.setColor("Red")
print(dog.getColor())
print(dog.getWeight())
print(dog.name)
dog.bark()

dog2 = Dog("Black", 20, "My Dog")
dog3 =Dog("Gsfgsfg", 10, "Gfg")

Dog.printDogsAmount()

#-------

class Person:

    def __init__(self,high,weight,name):
        self.high = high
        self.weight = weight
        self.name = name

    def calcBmi (self):
        return self.weight/self.high**2


#יצרתי עצמים
person1 = Person(1.80,80,"Moshe")
person2 = Person(1.40,80,"Jakob")

# בהדפסה שם העצם נקודה הפונקציה
print("your bmi is : ", person1.calcBmi())
print("your bmi is : ", person2.calcBmi())
