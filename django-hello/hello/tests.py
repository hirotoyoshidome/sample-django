from django.test import TestCase
from .models import Question

class QuestionModelTests(TestCase):
    def test_str_with_question(self):
        exp = "test"
        question = Question(question_text=exp)
        self.assertIs(question.__str__(), exp)
