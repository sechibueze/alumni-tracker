# Generated by Django 3.2.3 on 2021-05-31 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pathway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Alumni pathway')),
                ('description', models.CharField(default='Enter your pathway text', max_length=250, verbose_name='pathway description')),
            ],
        ),
    ]
