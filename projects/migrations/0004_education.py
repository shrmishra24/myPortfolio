# Generated by Django 3.1.2 on 2020-10-26 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20201025_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('marks', models.CharField(max_length=5)),
                ('year', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
    ]