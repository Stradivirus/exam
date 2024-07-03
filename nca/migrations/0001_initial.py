# Generated by Django 4.2.13 on 2024-07-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NCA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice_a', models.CharField(max_length=100)),
                ('choice_b', models.CharField(max_length=100)),
                ('choice_c', models.CharField(max_length=100)),
                ('choice_d', models.CharField(max_length=100)),
                ('correct_answer', models.CharField(max_length=100)),
            ],
        ),
    ]
