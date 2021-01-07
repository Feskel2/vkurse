# Generated by Django 3.1.5 on 2021-01-06 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210106_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='adress',
            field=models.TextField(blank=True, help_text='Адрес', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='count_estimates',
            field=models.IntegerField(blank=True, help_text='Колво-оценок', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date_time',
            field=models.DateTimeField(blank=True, help_text='Дата и время конца', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='estimates',
            field=models.IntegerField(blank=True, help_text='Колво-оценок', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(blank=True, help_text='Ссылка на мероприятие', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, help_text='Картинка', null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='place',
            field=models.TextField(blank=True, help_text='Координаты места (для карты)', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.CharField(blank=True, help_text='Название на английском', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date_time',
            field=models.DateTimeField(blank=True, help_text='Дата и время начала', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='subject',
            field=models.TextField(blank=True, help_text='Описание', max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='tags',
            field=models.TextField(blank=True, help_text='Тэги', max_length=1000, null=True),
        ),
    ]
