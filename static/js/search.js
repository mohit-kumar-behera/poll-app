$(function(){
    $("#searchPoll").keyup(function(){
        var value = $(this).val().toLowerCase()
        $(".container.polls .question").filter(function(){
            $(this).parent().parent().toggle($(this).text().toLowerCase().indexOf(value) > -1)
        })
    });
});