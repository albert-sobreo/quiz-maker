from django.shortcuts import render, HttpResponse, render_to_response, redirect
from app.models import Quiz_Event, Quiz_Section, Quiz_Question, Quiz_Choices, Quiz_Answer
import datetime

# Create your views here.
def home(request):
    context = {
        "quizzes": Quiz_Event.objects.all()
    }
    return render(request, "index.html", context)

def createquizprocess(request):
    quiz_name = request.POST['quiz_name']
    deadline = datetime.datetime.strptime(request.POST['deadline'].replace('T', " "), '%Y-%m-%d %H:%M')
    date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M")

    quiz_event = Quiz_Event()

    quiz_event.quiz_name = quiz_name
    quiz_event.date = date
    quiz_event.deadline = deadline
    quiz_event.save()

    request.session['quizKey'] = quiz_event.pk
    return redirect('/quizmaker/')

def quizmaker(request):
    context = {
        'quiz': Quiz_Event.objects.get(pk=request.session.get('quizKey'))
    }
    
    return render(request, "quizmaker.html", context)

def selectquiz(request, quizKey):
    request.session["quizKey"] = quizKey
    return redirect('/quizmaker/')

def deletequiz(request, quizKey):
    Quiz_Event.objects.filter(pk=quizKey).delete()
    return redirect('/')