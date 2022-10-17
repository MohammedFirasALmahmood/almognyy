from django.urls import path
from . import views
urlpatterns=[
    path('',views.Manage,name='manage'),
    path('add/',views.ADD,name='addstudent'),
    path('code/',views.GetCode,name='GetCode'),
    path('charge/',views.Charge,name='Charge')

]