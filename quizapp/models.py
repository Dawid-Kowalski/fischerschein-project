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

class Question(models.Model):
    
    MAIN_TOPIC_CHOICES_DE = (
        ('Fischkunde und -hege','Fischkunde und -hege'),
        ('Pflege der Fischgewässer','Pflege der Fischgewässer'),
        ('Fanggeräte und deren Gebrauch','Fanggeräte und deren Gebrauch'),
        ('Behandlung der gefangenen Fische','Behandlung der gefangenen Fische'),
        ('Einschlägige Rechtsvorschriften','Einschlägige Rechtsvorschriften'),
    )

    MAIN_TOPIC_CHOICES_PL = (
        ('budowa ryb','budowa ryb'),
        ('dbanie o miejsca połowu','dbanie o miejsca połowu'),
        ('sprzęt wędkarski i jego użycie','sprzęt wędkarski i jego użycie'),
        ('obchodzenie się ze złapaną rybą','obchodzenie się ze złapaną rybą'),
        ('odpowiadające przepisy','odpowiadające przepisy'),
    )

    UNDER_TOPIC_CHOICES_DE = (
        ('Aufbau des Fischkörpers, Bau und Funktion der Fischorgane','Aufbau des Fischkörpers, Bau und Funktion der Fischorgane'),
        ('Unterscheidung einheimischer Fischarten','Unterscheidung einheimischer Fischarten'),
        ('häufig auftretende Fischkrankheite','häufig auftretende Fischkrankheiten'),
        ('Notwendigkeit von Besatzmaßnahme','Notwendigkeit von Besatzmaßnahme'),
        ('Naturnahrung, Sauerstoff und Temperaturverhältnisse','Naturnahrung, Sauerstoff und Temperaturverhältnisse'),
        ('Sonstiges-Fischkunde und -hege','Sonstiges-Fischkunde und -hege'),
        ('Fischereiliche Gewässerkunde','Fischereiliche Gewässerkunde'),
        ('Schutz der Gewässer vor Verunreinigung','Schutz der Gewässer vor Verunreinigung'),
        ('Ufer und Gelegeschutz','Ufer und Gelegeschutz'),
        ('Mittel und Geräte zur Gewässerinstandhaltung','Mittel und Geräte zur Gewässerinstandhaltung'),
        ('Sonstiges-Pflege der Fischgewässer','Sonstiges-Pflege der Fischgewässer'),
        ('Fanggeräte und deren Gebrauch','Fanggeräte und deren Gebrauch'),
        ('Betäuben, Töten und Schlachten von Fischen','Betäuben, Töten und Schlachten von Fischen'),
        ('Aufbewahrung von Fischen','Aufbewahrung von Fischen'),
        ('Tierschutz','Tierschutz'),
        ('Fischereiordnung des Landes Brandenburg (BbgFischO','Fischereiordnung des Landes Brandenburg (BbgFischO)'),
        ('Sonstiges-Behandlung der gefangenen Fische','Sonstiges-Behandlung der gefangenen Fische'),
        ('Landesfischereirecht','Landesfischereirecht'),
        ('Tierschutzrecht','Tierschutzrecht'),
        ('Naturschutzrecht','Naturschutzrecht'),
        ('Wasserrecht','Wasserrecht'),
        ('Sonstiges-Einschlägige Rechtsvorschriften','Sonstiges-Einschlägige Rechtsvorschriften'),
    )

    UNDER_TOPIC_CHOICES_PL = (
        ('budowa organów u ryb','budowa organów u ryb'),
        ('rozróżnianie rodzinych ryb','rozróżnianie rodzinych ryb'),
        ('najczęstrze choroby u ryb','najczęstrze choroby u ryb'),
        ('zarybianie','zarybianie'),
        ('naturalne warunki życia, tlen i temperatura','naturalne warunki życia, tlen i temperatura'),
        ('pozostałe-budowa ryb','pozostałe-budowa ryb'),
        ('hydrologia','hydrologia'),
        ('ochrona wód przed zanieczyszczeniem','ochrona wód przed zanieczyszczeniem'),
        ('ochrona brzegów i łowisk','ochrona brzegów i łowisk'),
        ('środki i sprzęt do utrzynania łowisk w dobrym stanie','środki i sprzęt do utrzynania łowisk w dobrym stanie'),
        ('pozostałe-dbanie o miejsca połowu','pozostałe-dbanie o miejsca połowu'),
        ('sprzęt wędkarski i jego użycie','sprzęt wędkarski i jego użycie'),
        ('ogłuszanie, uśmiercanie i szlachtowanie ryb','ogłuszanie, uśmiercanie i szlachtowanie ryb'),
        ('przechowywanie ryb','przechowywanie ryb'),
        ('ochrona zwierząt','ochrona zwierząt'),
        ('prawo dot. wędkarstwa w Brandenburgii','prawo dot. wędkarstwa w Brandenburgii'),
        ('pozostałe-obchodzenie się ze złapaną rybą','pozostałe-obchodzenie się ze złapaną rybą'),
        ('prawo połowu','prawo połowu'),
        ('prawo dot. ochrony zwierząt','prawo dot. ochrony zwierząt'),
        ('prawo dot. ochrony przyrody','prawo dot. ochrony przyrody'),
        ('prawo wodne','prawo wodne'),
        ('pozostałe-odpowiadające przepisy','pozostałe-odpowiadające przepisy'),
    )

    question_id = models.IntegerField()

    main_topic_de = models.CharField(max_length=200, choices=MAIN_TOPIC_CHOICES_DE)
    main_topic_pl = models.CharField(max_length=200, choices=MAIN_TOPIC_CHOICES_PL)
    under_topic_de = models.CharField(max_length=200, choices=UNDER_TOPIC_CHOICES_DE)
    under_topic_pl = models.CharField(max_length=200, choices=UNDER_TOPIC_CHOICES_PL)

    question_de = models.TextField(max_length=400)
    question_pl = models.TextField(max_length=400)

    answer_a_de = models.TextField(max_length=400)
    answer_a_pl = models.TextField(max_length=400)
    answer_b_de = models.TextField(max_length=400)
    answer_b_pl = models.TextField(max_length=400)
    answer_c_de = models.TextField(max_length=400)
    answer_c_pl = models.TextField(max_length=400)

    correct_answer_de = models.TextField(max_length=400)
    correct_answer_pl = models.TextField(max_length=400)

    def __str__(self):
        return f'{self.question_id} . {self.question_de}'
    
    class Meta:
        ordering = ('question_id',)

class TestPageTxt(models.Model):
    #buttons texts
    test_page_new_test_btn_txt_de = models.CharField(max_length=30)
    test_page_new_test_btn_txt_pl = models.CharField(max_length=30)
    test_page_check_test_btn_txt_de = models.CharField(max_length=30)
    test_page_check_test_btn_txt_pl = models.CharField(max_length=30)
    test_page_test_info_btn_txt_de = models.CharField(max_length=30)
    test_page_test_info_btn_txt_pl = models.CharField(max_length=30)
    # other questions text
    test_page_other_question_txt_pl = models.CharField(max_length=80)
    #other topic buttons texts
    test_page_ichtyology_btn_txt_de = models.CharField(max_length=50)
    test_page_ichtyology_btn_txt_pl = models.CharField(max_length=50)
    test_page_maintenace_of_fish_water_btn_txt_de = models.CharField(max_length=50)
    test_page_maintenace_of_fish_water_btn_txt_pl = models.CharField(max_length=50)
    test_page_fishing_gear_btn_txt_de = models.CharField(max_length=50)
    test_page_fishing_gear_btn_txt_pl = models.CharField(max_length=50)
    test_page_treatment_of_cathing_fish_btn_txt_de = models.CharField(max_length=50)
    test_page_treatment_of_cathing_fish_btn_txt_pl = models.CharField(max_length=50)
    test_page_relevant_legislation_btn_txt_de = models.CharField(max_length=50)
    test_page_relevant_legislation_btn_txt_pl = models.CharField(max_length=50)
    #modal results texts
    test_page_modal_results_title_btn_txt_de = models.CharField(max_length=30)
    test_page_modal_results_title_btn_txt_de = models.CharField(max_length=30)
    test_page_modal_results_correct_answer_txt_de = models.CharField(max_length=30)
    test_page_modal_results_correct_answer_txt_pl = models.CharField(max_length=30)
    # modal results topi texts
    test_page_modal_ichtyology_txt_de = models.CharField(max_length=50)
    test_page_modal_ichtyology_txt_pl = models.CharField(max_length=50)
    test_page_modal_maintenace_of_fish_water_txt_de = models.CharField(max_length=50)
    test_page_modal_maintenace_of_fish_water_txt_pl = models.CharField(max_length=50)
    test_page_modal_fishing_gear_txt_de = models.CharField(max_length=50)
    test_page_modal_fishing_gear_txt_pl = models.CharField(max_length=50)
    test_page_modal_treatment_of_cathing_fish_txt_de = models.CharField(max_length=50)
    test_page_modal_treatment_of_cathing_fish_txt_pl = models.CharField(max_length=50)
    test_page_modal_relevant_legislation_txt_de = models.CharField(max_length=50)
    test_page_modal_relevant_legislation_txt_pl = models.CharField(max_length=50) 
    # modal buttons
    test_page_modal_try_again_btn_txt_de = models.CharField(max_length=30)
    test_page_modal_try_again_btn_txt_pl = models.CharField(max_length=30)
    test_page_modal_new_test_btn_txt_de = models.CharField(max_length=30)
    test_page_modal_new_test_btn_txt_pl = models.CharField(max_length=30)

    def __str__(self):
        return 'Test page texts'
























