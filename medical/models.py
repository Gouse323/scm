from django.db import models

# Create your models here.


class Doctors(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    specialist = models.CharField(max_length=100)
    experiance = models.IntegerField()
    email = models.EmailField()


class Patient(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=100)
    problem = models.CharField(max_length=100)
    email = models.EmailField()


# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-host'  # Your SMTP host
EMAIL_PORT = 587  # Your SMTP port number
EMAIL_USE_TLS = True  # Use TLS encryption
EMAIL_HOST_USER = 'gouse030203@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'your-email-password'  # Your email password
# DEFAULT_FROM_EMAIL = 'your-email@example.com'  # Your default "from" address
