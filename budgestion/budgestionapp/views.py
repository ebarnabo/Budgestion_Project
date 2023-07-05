from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from .models import *



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


def logout(request):
    # Supprimer la clé 'etudiant_id' de la session
    if 'etudiant_id' in request.session:
        del request.session['etudiant_id']

    # Rediriger vers une page après la déconnexion (par exemple, la page d'accueil)
    return redirect('connexion')

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
    if not  request.session.get('etudiant_id'):
        # La session n'est pas connectée, rediriger vers la page d'index
        return redirect('connexion')

    # Récupérer l'ID de l'étudiant en session
    etudiant_id = request.session.get('etudiant_id')

    # Récupérer l'étudiant correspondant à l'ID
    etudiant = Etudiant.objects.get(id=etudiant_id)

    somme_revenus = getSommeRevenus(etudiant_id)
    somme_depenses = getSommeDepenses(etudiant_id)
    liste_depenses = getListeDepenses(etudiant_id)
    liste_revenus = getListeRevenus(etudiant_id)

    liste_transactions = list(liste_depenses) + list(liste_revenus)
    import datetime

    reference_date = datetime.datetime(1900, 1, 1)

    liste_transactions = sorted(liste_transactions, key=lambda t: (
                reference_date - datetime.datetime.combine(t.jour, datetime.datetime.min.time())).total_seconds(),
                                reverse=False)

    solde = getSolde(etudiant_id)


    return render(request, 'dashboard.html', {
        'pseudo': etudiant.login,
        'somme_revenus': somme_revenus,
        'somme_depenses': somme_depenses,
        'liste_depenses': liste_depenses,
        'liste_revenus': liste_revenus,
        'liste_transactions': liste_transactions,
        'solde': solde
    })
def delLigne(request):
    if request.method == 'POST':

        entry_id = request.POST.get('delete_entry_id')
        entry_type = request.POST.get('delete_entry_type')
        print(entry_id, entry_type)

        if entry_type == 'Achat':
            entry = Achat.objects.get(id=entry_id)
        elif entry_type == 'Revenu':
            entry = Revenu.objects.get(id=entry_id)

        entry.delete()
        return redirect('dashboard')  # Rediriger vers la page de tableau de bord après l'ajout

    return render(request, 'dashboard.html')



def addLigne(request):
    if request.method == 'POST':

        etudiant_id = request.session.get('etudiant_id')
        etudiant = Etudiant.objects.get(id=etudiant_id)

        nom = request.POST.get('nom')
        montant = request.POST.get('montant')
        date = request.POST.get('date')
        type_entree = request.POST.get('type')
        print(nom, montant, date, type_entree)
        if type_entree == 'revenu':
            revenu = Revenu.objects.create(description=nom, montant=montant, jour=date, idEtudiant = etudiant)
            revenu.save()
        elif type_entree == 'depense':
            depense = Achat.objects.create(description=nom, montant=montant, jour=date, idEtudiant = etudiant)
            depense.save()

        return redirect('dashboard')  # Rediriger vers la page de tableau de bord après l'ajout

    return render(request, 'dashboard.html')






def dashboardadmin(request):
    return render(request, 'dashboard-admin.html')


