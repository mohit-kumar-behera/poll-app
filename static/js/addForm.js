var addChoiceBtn = document.getElementById("addChoice");
var pollForm = document.getElementsByClassName("pollForm")[0];
var choicesElem = document.getElementsByClassName("choice");
var len_choicesElem = choicesElem.length;

addChoice.onclick = function() {
    len_choicesElem += 1; 
    var divElem = document.createElement("div");
    divElem.className = "form-group";
    var inputElem = document.createElement("input");
    inputElem.type = "text";
    inputElem.className = "form-control choice";
    inputElem.placeholder = "Enter Your Choice " + len_choicesElem;
    inputElem.name = "choice_" + len_choicesElem;
    inputElem.autocomplete = "off";
    divElem.appendChild(inputElem)
    $(".form-group:last").after(divElem);
}