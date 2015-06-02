window.onload=function() {
    $.ajax({
        url: '/itemarticleindex',
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            console.log(response);
            if(response == 'error') {
                document.getElementById('erreurarticle').innerHTML = "On verra";
            }
            else {
            document.getElementById('titreArticle1').innerHTML = response['titreArticle1'];
            document.getElementById('titreArticle2').innerHTML = response['titreArticle2'];
            document.getElementById('titreArticle3').innerHTML = response['titreArticle3'];
            }
        }
    })
}