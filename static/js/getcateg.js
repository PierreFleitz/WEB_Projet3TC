window.onload=function() {
    console.log("WOULI WOULOU")
    $.ajax({
        url: '/getarticlecat1',
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
            var img4 = document.createElement('img');
            var img5 = document.createElement('img');
            var img6 = document.createElement('img');
            document.getElementById('titreArticle1').innerHTML = response['titreArticle1'];
            document.getElementById('titreArticle2').innerHTML = response['titreArticle2'];
            document.getElementById('titreArticle3').innerHTML = response['titreArticle3'];
            document.getElementById('titreArticle4').innerHTML = response['titreArticle4'];
            document.getElementById('titreArticle5').innerHTML = response['titreArticle5'];
            document.getElementById('titreArticle6').innerHTML = response['titreArticle6'];
            img1.src = response['urlimage1'];
            document.getElementById('urlimage1').appendChild(img1);
            img1.style.width = "291.328px";
            img1.style.height = "187.281px";
            img2.src = response['urlimage2'];
            document.getElementById('urlimage2').appendChild(img2);
            img2.style.width = "291.328px";
            img2.style.height = "187.281px";
            img3.src = response['urlimage3'];
            document.getElementById('urlimage3').appendChild(img3);
            img3.style.width = "291.328px";
            img3.style.height = "187.281px";
            img4.src = response['urlimage4'];
            document.getElementById('urlimage4').appendChild(img4);
            img4.style.width = "291.328px";
            img4.style.height = "187.281px";
            img5.src = response['urlimage5'];
            document.getElementById('urlimage5').appendChild(img5);
            img5.style.width = "291.328px";
            img5.style.height = "187.281px";
            img6.src = response['urlimage6'];
            document.getElementById('urlimage6').appendChild(img6);
            img6.style.width = "291.328px";
            img6.style.height = "187.281px";
            }
        }
    })
}