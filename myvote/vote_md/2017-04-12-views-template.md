#### views, template 연동

url 을 views에 있는 메소드들과 연결시킬 것이다(function based view)

```python
#views.py
def results(request, question_id):		#투표결과 view
    response = "You're lokking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):			#투표 view
    return HttpResponse("You're voting on question %s" % question_id)

def detail(request, question_id):		#detail view
    response = "You're lokking at Question : %s"
    return HttpResponse(response % question_id)   
```

```python
#myvote/vote/urls.py	!= myvote/urls.py
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail")
    #Parameter로 숫자인 question_id를 받아서 views.detail 메소드로 전달
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name="results"),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
]
```

