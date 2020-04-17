from django.shortcuts import render
from .models import HeaderPageTxt, MainPageTxt, QuestionPageTxt, Question, TestPageTxt

header_txt = HeaderPageTxt.objects.all()[:1]
header_data = {}

# menu
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
# hero
header_data['hero_main_txt_de'] = header_txt[0].hero_main_txt_de
header_data['hero_main_txt_pl'] = header_txt[0].hero_main_txt_pl
header_data['hero_under_txt_de'] = header_txt[0].hero_under_txt_de
header_data['hero_under_txt_pl'] = header_txt[0].hero_under_txt_pl

def main_page(request):

    main_page_txt = MainPageTxt.objects.all()[:1]
    main_page_data = {}

    # without account
    main_page_data['main_page_without_account_title_txt_de'] = main_page_txt[0].main_page_without_account_title_txt_de
    main_page_data['main_page_without_account_title_txt_pl'] = main_page_txt[0].main_page_without_account_title_txt_pl
    main_page_data['main_page_without_account_benefit_1_txt_de'] = main_page_txt[0].main_page_without_account_benefit_1_txt_de
    main_page_data['main_page_without_account_benefit_1_txt_pl'] = main_page_txt[0].main_page_without_account_benefit_1_txt_pl
    main_page_data['main_page_without_account_benefit_2_txt_de'] = main_page_txt[0].main_page_without_account_benefit_2_txt_de
    main_page_data['main_page_without_account_benefit_2_txt_pl'] = main_page_txt[0].main_page_without_account_benefit_2_txt_pl
    main_page_data['main_page_without_account_benefit_3_txt_de'] = main_page_txt[0].main_page_without_account_benefit_3_txt_de
    main_page_data['main_page_without_account_benefit_3_txt_pl'] = main_page_txt[0].main_page_without_account_benefit_3_txt_pl
    # with account
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
    # buttons
    main_page_data['main_page_without_account_single_question_btn_txt_de'] = main_page_txt[0].main_page_without_account_single_question_btn_txt_de
    main_page_data['main_page_without_account_single_question_btn_txt_pl'] = main_page_txt[0].main_page_without_account_single_question_btn_txt_pl
    main_page_data['main_page_without_account_full_test_btn_txt_de'] = main_page_txt[0].main_page_without_account_full_test_btn_txt_de
    main_page_data['main_page_without_account_full_test_btn_txt_pl'] = main_page_txt[0].main_page_without_account_full_test_btn_txt_pl
    main_page_data['main_page_with_account_make_account_btn_txt_de'] = main_page_txt[0].main_page_with_account_make_account_btn_txt_de
    main_page_data['main_page_with_account_make_account_btn_txt_pl'] = main_page_txt[0].main_page_with_account_make_account_btn_txt_pl
    main_page_data['main_page_with_account_login_btn_txt_de'] = main_page_txt[0].main_page_with_account_login_btn_txt_de
    main_page_data['main_page_with_account_login_btn_txt_pl'] = main_page_txt[0].main_page_with_account_login_btn_txt_pl
    # benefits
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
    # about me
    main_page_data['main_page_about_me_title_txt_de'] = main_page_txt[0].main_page_about_me_title_txt_de
    main_page_data['main_page_about_me_title_txt_pl'] = main_page_txt[0].main_page_about_me_title_txt_pl
    main_page_data['main_page_about_me_text_txt_de'] = main_page_txt[0].main_page_about_me_text_txt_de
    main_page_data[' main_page_about_me_text_txt_pl'] = main_page_txt[0].main_page_about_me_text_txt_pl

    context = {**header_data, **main_page_data}

    return render(request,'quizapp/main_page.html',context)

def simple_question(request):

    question_data = {}
    all_questions = Question.objects.all()
    question_data['all_questions'] = all_questions

    question_page_txt = QuestionPageTxt.objects.all()[:1]
    question_page_data = {}

    # buttons
    question_page_data['question_page_new_question_btn_txt_de'] = question_page_txt[0].question_page_new_question_btn_txt_de
    question_page_data['question_page_new_question_btn_txt_pl'] = question_page_txt[0].question_page_new_question_btn_txt_pl
    question_page_data['question_page_check_question_btn_txt_de'] = question_page_txt[0].question_page_check_question_btn_txt_de
    question_page_data['question_page_check_question_btn_txt_pl'] = question_page_txt[0].question_page_check_question_btn_txt_pl
    # topics
    question_page_data['question_page_topic_txt_de'] = question_page_txt[0].question_page_topic_txt_de
    question_page_data['question_page_topic_txt_pl'] = question_page_txt[0].question_page_topic_txt_pl
    question_page_data['question_page_under_topic_txt_de'] = question_page_txt[0].question_page_under_topic_txt_de
    question_page_data['question_page_under_topic_txt_pl'] = question_page_txt[0].question_page_under_topic_txt_pl
    # quetion
    question_page_data['question_page_question_header_txt_de'] = question_page_txt[0].question_page_question_header_txt_de
    question_page_data['question_page_question_header_txt_pl'] = question_page_txt[0].question_page_question_header_txt_pl
    # modal
    question_page_data['question_page_modal_title_txt_de'] = question_page_txt[0].question_page_modal_title_txt_de
    question_page_data['question_page_modal_title_txt_pl'] = question_page_txt[0].question_page_modal_title_txt_pl
    # modal buttons
    question_page_data['question_page_modal_try_again_btn_txt_de'] = question_page_txt[0].question_page_modal_try_again_btn_txt_de
    question_page_data['question_page_modal_try_again_btn_txt_pl'] = question_page_txt[0].question_page_modal_try_again_btn_txt_pl
    question_page_data['question_page_modal_correct_answer_btn_txt_de'] = question_page_txt[0].question_page_modal_correct_answer_btn_txt_de
    question_page_data['question_page_modal_correct_answer_btn_txt_pl'] = question_page_txt[0].question_page_modal_correct_answer_btn_txt_pl
    question_page_data['question_page_modal_new_question_btn_txt_de'] = question_page_txt[0].question_page_modal_new_question_btn_txt_de
    question_page_data['question_page_modal_new_question_btn_txt_pl'] = question_page_txt[0].question_page_modal_new_question_btn_txt_pl

    context = {**question_data,**header_data,**question_page_data}

    return render(request,'quizapp/simple_question_page.html',context)

def full_test(request):

    question_data = {}
    all_questions = Question.objects.all()
    question_data['all_questions'] = all_questions

    test_page_txt = TestPageTxt.objects.all()[:1]
    test_page_data = {}

    #buttons texts
    test_page_data['test_page_new_test_btn_txt_de'] = test_page_txt[0].test_page_new_test_btn_txt_de
    test_page_data['test_page_new_test_btn_txt_pl'] = test_page_txt[0].test_page_new_test_btn_txt_pl
    test_page_data['test_page_check_test_btn_txt_de'] = test_page_txt[0].test_page_check_test_btn_txt_de
    test_page_data['test_page_check_test_btn_txt_pl'] = test_page_txt[0].test_page_check_test_btn_txt_pl
    test_page_data['test_page_test_info_btn_txt_de'] = test_page_txt[0].test_page_test_info_btn_txt_de
    test_page_data['test_page_test_info_btn_txt_pl'] = test_page_txt[0].test_page_test_info_btn_txt_pl
    # other questions text
    test_page_data['test_page_other_question_txt_de'] = test_page_txt[0].test_page_other_question_txt_de
    test_page_data['test_page_other_question_txt_pl'] = test_page_txt[0].test_page_other_question_txt_pl
    #other topic buttons texts
    test_page_data['test_page_ichtyology_btn_txt_de'] = test_page_txt[0].test_page_ichtyology_btn_txt_de
    test_page_data['test_page_ichtyology_btn_txt_pl'] = test_page_txt[0].test_page_ichtyology_btn_txt_pl
    test_page_data['test_page_maintenace_of_fish_water_btn_txt_de'] = test_page_txt[0].test_page_maintenace_of_fish_water_btn_txt_de
    test_page_data['test_page_maintenace_of_fish_water_btn_txt_pl'] = test_page_txt[0].test_page_maintenace_of_fish_water_btn_txt_pl
    test_page_data['test_page_fishing_gear_btn_txt_de'] = test_page_txt[0].test_page_fishing_gear_btn_txt_de
    test_page_data['test_page_fishing_gear_btn_txt_pl'] = test_page_txt[0].test_page_fishing_gear_btn_txt_pl
    test_page_data['test_page_treatment_of_cathing_fish_btn_txt_de'] = test_page_txt[0].test_page_treatment_of_cathing_fish_btn_txt_de
    test_page_data['test_page_treatment_of_cathing_fish_btn_txt_pl'] = test_page_txt[0].test_page_treatment_of_cathing_fish_btn_txt_pl
    test_page_data['test_page_relevant_legislation_btn_txt_de'] = test_page_txt[0].test_page_relevant_legislation_btn_txt_de
    test_page_data['test_page_relevant_legislation_btn_txt_pl'] = test_page_txt[0].test_page_relevant_legislation_btn_txt_pl
    #modal results texts
    test_page_data['test_page_modal_results_title_btn_txt_de'] = test_page_txt[0].test_page_modal_results_title_btn_txt_de
    test_page_data['test_page_modal_results_title_btn_txt_pl'] = test_page_txt[0].test_page_modal_results_title_btn_txt_pl
    test_page_data['test_page_modal_results_correct_answer_txt_de'] = test_page_txt[0].test_page_modal_results_correct_answer_txt_de
    test_page_data['test_page_modal_results_correct_answer_txt_pl'] = test_page_txt[0].test_page_modal_results_correct_answer_txt_pl
    # modal results topi texts
    test_page_data['test_page_modal_ichtyology_txt_de'] = test_page_txt[0].test_page_modal_ichtyology_txt_de
    test_page_data['test_page_modal_ichtyology_txt_pl'] = test_page_txt[0].test_page_modal_ichtyology_txt_pl
    test_page_data['test_page_modal_maintenace_of_fish_water_txt_de'] = test_page_txt[0].test_page_modal_maintenace_of_fish_water_txt_de
    test_page_data['test_page_modal_maintenace_of_fish_water_txt_pl'] = test_page_txt[0].test_page_modal_maintenace_of_fish_water_txt_pl
    test_page_data['test_page_modal_fishing_gear_txt_de'] = test_page_txt[0].test_page_modal_fishing_gear_txt_de
    test_page_data['test_page_modal_fishing_gear_txt_pl'] = test_page_txt[0].test_page_modal_fishing_gear_txt_pl
    test_page_data['test_page_modal_treatment_of_cathing_fish_txt_de'] = test_page_txt[0].test_page_modal_treatment_of_cathing_fish_txt_de
    test_page_data['test_page_modal_treatment_of_cathing_fish_txt_pl'] = test_page_txt[0].test_page_modal_treatment_of_cathing_fish_txt_pl
    test_page_data['test_page_modal_relevant_legislation_txt_de'] = test_page_txt[0].test_page_modal_relevant_legislation_txt_de
    test_page_data['test_page_modal_relevant_legislation_txt_pl'] = test_page_txt[0].test_page_modal_relevant_legislation_txt_pl
    # modal results buttons
    test_page_data['test_page_modal_try_again_btn_txt_de'] = test_page_txt[0].test_page_modal_try_again_btn_txt_de
    test_page_data['test_page_modal_try_again_btn_txt_pl'] = test_page_txt[0].test_page_modal_try_again_btn_txt_pl
    test_page_data['test_page_modal_new_test_btn_txt_de'] = test_page_txt[0].test_page_modal_new_test_btn_txt_de
    test_page_data['test_page_modal_new_test_btn_txt_pl'] = test_page_txt[0].test_page_modal_new_test_btn_txt_pl
    # modal test info texts
    test_page_data['test_page_modal_test_info_title_txt_de'] = test_page_txt[0].test_page_modal_test_info_title_txt_de
    test_page_data['test_page_modal_test_info_title_txt_pl'] = test_page_txt[0].test_page_modal_test_info_title_txt_pl
    test_page_data['test_page_modal_test_info_text_txt_de'] = test_page_txt[0].test_page_modal_test_info_text_txt_de
    test_page_data['test_page_modal_test_info_text_txt_pl'] = test_page_txt[0].test_page_modal_test_info_text_txt_pl
    # modal test info buttons
    test_page_data['test_page_modal_test_info_close_btn_txt_de'] = test_page_txt[0].test_page_modal_test_info_close_btn_txt_de
    test_page_data['test_page_modal_test_info_close_btn_txt_pl'] = test_page_txt[0].test_page_modal_test_info_close_btn_txt_pl

    context = {**question_data,**header_data,**test_page_data}

    return render(request,'quizapp/full_test_page.html',context)