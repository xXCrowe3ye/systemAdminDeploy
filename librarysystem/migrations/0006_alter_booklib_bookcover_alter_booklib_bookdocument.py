# Generated by Django 4.2.7 on 2023-12-06 15:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarysystem', '0005_alter_booklib_bookcover_alter_booklib_bookdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booklib',
            name='bookcover',
            field=models.ImageField(default='Harry Potter.jpg', upload_to='book_covers/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]),
        ),
        migrations.AlterField(
            model_name='booklib',
            name='bookdocument',
            field=models.FileField(default='Chapter1.pdf', upload_to='book_documents/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'csv'])]),
        ),
    ]
