from django.http import HttpResponseRedirect
#from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

#def hello(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    #template = loader.get_template('hello/hello.html')
#    context = {
#            'latest_question_list': latest_question_list,
#    }
#    #return HttpResponse(template.render(context, request))
#    return render(request, 'hello/hello.html', context)
class HelloView(generic.ListView):
    template_name = 'hello/hello.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'hello/detail.html', {'question': question})
class DetailView(generic.DetailView):
    model = Question
    template_name = 'hello/detail.html'

#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'hello/results.html', {'question': question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'hello/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'hello/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice .",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('hello:results', args=(question.id,)))


