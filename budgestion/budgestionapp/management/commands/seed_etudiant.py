from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError

from budgestionapp.models import Etudiant

class Command(BaseCommand):
    help = 'Seed Etudiant data'

    def handle(self, *args, **options):
        # Création des étudiants
        etudiants = [
            {
                'login': 'adminEtudiant',
                'mdp_hash': make_password('p@sswordAdmin'),
                'nom': 'Admin',
                'prenom': 'EtuAdmin',
                'dateNaissance': '1980-01-01',
                'etablissement': 'Etablissement 2',
                'mail': 'admin@example.com',
                'budget': 15000,
                'is_admin': True,
            },
            {
                'login': 'etudiant1',
                'mdp_hash': make_password('password1'),
                'nom': 'Nom 1',
                'prenom': 'Prenom 1',
                'dateNaissance': '2000-01-01',
                'etablissement': 'Etablissement 1',
                'mail': 'etudiant1@example.com',
                'budget': 1000,
                'is_admin': False,
            },
            {
                'login': 'etudiant2',
                'mdp_hash': make_password('password2'),
                'nom': 'Nom 2',
                'prenom': 'Prenom 2',
                'dateNaissance': '2000-02-02',
                'etablissement': 'Etablissement 2',
                'mail': 'etudiant2@example.com',
                'budget': 1500,
                'is_admin': False,
            },


        ]

        for etudiant_data in etudiants:
            try:
                Etudiant.objects.create(**etudiant_data)
            except IntegrityError:
                self.stdout.write(
                    self.style.WARNING(f"Étudiant avec le login '{etudiant_data['login']}' existe déjà. Ignoré."))

        self.stdout.write(self.style.SUCCESS('Etudiant data seeded successfully.'))