# Generated by Django 3.0.5 on 2020-04-16 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0003_mainpagetxt'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPageTxt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_page_new_question_btn_txt_de', models.CharField(max_length=30)),
                ('question_page_new_question_btn_txt_pl', models.CharField(max_length=30)),
                ('question_page_check_question_btn_txt_de', models.CharField(max_length=30)),
                ('question_page_check_question_btn_txt_pl', models.CharField(max_length=30)),
                ('question_page_topic_txt_de', models.CharField(max_length=30)),
                ('question_page_topic_txt_pl', models.CharField(max_length=30)),
                ('question_page_under_topic_txt_de', models.CharField(max_length=30)),
                ('question_page_under_topic_txt_pl', models.CharField(max_length=30)),
                ('question_page_question_header_txt_de', models.CharField(max_length=30)),
                ('question_page_question_header_txt_pl', models.CharField(max_length=30)),
                ('question_page_modal_title_txt_de', models.CharField(max_length=30)),
                ('question_page_modal_title_txt_pl', models.CharField(max_length=30)),
                ('question_page_modal_try_again_btn_txt_de', models.CharField(max_length=30)),
                ('question_page_modal_try_again_btn_txt_pl', models.CharField(max_length=30)),
                ('question_page_modal_correct_answer_btn_txt_de', models.CharField(max_length=30)),
                ('question_page_modal_correct_answer_btn_txt_pl', models.CharField(max_length=30)),
                ('question_page_modal_new_question_btn_txt_de', models.CharField(max_length=30)),
                ('question_page_modal_new_question_btn_txt_pl', models.CharField(max_length=30)),
            ],
        ),
    ]