class Student:
    def Welcome(self):
        print("welcome home student")
        
        
    def Id(self):
        print("your id is ready")
        
        
class home(Student):
    def Name(self):
        print("my name is barmuat")
        
    def Age(self):
        print("23 years old")
        
        
s = home()
s.Welcome()
s.Id()
s.Name()
s.Age()