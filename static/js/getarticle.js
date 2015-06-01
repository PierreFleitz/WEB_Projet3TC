window.onload=function() {
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
            }
        }
    })
}