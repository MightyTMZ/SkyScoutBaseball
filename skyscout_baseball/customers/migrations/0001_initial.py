# Generated by Django 4.2.7 on 2024-08-04 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Waitlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('job_title', models.CharField(max_length=255)),
                ('been_in_baseball_industry', models.BooleanField()),
                ('type_of_involvement', models.CharField(choices=[('Pl', 'Player (current or former)'), ('Co', 'Coach'), ('Pa', 'Parent'), ('N/A', 'Not in industry')], max_length=5)),
                ('comments', models.TextField(blank=True, max_length=10000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('testimonial', models.BooleanField()),
            ],
        ),
    ]
