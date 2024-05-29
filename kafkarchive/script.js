let cont;

function searching() {
    let amogus = document.forms["searchbar"]["searchcontent"].value;
    cont = document.getElementById("searchbar1").value;
    if (amogus == "") {
        alert("ඞ");
        return false;
    } else {
        window.open("https://www.google.com/search?q="+cont, '_blank');
        return false;
    }
}