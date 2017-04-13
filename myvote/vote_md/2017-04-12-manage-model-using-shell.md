#### shell로 모델 조작하기 



```
(app1env) PS D:\workspace\myvote> python manage.py shell
>>> from vote.models import Question, Choice
>>> Question.objects.all()						# = select * from Question
```

```
>>> from django.utils import timezone
>>> q = Question(question_text = "최고의 고기는?", pub_date = timezone.now())
#insert 
#  into Question(question_text,pub_date) 
#         values("최고의 고기는", timezone.now())
>>> q
<Question: Question object>			#__string__을 overtiding 해줘야 함
>>> q.save()
>>> q.id							#select id from Question q
1
>>> q.question_text					#select question_text from Question q
'최고의 고기는?'
```

```python
#models.py
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
```

다시 Quesiton.objects.all() 하면 question_text가 잘 출력됨



Choice 객체는 Quesiton 객체에 연관되어진 객체라 c = Choice()로 생성할 수 없음

```
>>> from django.utils import timezone
>>> q = Question(question_text = "동물", pub_date = timezone.now())
>>> q.save()										#save()를 해야 객체 생성이 완료됨
>>> q.choice_set.create(choice_text = "pig")
>>> q.choice_set.all()								#생성된 choice 객체 다 나옴
```

