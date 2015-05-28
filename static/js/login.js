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
	var prenomOk = verifPrenom(f.prenom);

	
	if(pseudoOk && mailOk && ageOk && nameOk && prenomOk){
		return true
	}
	else
	{
		alert("Veuillez remplir correctement tous les champs");
		return false;
	}
}

jQuery(document).ready(function() {
    $('#monForm').on('submit', function(e) {
        e.preventDefault(); // J'empêche le comportement par défaut du navigateur, c-à-d de soumettre le formulaire
 
        var $this = $(this);
 
        var mail = $('#mail').val();
        var password = $('#password').val();
 
        if(mail === '' || password === '') {
            alert('Les champs doivent êtres remplis');
        } else {
            $.ajax({
                url: '/login',
                type: 'POST',
                data: {
                	mail: mail,
                	password: password,
                
                dataType: 'json', // JSON
                success: function(data) {
                	alert('OK');
                	window.location.replace('/index');                   
                }
                }            	
        	})
    	}
	})
})