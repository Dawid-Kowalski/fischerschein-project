from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page,name='main_page'),
    path('simple_question',views.simple_question,name='simple_question'),
    path('full_test',views.full_test,name='full_test'),
]