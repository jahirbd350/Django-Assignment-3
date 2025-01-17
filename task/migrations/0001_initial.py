# Generated by Django 5.1.3 on 2024-12-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('is_completed', models.BooleanField(default=False)),
                ('task_date', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]
