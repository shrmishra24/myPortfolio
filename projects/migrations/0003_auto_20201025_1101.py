# Generated by Django 3.1.2 on 2020-10-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_about_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('title', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=13)),
                ('age', models.IntegerField()),
                ('location', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('detail_desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
    ]
