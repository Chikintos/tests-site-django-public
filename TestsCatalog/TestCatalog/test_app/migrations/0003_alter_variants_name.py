# Generated by Django 4.0.7 on 2022-09-29 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_alter_answer_description_alter_test_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variants',
            name='name',
            field=models.CharField(max_length=150, null=True, verbose_name='Заголовок відповіді'),
        ),
    ]
