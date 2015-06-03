window.onload=function() {
    var myImg = new Image();
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
            var img1 = document.createElement('img');
            var img2 = document.createElement('img');
            var img3 = document.createElement('img');
            document.getElementById('titreArticle1').innerHTML = response['titreArticle1'];
            document.getElementById('titreArticle2').innerHTML = response['titreArticle2'];
            document.getElementById('titreArticle3').innerHTML = response['titreArticle3'];
            img1.src = response['urlimage1'];
            document.getElementById('urlimage1').appendChild(img1);
            //img1.style.width = "291.328px";
            //img1.style.height = "187.281px";
            img1.className = "img-responsive";
            img2.src = response['urlimage2'];
            document.getElementById('urlimage2').appendChild(img2);
            //img2.style.width = "291.328px";
            //img2.style.height = "187.281px";
            img2.className = "img-responsive";
            img3.src = response['urlimage3'];
            document.getElementById('urlimage3').appendChild(img3);
            //img3.style.width = "291.328px";
            //img3.style.height = "187.281px";
            img3.className = "img-responsive";
            }
        }
    })
}