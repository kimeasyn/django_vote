from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from .models     import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #orderby 안에 - 를 붙이면 desc 내림차순으로 정렬함
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'vote/index.html', context)

def results(request, question_id):
    response = "You're lokking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'vote/detail.html', {'question': question})
