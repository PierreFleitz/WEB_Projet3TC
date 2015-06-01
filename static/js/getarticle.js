window.onload=function() {
        $.get("/item", function(data, status){
            alert("Data: " + data + "\nStatus: " + status);
        })
}