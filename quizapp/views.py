from django.shortcuts import render
from .models import HeaderPageTxt

def main_page(request):
    header_txt = HeaderPageTxt.objects.all()[:1]
    header_data = {}
    header_data['menu_simple_question_txt_de'] = header_txt[0].menu_simple_question_txt_de
    header_data['menu_simple_question_txt_pl'] = header_txt[0].menu_simple_question_txt_pl
    header_data['menu_full_test_txt_de'] = header_txt[0].menu_full_test_txt_de
    header_data['menu_full_test_txt_pl'] = header_txt[0].menu_full_test_txt_pl
    header_data['menu_fischerschein_info_txt_de'] = header_txt[0].menu_fischerschein_info_txt_de
    header_data['menu_fischerschein_info_txt_pl'] = header_txt[0].menu_fischerschein_info_txt_pl
    header_data['menu_FAQ_txt_de'] = header_txt[0].menu_FAQ_txt_de
    header_data['menu_FAQ_txt_pl'] = header_txt[0].menu_FAQ_txt_pl
    header_data['menu_about_project_de'] = header_txt[0].menu_about_project_de
    header_data['menu_about_project_pl'] = header_txt[0].menu_about_project_pl
    header_data['hero_main_txt_de'] = header_txt[0].hero_main_txt_de
    header_data['hero_main_txt_pl'] = header_txt[0].hero_main_txt_pl
    header_data['hero_under_txt_de'] = header_txt[0].hero_under_txt_de
    header_data['hero_under_txt_pl'] = header_txt[0].hero_under_txt_pl
    return render(request,'quizapp/main_page.html',header_data)