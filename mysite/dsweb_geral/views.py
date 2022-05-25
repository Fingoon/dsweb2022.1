from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Question, Choice

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('dsweb_geral/index.html')
    context = {'latest_question_list': latest_question_list}
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    template = loader.get_template('dsweb_geral/detail.html')
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return HttpResponse(template.render({'question':question},request))
'''

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'dsweb_geral/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'dsweb_geral/detail.html',{'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'dsweb_geral/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        id_choice = request.POST['choice']
        selected_choice = question.choice_set.get(pk=id_choice)
    except (KeyError, Choice.DoesNotExist):
        contexto = {'question':question, 'error_message':"Você não selecionou uma opção"}
        return render(request,'dsweb_geral/detail.html', contexto)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results',args=(question_id,)))

