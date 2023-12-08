from django.db import models
from django.contrib.auth.models import User
from django.db import migrations
from django.core.validators import FileExtensionValidator


# Create your models here.
class booklib (models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=11)
    booktitle = models.CharField(max_length=50)
    bookauthor = models.CharField(max_length=50)
    yearpub = models.CharField(max_length=4)
    bookgenre = models.CharField(max_length=100)
    RADIO_CHOICES = (
        ('Brandnew', 'Brandnew'),
        ('Secondhand-Fair', 'Secondhand-Fair'),
        ('Secondhand-Poor', 'Secondhand-Poor'),
    )
    radio_choice = models.CharField(max_length=20, choices=RADIO_CHOICES)
    booksummary = models.TextField(max_length=500)
    # bookcover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    # bookdocument = models.FileField(upload_to='book_documents/', null=True, blank=True)
    bookcover = models.ImageField(upload_to='book_covers/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])], default='Harry Potter.jpg')
    bookdocument = models.FileField(upload_to='book_documents/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx', 'csv'])], default='Harry Potter.pdf')    

    def __str__(self):
        return self.booktitle