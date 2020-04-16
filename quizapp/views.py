from django.shortcuts import render
from .models import HeaderPageTxt, MainPageTxt

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

def main_page(request):

    main_page_txt = MainPageTxt.objects.all()[:1]
    main_page_data = {}

    main_page_data['main_page_without_account_title_txt_de'] = main_page_txt[0].main_page_without_account_title_txt_de
    main_page_data['main_page_without_account_title_txt_pl'] = main_page_txt[0].main_page_without_account_title_txt_pl
    main_page_data['main_page_without_account_benefit_1_txt_de'] = main_page_txt[0].main_page_without_account_benefit_1_txt_de
    main_page_data['main_page_without_account_benefit_1_txt_pl'] = main_page_txt[0].main_page_without_account_benefit_1_txt_pl
    main_page_data['main_page_without_account_benefit_2_txt_de'] = main_page_txt[0].main_page_without_account_benefit_2_txt_de
    main_page_data['main_page_without_account_benefit_2_txt_pl'] = main_page_txt[0].main_page_without_account_benefit_2_txt_pl
    main_page_data['main_page_without_account_benefit_3_txt_de'] = main_page_txt[0].main_page_without_account_benefit_3_txt_de
    main_page_data['main_page_without_account_benefit_3_txt_pl'] = main_page_txt[0].main_page_without_account_benefit_3_txt_pl
    main_page_data['main_page_with_account_title_txt_de'] = main_page_txt[0].main_page_with_account_title_txt_de
    main_page_data['main_page_with_account_title_txt_pl'] = main_page_txt[0].main_page_with_account_title_txt_pl
    main_page_data['main_page_with_account_benefit_1_txt_de'] = main_page_txt[0].main_page_with_account_benefit_1_txt_de
    main_page_data['main_page_with_account_benefit_1_txt_pl'] = main_page_txt[0].main_page_with_account_benefit_1_txt_pl
    main_page_data['main_page_with_account_benefit_2_txt_de'] = main_page_txt[0].main_page_with_account_benefit_2_txt_de
    main_page_data['main_page_with_account_benefit_2_txt_pl'] = main_page_txt[0].main_page_with_account_benefit_2_txt_pl
    main_page_data['main_page_with_account_benefit_3_txt_de'] = main_page_txt[0].main_page_with_account_benefit_3_txt_de
    main_page_data['main_page_with_account_benefit_3_txt_pl'] = main_page_txt[0].main_page_with_account_benefit_3_txt_pl
    main_page_data['main_page_with_account_benefit_4_txt_de'] = main_page_txt[0].main_page_with_account_benefit_4_txt_de
    main_page_data['main_page_with_account_benefit_4_txt_pl'] = main_page_txt[0].main_page_with_account_benefit_4_txt_pl
    main_page_data['main_page_with_account_benefit_5_txt_de'] = main_page_txt[0].main_page_with_account_benefit_5_txt_de
    main_page_data['main_page_with_account_benefit_5_txt_pl'] = main_page_txt[0].main_page_with_account_benefit_5_txt_pl
    main_page_data['main_page_without_account_single_question_btn_txt_de'] = main_page_txt[0].main_page_without_account_single_question_btn_txt_de
    main_page_data['main_page_without_account_single_question_btn_txt_pl'] = main_page_txt[0].main_page_without_account_single_question_btn_txt_pl
    main_page_data['main_page_without_account_full_test_btn_txt_de'] = main_page_txt[0].main_page_without_account_full_test_btn_txt_de
    main_page_data['main_page_without_account_full_test_btn_txt_pl'] = main_page_txt[0].main_page_without_account_full_test_btn_txt_pl
    main_page_data['main_page_with_account_make_account_btn_txt_de'] = main_page_txt[0].main_page_with_account_make_account_btn_txt_de
    main_page_data['main_page_with_account_make_account_btn_txt_pl'] = main_page_txt[0].main_page_with_account_make_account_btn_txt_pl
    main_page_data['main_page_with_account_login_btn_txt_de'] = main_page_txt[0].main_page_with_account_login_btn_txt_de
    main_page_data['main_page_with_account_login_btn_txt_pl'] = main_page_txt[0].main_page_with_account_login_btn_txt_pl
    main_page_data['main_page_benefit_1_main_txt_de'] = main_page_txt[0].main_page_benefit_1_main_txt_de
    main_page_data['main_page_benefit_1_main_txt_pl'] = main_page_txt[0].main_page_benefit_1_main_txt_pl
    main_page_data['main_page_benefit_1_under_txt_de'] = main_page_txt[0].main_page_benefit_1_under_txt_de
    main_page_data['main_page_benefit_1_under_txt_pl'] = main_page_txt[0].main_page_benefit_1_under_txt_pl
    main_page_data['main_page_benefit_2_main_txt_de'] = main_page_txt[0].main_page_benefit_2_main_txt_de
    main_page_data['main_page_benefit_2_main_txt_pl'] = main_page_txt[0].main_page_benefit_2_main_txt_pl
    main_page_data['main_page_benefit_2_under_txt_de'] = main_page_txt[0].main_page_benefit_2_under_txt_de
    main_page_data['main_page_benefit_2_under_txt_pl'] = main_page_txt[0].main_page_benefit_2_under_txt_pl
    main_page_data['main_page_benefit_3_main_txt_de'] = main_page_txt[0].main_page_benefit_3_main_txt_de
    main_page_data['main_page_benefit_3_main_txt_pl'] = main_page_txt[0].main_page_benefit_3_main_txt_pl
    main_page_data['main_page_benefit_3_under_txt_de'] = main_page_txt[0].main_page_benefit_3_under_txt_de
    main_page_data['main_page_benefit_3_under_txt_pl'] = main_page_txt[0].main_page_benefit_3_under_txt_pl
    main_page_data['main_page_about_me_title_txt_de'] = main_page_txt[0].main_page_about_me_title_txt_de
    main_page_data['main_page_about_me_title_txt_pl'] = main_page_txt[0].main_page_about_me_title_txt_pl
    main_page_data['main_page_about_me_text_txt_de'] = main_page_txt[0].main_page_about_me_text_txt_de
    main_page_data[' main_page_about_me_text_txt_pl'] = main_page_txt[0].main_page_about_me_text_txt_pl

    context = {**header_data, **main_page_data}

    return render(request,'quizapp/main_page.html',context)

def simple_question(request):

    context = {**header_data}

    return render(request,'quizapp/simple_question_page.html',context)