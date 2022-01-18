const back_Btn        =     document.getElementById("back-btn");
const update_Btn      =     document.getElementById("update-btn");
const delete_Btn      =     document.getElementById("delete-btn");



const spinnerBox      =     document.getElementById("spinner-box");
const postBox         =     document.getElementById("post-box");
const updateForm      =     document.getElementById("update-form");



const url                    =     window.location.href + "data/";
const urlUpdate              =     window.location.href + "update/";
const urlDelete              =     window.location.href + "delete/";



const titleInput      = document.getElementById("id_title");
const bodyInput       = document.getElementById("id_body");
const deleteForm      =     document.getElementById("deletePost");


const csrf     = document.getElementsByName("csrfmiddlewaretoken");


back_Btn.addEventListener('click',() => {
    history.back()
})

$.ajax({
    type : "GET",
    url:url,
    success: (response) => {
        console.log(response)
        spinnerBox.classList.add("hide_me");

        if (response.data.author == response.data.logged_in){
            update_Btn.classList.remove("hide_me");
            delete_Btn.classList.remove("hide_me");
        }
        else {
            console.log("diffrent")
        }

        const titleEl = document.createElement("h1");
        const bodyEl = document.createElement("p");
        titleEl.setAttribute("class","mt-2");



        bodyEl.setAttribute("class","mt-1")
        titleEl.setAttribute("id","title");
        bodyEl.setAttribute("id","body")


        titleEl.textContent = response.data.title;
        bodyEl.textContent = response.data.body;
        postBox.appendChild(titleEl);
        postBox.appendChild(bodyEl);

        titleInput.value = response.data.title
        bodyInput.value = response.data.body
    },
    error : (error) => {
        console.log(error)
    }
})

updateForm.addEventListener("submit",(event) => {
    console.log("Event",event)
    event.preventDefault()
    const title  =  document.getElementById("title");
    const body   = document.getElementById("body");    

    $.ajax({
        type : "POST",
        url : urlUpdate,
        headers:{
            
        },

        data : {
            'csrfmiddlewaretoken':csrf[0].value,
            "title":titleInput.value,
            "body":bodyInput.value
        },
        success : (response) => {
            handleAlert("success","post was successfully updated...")
            title.textContent = response.title
            body.textContent = response.body
            setInterval(() => {
                $("#updatePost").modal("hide")
            },1000)
           
        },
        error : (error) => {
            console.log(error)
        }
    })

 })

 deleteForm.addEventListener("submit",(event) => {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url : urlDelete,
            data : {
                'csrfmiddlewaretoken':csrf[0].value

            },
            success : (response) => {
                    window.location.href = window.location.origin; 
                    localStorage.setItem("title",response.title);
       
               

            },
            error : (error) => {
                console.log(error)
            }
        })
 })