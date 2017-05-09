from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse
# Create your tests here.

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days = days)
    return Question.objects.create(question_text=question_text,pub_date = time)

class QuestionViewTests(TestCase):
    def test_index_view_with_future_question(self):
        create_question(question_text='Future question', days = 30)
        response = self.client.get(reverse('vote:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

#shell에서 python manage.py test vote 명령으로 실행
class QuestionTest(TestCase):
    def test_was_published_recently_with_future(self):
        time = timezone.now() + datetime.timedelta(days = 7)
        fq = Question(pub_date = time)
        self.assertIs(fq.was_published_recently(), False)
