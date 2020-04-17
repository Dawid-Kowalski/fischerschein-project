from django.contrib import admin
from .models import HeaderPageTxt, MainPageTxt, QuestionPageTxt, Question

admin.site.register(HeaderPageTxt)
admin.site.register(MainPageTxt)
admin.site.register(QuestionPageTxt)
admin.site.register(Question)
