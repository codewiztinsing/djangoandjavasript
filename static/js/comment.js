const commentForm = document.getElementById("commentForm");
const body = document.getElementById("id_body");
const csrf  = document.getElementsByName("csrfmiddlewaretoken");
const url  = window.location.origin;
commentForm.addEventListener("submit",function(event){
    event.preventDefault();
    $.ajax({
        type:"POST",
        url:"",
        data : {
            'csrfmiddlewaretoken':csrf[0].value,
            "body":body.value

        },
        success : function(resp){
            window.location.href = window.location.origin; 


        },
        error: function(error){
            console.log(error)
        }
    })
})