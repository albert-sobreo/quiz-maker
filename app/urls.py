from django.urls import path, include
from app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home,),
    path('createquizprocess/', views.createquizprocess),
    path('quizmaker/', views.quizmaker),
    path('selectquiz/<int:quizKey>', views.selectquiz),
    path('deletequiz/<int:quizKey>', views.deletequiz),
]