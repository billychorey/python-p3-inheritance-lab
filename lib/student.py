# student.py

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        """
        Initialize a Student object.
        """
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, subject):
        """
        Learn a new subject and add it to the knowledge list.
        """
        self.knowledge.append(subject)
