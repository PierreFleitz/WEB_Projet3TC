window.onload=function() {
    var Classement =localStorage.getItem('Classement');
    console.log(Classement)
    console.log("PLOUF")
    $.ajax({
        url: '/itemarticle',
        type: 'POST',
        dataType: 'json',
        data: {
                Classement:Classement
            },
        success: function(response) {
            console.log(response);
            if(response == 'error') {
                document.getElementById('erreurarticle').innerHTML = "On verra";
            }
            else {
            var img = document.createElement('img');
            document.getElementById('titreArticle').innerHTML = response['titreArticle'];
            document.getElementById('contenuArticle').innerHTML = response['contenuArticle'];
            img.src = response['urlimage'];
            document.getElementById('urlimage').appendChild(img);
            img.style.width = "400px";
            img.style.height = "200px";
            }
        }
    })
}