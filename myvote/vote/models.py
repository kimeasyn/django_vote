from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        #날짜가 최신일때만 true return
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
                                #오늘          -  하루

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    #fk로 묶인 객체가 삭제되었을시 연동하여 삭제
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text