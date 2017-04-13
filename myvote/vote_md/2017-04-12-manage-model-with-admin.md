#### admin page로 data model 조작하기

```
(app1env) PS D:\workspace\myvote> python manage.py createsuperuser
#id/mail/pw입력
```

 http://127.0.0.1:8000/admin 접속 후 로그인

```python
#admin.py
#Question,choice 객체 admin에 등록
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
```



admin 페이지 새로고침(다시시작) 하면 admin페이지에 quesiton,choice 모델이 등록되어있는걸 볼 수 있다.

admin 페이지에서 question 객체 추가 및 각 question 마다 choice 객체를 추가한다.

