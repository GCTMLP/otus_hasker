# Generated by Django 4.0.6 on 2022-08-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_votesquestion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-pub_date',)},
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]