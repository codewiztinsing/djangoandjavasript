const first_div   = document.getElementById("first-div");
const post_box    = document.getElementById("post_box");
const spinner_box = document.getElementById("spinner-box");
const loadBtn     = document.getElementById("load-btn");
const endBox      = document.getElementById("end-box");

const title    = document.getElementById("id_title");
const body     = document.getElementById("id_body");
const csrf     = document.getElementsByName("csrfmiddlewaretoken");
const postForm = document.getElementById("post-form");
const url      = window.location.href


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');



const likeunlikeposts = () => {
    const likeunlikeforms = [...document.getElementsByClassName("like-unlike-form")];
    likeunlikeforms.forEach(form => form.addEventListener('submit',e =>{
        e.preventDefault();
        const clikedId = e.target.getAttribute('data-form-id');
        const clikedBtn = document.getElementById(`like-unlike-${clikedId}`);
        
     
        $.ajax({
            type:'POST',
            url:"likeunlike/",
            headers:{
                "X-CSRFToken": csrftoken
            },
            data : {
                
                'pk':clikedId
            },
            success : function(response){
        
                clikedBtn.textContent = response.liked ? `unlike(${response.count})`:`Like(${response.count})` 
            },
            error:function(error){
                console.log("error is ",error);
            }
        })
    }))
}


let visible = 3 ;
const getData = ()=> {

$.ajax({
    method : "GET",
    url : `/list/${visible}/`,
    success:function(resp){
        const data = resp.data
    
        setTimeout(() => {
            spinner_box.classList.add("hide_me")
            likeunlikeposts()
        },1000)
        data.forEach(element => {
            post_box.innerHTML += `
            <div class = "card mb-2" >
                <div class = "card-body">
                    <div class ="post-title">
                        <h5 class = "post-title">${element.title}</h5>
                           <hr class = "post-title-line" />
                    </div>
                <div class = "post-body">
                    <p class = "card-text">${element.body} </p>
                </div>
                    
                </div>
                <div class = "card-footer">
                    <div class = "box-view-comment-like">
                        <div class = "item-view-comment-like">
                            <a class = "btn btn-primary"  href = "${url}${element.id}" id = "box-view">View</a>
                        </div>

                        <div class = "item-view-comment-like">
                                     
                            <a class = "btn btn-primary" id ="box-comment" href=" ${url}comments/${element.id}/">comments</a>
                        </div>
                        <div class = "item-view-comment-like">
                            <form class = "like-unlike-form" data-form-id = ${element.id}> 
                                <div>
                                    <button style= "border-radius:100px;height:40px;width: 200px;background-color:rgb(205, 32, 228);" id = 'like-unlike-${element.id}'>${element.liked ? `unlike(${element.count}`:`like(${element.count})`}</button>
                                </div>
                            </form>

                        </div>
                    </div>
                    <div> 
                </div>
            </div>
            `
            
        });
        console.log(resp.size)
        if(resp.size === 0){
            endBox.textContent = "No post yet ..."
        }

        else if(resp.size <= visible){
            loadBtn.classList.add("hide_me");
            endBox.textContent = "No more post to load"

        }
    },
    error : function(err){
        console.log(err)
    
    }

})
}
loadBtn.addEventListener("click",()=>{
    spinner_box.classList.add("hide-me")
    visible += 3
    getData()
})


postForm.addEventListener('submit',e => {
    e.preventDefault();
    $.ajax({
        type : 'POST',
        url:'',
       
        data : {
            'csrfmiddlewaretoken':csrf[0].value,
            'title':title.value,
            'body':body.value
        },
        success  : function(response){
            post_box.insertAdjacentHTML('afterbegin',  

            `
            <div class = "card mb-2" >
                <div class = "card-body">
                    <h5 class = "card-title">${response.title}</h5>
                    <p class = "card-text">${response.body} </p>
                    
                </div>
                <div class = "card-footer">
                    <div class = "row">
                        <div class = "col-md-1 mt-2">
                            <a href = "${url}${response.id}" class = "btn btn-primary">View</a>
                        </div>

                        <div class = "col-md-1 mt-2">
                    
                            <a class = "btn btn-primary btn-outline text-center"href=" ${url}comments/${response.id}/">comments</a>
                        </div>
                        <div class = "col-md-1 mt-2">
                            <form class = "like-unlike-form" data-form-id = ${response.id}>
                           
                                    <button class = "btn btn-primary" id = 'like-unlike-${response.id}'>like(0)</button>
                            </form>
                        </div>
                    </div>
                    <div> 
                </div>
            </div>
        
            
            `)
            likeunlikeposts()
            $("#addPost").modal("hide");
            handleAlert("success","New post Added");
            postForm.reset()
        },
        error:function(error){
            $("#addPost").modal("hide");
            handleAlert("danger","oops ..somethings is wrong.....");
        }

    })

}
)

getData()