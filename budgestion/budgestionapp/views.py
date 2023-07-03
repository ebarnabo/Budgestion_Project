from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Etudiant



# Create your views here.



def connexion(request):
    if request.method == 'POST':
        pseudo = request.POST['Pseudo']
        mot_de_passe = request.POST['Mot de passe']

        # Vérifier les informations de connexion et authentifier l'étudiant
        try:
            etudiant = Etudiant.objects.get(login=pseudo)
            if check_password(mot_de_passe, etudiant.mdp_hash):
                # Informations de connexion valides, sauvegarder la session et rediriger vers le dashboard
                request.session['etudiant_id'] = etudiant.id
                return redirect('dashboard')
            else:
                # Informations de connexion invalides, afficher un message d'erreur
                return render(request, 'index.html', {'error': 'Informations de connexion incorrectes'})
        except Etudiant.DoesNotExist:
            # Compte inexistant, afficher un message d'erreur
            return render(request, 'index.html', {'error': 'Compte inexistant'})

    return render(request, 'index.html')

def inscription(request):
    if request.method == 'POST':
        login = request.POST['Pseudo']
        password = request.POST['Mot de passe']
        ecole_origine = request.POST["École d'origine"]
        confirm_password = request.POST['Confirmer votre mot de passe']

        # Vérifier si le mot de passe et la confirmation du mot de passe correspondent
        if password != confirm_password:
            return render(request, 'inscription.html', {'error': 'Les mots de passe ne correspondent pas.'})

        # Créer une instance de l'étudiant
        etudiant = Etudiant(
            login=login,
            mdp_hash=make_password(password)
        )

        # Sauvegarder l'étudiant dans la base de données
        etudiant.save()

        # Rediriger l'utilisateur vers une page de succès ou une autre vue
        return redirect('connexion')

    return render(request, 'inscription.html')
def dashboard(request):
    return render(request, 'dashboard.html')


def dashboardadmin(request):
    return render(request, 'dashboard-admin.html')