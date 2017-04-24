from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse
from .models     import Question
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'vote/index.html'
    context_object_name = 'latest_question_list' #parameter로 넘길 값 지정

    def get_queryset(self):     #overiding
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'vote/detail.html'

class ResultsView(generic.DeleteView):
    model = Question
    template_name = 'vote/results.html'

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #orderby 안에 - 를 붙이면 desc 내림차순으로 정렬함
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'vote/index.html', context)

#def results(request, question_id):
#    question = get_object_or_404(Question, pk = question_id)
#    return render(request, 'vote/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
        #input type = "submit"의 name의 value를 가지고 옴
    except:
        return render(request, 'vote/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect('vote:results', pk = question.id )
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk = question_id)
#    return render(request, 'vote/detail.html', {'question': question})
