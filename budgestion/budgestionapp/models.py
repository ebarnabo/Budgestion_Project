from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.
class Etudiant(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=200, unique=True)
    mdp_hash = models.CharField(max_length=128)
    nom = models.CharField(max_length=200, null=True, blank=True)
    prenom = models.CharField(max_length=200, null=True, blank=True)
    dateNaissance = models.DateField(null=True, blank=True)
    mail = models.EmailField(null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_admin = models.BooleanField(default=False, null=True, blank=True)


    # etablissement = models.CharField(max_length=200, choices=API_CHOICES)

    def set_mdp(self, mdp):
        self.mdp_hash = make_password(mdp)



class Categorie(models.Model):
    idCategorie = models.AutoField(primary_key=True)
    nomCategorie = models.CharField(max_length=200)
    descriptionCategorie = models.TextField()

class Revenu(models.Model):
    id = models.AutoField(primary_key=True)
    idEtudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    jour = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=200, default="Revenu")



class Achat(models.Model):
    id = models.AutoField(primary_key=True)
    idEtudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, null=True, blank=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    jour = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=200, default="Achat")



from django.db.models import Sum

def getSommeRevenus(idEtudiant):
    somme_revenus = Revenu.objects.filter(idEtudiant=idEtudiant).aggregate(total_revenus=Sum('montant'))
    return somme_revenus['total_revenus'] if somme_revenus['total_revenus'] else 0

def getSommeDepenses(idEtudiant):
    somme_depenses = Achat.objects.filter(idEtudiant=idEtudiant).aggregate(total_depenses=Sum('montant'))
    return somme_depenses['total_depenses'] if somme_depenses['total_depenses'] else 0

def getListeDepenses(idEtudiant):
    liste_depenses = Achat.objects.filter(idEtudiant=idEtudiant)
    return liste_depenses

def getListeRevenus(idEtudiant):
    liste_revenus = Revenu.objects.filter(idEtudiant=idEtudiant)
    return liste_revenus

def getSolde(idEtudiant):
    total_revenus = getSommeRevenus(idEtudiant)
    total_depenses = getSommeDepenses(idEtudiant)
    solde = total_revenus - total_depenses
    return solde

