function getAchats() {
    fetch('https://api.gouv.fr/documentation/api-annuaire-education')
      .then(response => response.json())
      .then(data => {
        afficherGraphiqueAchats(data);
      })
      .catch(error => {
        console.error('Une erreur s\'est produite lors de la récupération des achats :', error);
      });
  }
  
  function afficherGraphiqueAchats(data) {
    Highcharts.chart('graphiqueAchats', {
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Répartition des achats dans le temps'
      },
      xAxis: {
        categories: data.labels
      },
      yAxis: {
        title: {
          text: 'Montant des achats'
        }
      },
      series: [{
        name: 'Achats',
        data: data.values
      }]
    });
  }
  
  function enregistrerAchat() {
    var montant = document.getElementById('montant').value;
    var date = document.getElementById('date').value;
  
      var nouvelAchat = {
      montant: montant,
      date: date
    };
  
    fetch('https://api.gouv.fr/annuaire-education/achats/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(nouvelAchat)
    })
      .then(response => response.json())
      .then(data => {
        console.log('Réponse du serveur après l\'enregistrement de l\'achat :', data);
        alert('L\'achat de ' + data.montant + '€ le ' + data.date + ' a été enregistré avec succès !');
      })
      .catch(error => {
        console.error('Une erreur s\'est produite lors de l\'enregistrement de l\'achat :', error);
      });
  }
  
  function init() {
    getAchats();
  
    var formulaireAchat = document.getElementById('formulaireAchat');
    formulaireAchat.addEventListener('submit', function(event) {
      event.preventDefault();
      enregistrerAchat();
    });
  }
  
  document.addEventListener('DOMContentLoaded', init);
  