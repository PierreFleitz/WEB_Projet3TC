window.onload=function() {
        $.ajax({
        		url: '/item',
        		type: 'GET',
        		dataType: 'json',
        		success: function(response) {
                    console.log(response);
                if(response == 'error') {
                	document.getElementById('erreurarticle').innerHTML = "On verra";
                }
                else {
                	console.log("Bien affiché  ")
                	window.location.replace('/item');
                    alert("Document bien affiché");
                }
            }
        		}) 
}