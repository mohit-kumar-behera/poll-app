const choiceContainer = document.querySelector('.choice-container');

function vote(elem) {
    choice_id = elem.getAttribute('data-id');
    question_id = elem .getAttribute('question-id');
    $.ajax({
        type:'GET',
        url:"/home/vote/",
        data: {
            'choice_id':choice_id
        },
        success:function(json) {
            if(!json.alreadyVoted) {
                if(json.successfull) {
                    //alert("Successfully voted");
                    $(elem).addClass("choice__isVoted");
                    $(elem).parent().css('pointer-events','none');

                    var result_div = document.createElement("div");
                    var result_form = document.createElement("form");
                    var result_btn = document.createElement("button");
                    var result_btn_text = document.createTextNode("View Results");

                    result_div.className = "text-center mb-1";

                    result_form.action = "/home/";
                    result_form.method = "get"

                    result_btn.type = "submit";
                    result_btn.className = "btn btn-info";
                    result_btn.name = "resultBtn";
                    result_btn.value = question_id;

                    result_btn.appendChild(result_btn_text);
                    result_form.appendChild(result_btn);
                    result_div.appendChild(result_form);

                    $(elem).parent("ul").after(result_div);
                }
                else {
                    alert("Something went wrong");
                }
            }
            else {
                $("#message-modal #message").html("You already have voted. Refresh this page to apply changes");
                $("#message-modal").modal("show");
            }
        }
    });
}

choiceContainer.addEventListener('click', function(e) {
    const choiceElem = e.target.closest('.choice__li');
    if (!choiceElem) return;

    vote(choiceElem)
})