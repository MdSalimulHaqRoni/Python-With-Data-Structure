def method_name(a, b):
    print("Its a method")
class person:
    def __init__(self, person_name,date_of_birth,height):
        self.name= person_name
        self.date_of_birth = date_of_birth
        self.height = height
    def get_name(self):
        return self.name
    def set_name(self, new_name):
        self.name = new_name
    def get_summary(self):
        return f"Name: {self.name},Birth_date: {self.date_of_birth}, height: {self.height}"
a_person = person("Roni", "1997", "5 feet 8 inch")
print(a_person.get_summary())
a_person.set_name("Md Salimul Haq Roni")
print(a_person.get_summary())
print(a_person.date_of_birth)