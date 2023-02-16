# Generated by Django 4.0.7 on 2022-09-28 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Заголовок запитання')),
                ('description', models.CharField(max_length=2000, verbose_name='Опис Жанру')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва Тесту')),
                ('description', models.CharField(max_length=2000, verbose_name='Опис Жанру')),
                ('addDate', models.DateField(auto_now=True, verbose_name='Дата додавання')),
            ],
        ),
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Заголовок відповіді')),
                ('is_right', models.BooleanField(verbose_name='Чи є відповідь правильною')),
                ('Answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.answer')),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='Test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.test'),
        ),
    ]