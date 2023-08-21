from models.base_model import BaseModel


class Question(BaseModel):
    def __init__(self, question_prompt="", question_name="", question_options=[], question_answer=""):
        self.question_prompt = question_prompt
        self.question_name = question_name
        self.question_options = question_options
        self.question_answer = question_answer
