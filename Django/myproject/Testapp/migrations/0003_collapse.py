# Generated by Django 4.2.4 on 2023-09-16 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Testapp', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collapse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('first_button', models.CharField(max_length=30)),
                ('second_button', models.CharField(max_length=30)),
                ('text_field', models.TextField()),
            ],
        ),
    ]
