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





