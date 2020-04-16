# Generated by Django 3.0.5 on 2020-04-15 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_auto_20200416_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageTxt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_page_without_account_title_txt_de', models.CharField(max_length=50)),
                ('main_page_without_account_title_txt_pl', models.CharField(max_length=50)),
                ('main_page_without_account_benefit_1_txt_de', models.CharField(max_length=150)),
                ('main_page_without_account_benefit_1_txt_pl', models.CharField(max_length=150)),
                ('main_page_without_account_benefit_2_txt_de', models.CharField(max_length=150)),
                ('main_page_without_account_benefit_2_txt_pl', models.CharField(max_length=150)),
                ('main_page_without_account_benefit_3_txt_de', models.CharField(max_length=150)),
                ('main_page_without_account_benefit_3_txt_pl', models.CharField(max_length=150)),
                ('main_page_with_account_title_txt_de', models.CharField(max_length=50)),
                ('main_page_with_account_title_txt_pl', models.CharField(max_length=50)),
                ('main_page_with_account_benefit_1_txt_de', models.CharField(max_length=150)),
                ('main_page_with_account_benefit_1_txt_pl', models.CharField(max_length=150)),
                ('main_page_with_account_benefit_2_txt_de', models.CharField(max_length=150)),
                ('main_page_with_account_benefit_2_txt_pl', models.CharField(max_length=150)),
                ('main_page_with_account_benefit_3_txt_de', models.CharField(max_length=150)),
                ('main_page_with_account_benefit_3_txt_pl', models.CharField(max_length=150)),
                ('main_page_with_account_benefit_4_txt_de', models.CharField(max_length=150)),
                ('main_page_with_account_benefit_4_txt_pl', models.CharField(max_length=150)),
                ('main_page_with_account_benefit_5_txt_de', models.CharField(max_length=150)),
                ('main_page_with_account_benefit_5_txt_pl', models.CharField(max_length=150)),
                ('main_page_without_account_single_question_btn_txt_de', models.CharField(max_length=30)),
                ('main_page_without_account_single_question_btn_txt_pl', models.CharField(max_length=30)),
                ('main_page_without_account_full_test_btn_txt_de', models.CharField(max_length=30)),
                ('main_page_without_account_full_test_btn_txt_pl', models.CharField(max_length=30)),
                ('main_page_with_account_make_account_btn_txt_de', models.CharField(max_length=30)),
                ('main_page_with_account_make_account_btn_txt_pl', models.CharField(max_length=30)),
                ('main_page_with_account_login_btn_txt_de', models.CharField(max_length=30)),
                ('main_page_with_account_login_btn_txt_pl', models.CharField(max_length=30)),
                ('main_page_benefit_1_main_txt_de', models.CharField(max_length=50)),
                ('main_page_benefit_1_main_txt_pl', models.CharField(max_length=50)),
                ('main_page_benefit_1_under_txt_de', models.CharField(max_length=100)),
                ('main_page_benefit_1_under_txt_pl', models.CharField(max_length=100)),
                ('main_page_benefit_2_main_txt_de', models.CharField(max_length=50)),
                ('main_page_benefit_2_main_txt_pl', models.CharField(max_length=50)),
                ('main_page_benefit_2_under_txt_de', models.CharField(max_length=100)),
                ('main_page_benefit_2_under_txt_pl', models.CharField(max_length=100)),
                ('main_page_benefit_3_main_txt_de', models.CharField(max_length=50)),
                ('main_page_benefit_3_main_txt_pl', models.CharField(max_length=50)),
                ('main_page_benefit_3_under_txt_de', models.CharField(max_length=100)),
                ('main_page_benefit_3_under_txt_pl', models.CharField(max_length=100)),
                ('main_page_about_me_title_txt_de', models.CharField(max_length=30)),
                ('main_page_about_me_title_txt_pl', models.CharField(max_length=30)),
                ('main_page_about_me_text_txt_de', models.CharField(max_length=500)),
                ('main_page_about_me_text_txt_pl', models.CharField(max_length=500)),
            ],
        ),
    ]