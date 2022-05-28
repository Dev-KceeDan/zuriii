from mimetypes import init
from unicodedata import name


class Student:
    name=str()
    age = int()
    tracks =list()
    score = float()
    
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
      self.name = name
      self.age = age
      self.tracks = tracks
      self.score = score
      
    def speak(self):
        print("This is ", self.name, " and he is ", self.age, " years old. He is in the ", self.tracks, " track and he scored ", self.score, ". What an excellent student.")

# new student details
    print("New Student Details")
    def change_name(self, new_name):
        self.name = new_name
        print("New name is ", self.name)
        
    def change_age(self, new_age):
        self.age = int(new_age)
        print("New age is ", self.age)
        
    def add_track(self, new_track):
        self.tracks = new_track
        print("New track name is ", self.tracks)
        
    def get_score(self):
        print("Student's score is ", self.score)
        
#example instance 
s = Student("Ray", 16,"Full time", "87%")
print(s.change_name("Bobby"))
print(s.change_age("25")) 
print(s.add_track("UI/UX")) 
print(s.get_score()) 



def get_score(self, new_score):
        print("Score: ", self.score)