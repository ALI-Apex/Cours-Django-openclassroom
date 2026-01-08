from django.db import models
from django.contrib.auth.models import AbstractUser


# Modèle User personnalisé étendant AbstractUser pour ajouter photo de profil et rôle
class User(AbstractUser):
    # Constantes pour les rôles des utilisateurs
    CREATOR = "CREATOR"
    SUBSCRIBER = "SUBSCRIBER"

    # Choix disponibles pour le champ role
    ROLE_CHOICES = ((CREATOR, "Createur"), (SUBSCRIBER, "Abonne"))

    # Champ pour la photo de profil de l'utilisateur
    profile_photo = models.ImageField(verbose_name="photo de profil")
    # Champ pour le rôle de l'utilisateur (Createur ou Abonne)
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name="Role")
