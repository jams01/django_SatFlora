from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User

MASCULINO = 'MA'
FEMENINO = 'FE'
SEXO_CHOICES = [
    (MASCULINO, 'Masculino'),
    (FEMENINO, 'Femenino'),
]
    
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone = models.CharField(max_length=500, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    picture = models.ImageField(null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    sex = models.CharField(
        max_length=2,
        choices=SEXO_CHOICES,
        default=MASCULINO,
    )
    registerDate = models.DateField(auto_now=True, null=False)
    isactive = models.BooleanField(default=True)
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + "C.C." + self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Crea un perfil solo si se proporcionan datos de perfil
        if hasattr(instance, 'profile') and instance.profile is None:
            Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
     if hasattr(instance, 'profile') and instance.profile is not None:
        instance.profile.save()

