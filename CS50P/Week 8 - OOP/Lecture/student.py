class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.partonus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house, "partonus")
    
    # Getter
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    # Getter
    @property # This is how you define a getter
    def house(self):
        return self._house
    
    # Setter
    @house.setter # This is how you define a setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff", ""]:
            raise ValueError("Invalid House")
        self._house = house
    
    def charm(self):
        match self.partonus:
            case "Stag":
                return "Neigh im a horse"
            case "Dog":
                return "Bark im a dog"
            case _:
                return "No patronus"




def main():
    student = Student.get()
    
    print(student)


# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

    # If inside parentheses it will return a tuple (tuples are similar to lists but are immutable)
    # return (name, house)

if __name__ == "__main__":
    main()
