var prenomglob;
var nomglob;
var pseudoglob;
var mailglob;
var ageglob;

function surligne(champ, erreur)
{
	if(erreur)
		champ.style.border = "2px solid #f00",
		champ.style.backgroundColor = "#fba";
	else
		champ.style.border = "2px solid #00FF00",
		champ.style.backgroundColor = "#B0F2B6";
}

function verifPseudo(champ)
{
	if(champ.value.length < 2 || champ.value.length > 25)
	{
		surligne(champ, true);
		document.getElementById('erreurPseudo').innerHTML = "	Il faut un pseudo compris entre 2 et 25 caractères";
		document.getElementById('validPseudo').innerHTML = "";
		return false;
	}
	else
	{
		document.getElementById('validPseudo').innerHTML = "	Ce pseudo est valide ;)";
		document.getElementById('erreurPseudo').innerHTML = "";
		surligne(champ, false);
		return true;
	}
}

function verifName(champ)
{
	if(champ.value.length < 2 || champ.value.length > 25)
	{
		document.getElementById('erreurName').innerHTML = "	Ce n'est pas un un vrai nom dis donc !";
		document.getElementById('validName').innerHTML = "";
		surligne(champ, true);
		return false;
	}
	else
	{
		document.getElementById('validName').innerHTML = "	Très joli nom !";
		document.getElementById('erreurName').innerHTML = "";
		surligne(champ, false);
		return true;
	}
}

function verifMail(champ)
{
	var regex = /^[a-zA-Z0-9._-]+@[a-z0-9._-]{2,}\.[a-z]{2,4}$/;
	if(!regex.test(champ.value))
	{
		document.getElementById('erreurMail').innerHTML = "	Ce n'est pas une adresse mail dis donc !";
		document.getElementById('validMail').innerHTML = "";
		surligne(champ, true);
		return false;
	}
	else
	{
		document.getElementById('validMail').innerHTML = "	Ce mail est valide ;)";
		document.getElementById('erreurMail').innerHTML = "";
		surligne(champ, false);
		return true;
	}
}

function verifAge(champ)
	{
		var age = parseInt(champ.value);
		if(isNaN(age) || age < 5 || age > 111)
		{
			document.getElementById('erreurAge').innerHTML = "	Impressionnant comme âge !"
			surligne(champ, true);
			return false;
		}
		else
		{
			document.getElementById('erreurAge').innerHTML ="";
			surligne(champ, false);
			return true;
		}
	}
	
function verifPassword(champ) {
	if(champ.value.length < 5 ) {
		document.getElementById('erreurPassword').innerHTML = "	Le mot de passe doit être supérieur à 5 caractères !"
		document.getElementById('validPassword').innerHTML = "";
		surligne(champ, true);
		return false;
	}
	else{
		document.getElementById('validPassword').innerHTML = "	Ce mot de passe est suffisant";
		document.getElementById('erreurPassword').innerHTML = "";
		surligne(champ, false);
		return true;
	}
}

function verifForm(f)
{
	var pseudoOk = verifPseudo(f.pseudo);
	var mailOk = verifMail(f.mail);
	var ageOk = verifAge(f.age);
	var passwordOk = verifPassword(f.password);
	var nameOk = verifName(f.nom);
	var prenomOk = verifName(f.prenom);

	
	if(pseudoOk && mailOk && ageOk && nameOk && prenomOk){
		return true
	}
	else
	{
		alert("Veuillez remplir correctement tous les champs");
		return false;
	}
}
function get_classement(id) {
    var Classement;
    localStorage.setItem('Classement', id);
    console.log(localStorage.getItem('Classement'));
}

function get_categorie(id) {
    var Categorie;
    localStorage.setItem('Categorie',id);
}

jQuery(document).ready(function() {
	$('#monForm').on('submit', function(e) {
        e.preventDefault(); // J'empêche le comportement par défaut du navigateur, c-à-d de soumettre le formulaire

        var $this = $(this);

        var $pseudo1 = $('#pseudo1').val();
        var $password1 = $('#password1').val();

        if($pseudo1 === '' || $password1 === '') {
        	alert('Les champs doivent êtres remplis');
        } else {
        	$.ajax({
        		url: '/login',
        		type: 'POST',
        		dataType: 'json',
        		data: {
        			pseudo1:$pseudo1,
        			password1:$password1
        		},
        			success: function(response) {
                console.log(response);
                if(response == 'error') {
                	document.getElementById('erreurLogin').innerHTML = "Le mot de passe ou le login est incorrect";
                }
                else {
                    /* //prenomglob=response['prenom'];
                    nomglob= response ['nom'];
                    //pseudoglob = response['pseudo'];
                    mailglob = response ['mail'];
                    ageglob = response ['age'];
                    prenomglob=localStorage.getItem("plouf plouf");
                    localStorage.setItem("pseudoglob",response['pseudo']);
                    console.log(prenomglob + "kvof" + pseudoglob + mailglob); */
                	window.location.replace('/index');
                }
            }
        		})          	
        	}
        })
    })

jQuery(document).ready(function() {
	$('#inscription').on('submit', function(e) {
        e.preventDefault(); // J'empêche le comportement par défaut du navigateur, c-à-d de soumettre le formulaire

        var $this = $(this);

        var $prenom = $('#prenom').val();
        var $nom = $('#nom').val();
        var $pseudo = $('#pseudo').val();
        var $mail = $('#mail').val();
        var $age = $('#age').val();
        var $password = $('#password').val();

        /*if($mail === '' || $password === '') {
        	alert('Les champs doivent êtres remplis inscription');
        } else {*/
        	$.ajax({
        		url: '/signup',
        		type: 'POST',
        		dataType: 'json',
        		data: {
        			prenom:$prenom,
        			nom:$nom,
        			pseudo:$pseudo,
        			mail:$mail,
        			age:$age,
        			password:$password
        		},
        			success: function(response) {
                console.log(response);
                if(response == 'error') {
                	document.getElementById('erreurLogin').innerHTML = "Problème de post en inscription";
                }
                else {
                	console.log("Bien connecté")
                	window.location.replace('/index');
                }
            }
        		}) 
    })
})

jQuery(document).ready(function() {
	$('#addArticle').on('submit', function(e) {
        e.preventDefault(); // J'empêche le comportement par défaut du navigateur, c-à-d de soumettre le formulaire

        var $this = $(this);

        var $nomarticle= $('#nomarticle').val();
        var $catearticle = $('#catearticle').val();
        var $contenu = $('#contenu').val();
        var $urlimage = $('#urlimage').val();
        	$.ajax({
        		url: '/addarticle',
        		type: 'POST',
        		dataType: 'json',
        		data: {
        			nomarticle:$nomarticle,
        			catearticle:$catearticle,
        			contenu:$contenu,
                    urlimage:$urlimage
        		},
        			success: function(response) {
                console.log(response);
                if(response == 'error') {
                	document.getElementById('erreurarticle').innerHTML = "On verra";
                }
                else {
                	console.log("Bien envoyé")
                	window.location.replace('/index');
                    alert("Document bien posté");
                }
            }
        		}) 
    })
})