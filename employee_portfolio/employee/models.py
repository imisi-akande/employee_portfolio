from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

# Create your models here.
class Department(models.Model):
    """This class represents the department model."""
    department = models.CharField(max_length=255, blank=False)
    firstname = models.CharField(max_length=55, blank=False)
    lastname = models.CharField(max_length=55, blank=False)
    email = models.EmailField(max_length=70,blank=False, unique= True)
    description = models.CharField(max_length=255, blank=False)
    employer = models.ForeignKey('auth.User', 
            related_name='departments',
            on_delete=models.CASCADE)  
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.department)
    
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

        