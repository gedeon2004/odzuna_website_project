// Script de base pour Odzuna
document.addEventListener("DOMContentLoaded", function () {
    console.log("Site Odzuna prêt.");

    // Exemple : message au clic du bouton newsletter
    const form = document.querySelector(".newsletter form");
    if (form) {
        form.addEventListener("submit", function (e) {
            alert("Merci pour votre inscription !");
        });
    }

    // Exemple : interactivité future (HTMX ou autre)
});


document.querySelectorAll('.favori-form').forEach(form => {
    form.addEventListener('submit', function (e) {
        e.preventDefault();
        fetch(this.action, {
            method: 'POST',
            headers: {
                'X-CSRFToken': this.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(res => res.json())
        .then(data => {
            alert(data.status === 'added' ? "Ajouté aux favoris !" : "Déjà dans vos favoris.");
        });
    });
});
