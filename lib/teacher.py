import random
from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
       
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
       
        if not self.knowledge:
            return "The teacher has no knowledge to teach."
        return random.choice(self.knowledge)

    def add_knowledge(self, knowledge):
      
        self.knowledge.append(knowledge)
