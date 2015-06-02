window.onload=function() {
    var img = document.createElement('img');
    
    $.ajax({
        url: '/itemarticle',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            console.log(response);
            if(response == 'error') {
                document.getElementById('erreurarticle').innerHTML = "On verra";
            }
            else {
            document.getElementById('titreArticle').innerHTML = response['titreArticle'];
            document.getElementById('contenuArticle').innerHTML = response['contenuArticle'];
            img.src = response['urlimage'];
            document.getElementById('urlimage').appendChild(img);
            }
        }
    })
}

function displayImg(link) {

    var img = new Image(),
        overlay = document.getElementById('overlay');

    img.addEventListener('load', function() {
        overlay.innerHTML = '';
        overlay.appendChild(img);
    }, false);

    img.src = link.href;
    overlay.style.display = 'block';
    overlay.innerHTML = '<span>Chargement en cours...</span>';

}