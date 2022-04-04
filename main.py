def count_vowels(text):
    count = 0
    if type(text) == int:
        return 42
    else:
        for item in string:
            vowel = set("aeiouAEIOU")
            if item in vowel:
                count = count + 1
        if count > 0:
            print("The number of vowels is: ")
            return count


string = "ktdaarUU"
print(count_vowels(string))


# 2

def hamming(text1, text2):
    if len(text1) != len(text2):
        return 0
    else:
        count = 0
        l = len(text1)
        for i in range(l):
            if text1[i] != text2[i]:
                count = count + 1
        return count


string1 = 'cat'
string2 = 'atc'
print(hamming(string1, string2))


# 3

class Vehicle:  # abstract class = blueprint for other cl.

    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

    def print_color(self):
        print(self.color)

    def print_fuel_type(self):
        print(self.fuel_type)


class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)   # calls constructor of mother
        self.doors = doors

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Doors: {2}".format(self.color, self.fuel_type, self.doors)

    def print_doors(self):
        print(self.doors)


class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return "Color: {0}, Fuel Type: {1}, Passengers: {2}".format(self.color, self.fuel_type, self.passengers)

    def print_passengers(self):
        print(self.passengers)


v = Vehicle('red', 'gas')
c = Car('green', 'electricity', 4)
b = Bus('yellow', 'diesel', 33)

print(c.__str__())
print(b.__str__())


# 4

class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):  # overriding the __str__ function for a custom string representation of the object
        return "{0}, {1}".format(self.name, self.author)


book1 = Book('Dune', 'Frank Herbert')
print(book1)

# 5



