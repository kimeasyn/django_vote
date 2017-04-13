#### 모델 만들기

question, choice 2개

Django는 ORM형식으로 db를 다룬다

> ORM(Object relational mapping) : sql문을 작성하지 않고 model이 db에 저장하는 형식

```python
#myvote/vote/model.py
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    #fk로 묶인 객체가 삭제되었을시 연동하여 삭제
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
```

```l
PS D:\workspace> .\python-env\app1env\Scripts\activate.ps1
(app1env) PS D:\workspace> cd myvote
(app1env) PS D:\workspace\myvote> python manage.py makemigrations	#모델 생성
(app1env) PS D:\workspace\myvote> python manage.py migrate			#
(app1env) PS D:\workspace\myvote> python manage.py sqlmigrate vote 0001
#vote app에서 0001번째로 실행한 sql문을 볼 수가 있음
```

