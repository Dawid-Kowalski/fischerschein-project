from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page,name='main_page'),
    path('simple_question',views.simple_question,name='simple_question'),
    path('full_test',views.full_test,name='full_test'),
    path('fischerschein_info',views.fischerschein_info,name='fischerschein_info'),
    path('FAQ',views.FAQ,name='FAQ'),
    path('project_info',views.project_info,name='project_info'),
]