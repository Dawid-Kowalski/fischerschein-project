from django.db import models

class HeaderPageTxt(models.Model):
    # menu texts pl and de
    menu_simple_question_txt_de = models.CharField(max_length=30)
    menu_simple_question_txt_pl = models.CharField(max_length=30)
    menu_full_test_txt_de = models.CharField(max_length=30)
    menu_full_test_txt_pl = models.CharField(max_length=30)
    menu_fischerschein_info_txt_de = models.CharField(max_length=30)
    menu_fischerschein_info_txt_pl = models.CharField(max_length=30)
    menu_FAQ_txt_de = models.CharField(max_length=30)
    menu_FAQ_txt_pl = models.CharField(max_length=30)
    menu_about_project_de = models.CharField(max_length=30)
    menu_about_project_pl = models.CharField(max_length=30)
    # hero texts
    hero_main_txt_de = models.CharField(max_length=80)
    hero_main_txt_pl = models.CharField(max_length=80)
    hero_under_txt_de = models.CharField(max_length=80)
    hero_under_txt_pl = models.CharField(max_length=80)

    def __str__(self):
        return 'Headerpage texts'

class MainPageTxt(models.Model):
    # without account texts
    main_page_without_account_title_txt_de = models.CharField(max_length=50)
    main_page_without_account_title_txt_pl = models.CharField(max_length=50)
    main_page_without_account_benefit_1_txt_de = models.CharField(max_length=150)
    main_page_without_account_benefit_1_txt_pl = models.CharField(max_length=150)
    main_page_without_account_benefit_2_txt_de = models.CharField(max_length=150)
    main_page_without_account_benefit_2_txt_pl = models.CharField(max_length=150)
    main_page_without_account_benefit_3_txt_de = models.CharField(max_length=150)
    main_page_without_account_benefit_3_txt_pl = models.CharField(max_length=150)
    # with account texts
    main_page_with_account_title_txt_de = models.CharField(max_length=50)
    main_page_with_account_title_txt_pl = models.CharField(max_length=50)
    main_page_with_account_benefit_1_txt_de = models.CharField(max_length=150)
    main_page_with_account_benefit_1_txt_pl = models.CharField(max_length=150)
    main_page_with_account_benefit_2_txt_de = models.CharField(max_length=150)
    main_page_with_account_benefit_2_txt_pl = models.CharField(max_length=150)
    main_page_with_account_benefit_3_txt_de = models.CharField(max_length=150)
    main_page_with_account_benefit_3_txt_pl = models.CharField(max_length=150)
    main_page_with_account_benefit_4_txt_de = models.CharField(max_length=150)
    main_page_with_account_benefit_4_txt_pl = models.CharField(max_length=150)
    main_page_with_account_benefit_5_txt_de = models.CharField(max_length=150)
    main_page_with_account_benefit_5_txt_pl = models.CharField(max_length=150)
    # button texts
    main_page_without_account_single_question_btn_txt_de = models.CharField(max_length=30)
    main_page_without_account_single_question_btn_txt_pl = models.CharField(max_length=30)
    main_page_without_account_full_test_btn_txt_de = models.CharField(max_length=30)
    main_page_without_account_full_test_btn_txt_pl = models.CharField(max_length=30)
    main_page_with_account_make_account_btn_txt_de = models.CharField(max_length=30)
    main_page_with_account_make_account_btn_txt_pl = models.CharField(max_length=30)
    main_page_with_account_login_btn_txt_de = models.CharField(max_length=30)
    main_page_with_account_login_btn_txt_pl = models.CharField(max_length=30)
    # benefits
    main_page_benefit_1_main_txt_de = models.CharField(max_length=50)
    main_page_benefit_1_main_txt_pl = models.CharField(max_length=50)
    main_page_benefit_1_under_txt_de = models.CharField(max_length=100)
    main_page_benefit_1_under_txt_pl = models.CharField(max_length=100)
    main_page_benefit_2_main_txt_de = models.CharField(max_length=50)
    main_page_benefit_2_main_txt_pl = models.CharField(max_length=50)
    main_page_benefit_2_under_txt_de = models.CharField(max_length=100)
    main_page_benefit_2_under_txt_pl = models.CharField(max_length=100)
    main_page_benefit_3_main_txt_de = models.CharField(max_length=50)
    main_page_benefit_3_main_txt_pl = models.CharField(max_length=50)
    main_page_benefit_3_under_txt_de = models.CharField(max_length=100)
    main_page_benefit_3_under_txt_pl = models.CharField(max_length=100)
    # about me footer
    main_page_about_me_title_txt_de = models.CharField(max_length=30)
    main_page_about_me_title_txt_pl = models.CharField(max_length=30)
    main_page_about_me_text_txt_de = models.CharField(max_length=500)
    main_page_about_me_text_txt_pl = models.CharField(max_length=500)

    def __str__(self):
        return 'Mainpage texts'

class QuestionPageTxt(models.Model):
    # buttons texts
    question_page_new_question_btn_txt_de = models.CharField(max_length=30)
    question_page_new_question_btn_txt_pl = models.CharField(max_length=30)
    question_page_check_question_btn_txt_de = models.CharField(max_length=30)
    question_page_check_question_btn_txt_pl = models.CharField(max_length=30)
    # topics texts
    question_page_topic_txt_de = models.CharField(max_length=30)
    question_page_topic_txt_pl = models.CharField(max_length=30)
    question_page_under_topic_txt_de = models.CharField(max_length=30)
    question_page_under_topic_txt_pl = models.CharField(max_length=30)
    # quetion text
    question_page_question_header_txt_de = models.CharField(max_length=30)
    question_page_question_header_txt_pl = models.CharField(max_length=30)
    # modal texts
    question_page_modal_title_txt_de = models.CharField(max_length=30)
    question_page_modal_title_txt_pl = models.CharField(max_length=30)
    # modal buttons
    question_page_modal_try_again_btn_txt_de = models.CharField(max_length=30)
    question_page_modal_try_again_btn_txt_pl = models.CharField(max_length=30)
    question_page_modal_correct_answer_btn_txt_de = models.CharField(max_length=30)
    question_page_modal_correct_answer_btn_txt_pl = models.CharField(max_length=30)
    question_page_modal_new_question_btn_txt_de = models.CharField(max_length=30)
    question_page_modal_new_question_btn_txt_pl = models.CharField(max_length=30)

    def __str__(self):
        return 'Question page texts'
















