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

def savequiz(request):
    qe_id = request.session.get("quizKey")
    quizEvent = Quiz_Event.objects.get(pk=qe_id)

    ppi = {}
    qt = {}
    tA = {}
    ch = {}
    se = {}

    for key, val in request.POST.items():
        if 'ppi-section' in key:
            ppi[key[-1]] = val

        elif 'qt-section' in key:
            qt[key[-1]] = val

        elif 'tArea' in key:
            tA[key[-2] + key[-1]] = val

        elif 'ch' in key:
            ch[key[-3] + key[-2] + key[-1]] = val

        elif 'select' in key:
            se[key[-2] + key[-1]] = val

    for key, val in se.items():
        globals()['answer_{}'.format(key)] = Quiz_Answer()
        globals()['answer_{}'.format(key)].quiz_answer = val
        globals()['answer_{}'.format(key)].save()

    for key, val in ch.items():
        globals()['ch_{}'.format(key)] = Quiz_Choices()
        globals()['ch_{}'.format(key)].choice = val
        globals()['ch_{}'.format(key)].save()

    for key, val in tA.items():
        globals()['question_{}'.format(key)] = Quiz_Question()
        globals()['question_{}'.format(key)].question = val

        globals()['question_{}'.format(key)].quiz_answer = globals()['answer_{}'.format(key)]

        k = ''
        j = ''
        
        globals()['question_{}'.format(key)].save()
        for k, j in globals().items():
            if "ch_{}".format(key) in k:
                print(globals()['{}'.format(k)])
                globals()['question_{}'.format(key)].quiz_choices.add(globals()['{}'.format(k)])

        globals()['question_{}'.format(key)].save()

    for key, val in ppi.items():
        globals()['section_{}'.format(key)] = Quiz_Section()
        globals()['section_{}'.format(key)].points_per_item = val
        globals()['section_{}'.format(key)].save()

        for k, j in globals().items():
            if "question_{}".format(key) in k:
                globals()['section_{}'.format(key)].quiz_question.add(globals()['{}'.format(k)])

        globals()['section_{}'.format(key)].save()

    for key, val in qt.items():
        globals()['section_{}'.format(key)].quiz_type = val
        globals()['section_{}'.format(key)].save()

    for key, val in ppi.items():
        quizEvent.quiz_section.add(globals()['section_{}'.format(key)])
        quizEvent.save()

    return redirect('/')

def editquiz(request):
    pass