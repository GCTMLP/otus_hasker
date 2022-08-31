# Generated by Django 4.0.6 on 2022-08-03 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('cover', models.ImageField(upload_to='images/')),
                ('book', models.FileField(upload_to='books/')),
            ],
        ),
    ]