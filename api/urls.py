from django.urls import path
from . import views

urlpatterns=[
    path('PutStudent/<str:student_phone>',views.PutActivation),
    path('GetStudents/',views.GetStudents.as_view()),
    path('GetStudent/<str:student_phone>',views.GetStudent.as_view()),
    path('WGrammar/',views.mixins_WGrammar.as_view()),
    path('AGrammar1/',views.mixins_AGrammer1.as_view()),
    path('AGrammar4M/',views.mixins_AGrammar4M.as_view()),
    path('AGrammar4/<int:ExNo>',views.GetQuestions),

]