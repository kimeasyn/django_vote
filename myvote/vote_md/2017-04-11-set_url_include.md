#### django 투표앱 만들기



```
(app1env) PS D:\workspace\myvote> atom .
```

```python
#views.py
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, vote")
```

myvote/url.py 복사 후

myvote/vote/urls.py 생성후 복붙 후 수정

```python
#myvote/vote/urls.py
from django.conf.urls import url

from. import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
]
```



myvote/urls.py 수정

```python
#myvote/urls.py
from django.conf.urls import url,include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vote/', include('vote.urls'))					#vote/~는 vote.안에 urls.py로 처리
    #vote/$ 하면 vote/...뒤에 url이 먹히지 않음
]
```



