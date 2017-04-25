from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
# Create your tests here.

#shell에서 python manage.py test vote 명령으로 실행
class QuestionTest(TestCase):
    def test_was_published_recently_with_future(self):
        time = timezone.now() + datetime.timedelta(days = 7)
        fq = Question(pub_date = time)
        self.assertIs(fq.was_published_recently(), False)
