from django.urls import path
from . import views

urlpatterns=[
    path('Students/',views.GetStudent),
    path('Student/<int:number>',views.PutActivation),
]