from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
class Etudiant(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=200)
    mdp_hash = models.CharField(max_length=128)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    dateNaissance = models.DateField()
    mail = models.EmailField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    # etablissement = models.CharField(max_length=200, choices=API_CHOICES)

    def set_mdp(self, mdp):
        self.mdp_hash = make_password(mdp)

class Categorie(models.Model):
    idCategorie = models.AutoField(primary_key=True)
    nomCategorie = models.CharField(max_length=200)
    descriptionCategorie = models.TextField()


class Revenu(models.Model):
    idRevenu = models.AutoField(primary_key=True)
    idEtudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    montantRevenu = models.DecimalField(max_digits=10, decimal_places=2)
    jourRevenu = models.DateField()
    heureRevenu = models.TimeField()
    idCategorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)


class Achat(models.Model):
    idAchat = models.AutoField(primary_key=True)
    idEtudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    montantAchat = models.DecimalField(max_digits=10, decimal_places=2)
    jourAchat = models.DateField()
    heureAchat = models.TimeField()
    idCategorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
