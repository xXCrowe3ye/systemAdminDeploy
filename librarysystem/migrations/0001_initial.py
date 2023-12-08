# Generated by Django 4.2.1 on 2023-05-17 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booklib',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=11)),
                ('booktitle', models.CharField(max_length=50)),
                ('bookauthor', models.CharField(max_length=50)),
                ('yearpub', models.CharField(max_length=4)),
                ('bookgenre', models.CharField(max_length=100)),
                ('radio_choice', models.CharField(choices=[('condi_brandnew', 'Brandnew'), ('condi_fair', 'Secondhand - Fair'), ('condi_poor', 'Secondhand - Poor')], max_length=20)),
                ('booksummary', models.TextField(max_length=500)),
            ],
        ),
    ]
