const alertBox = document.getElementById("alert-box");

const handleAlert = (type,message) => {
    alertBox.innerHTML = `
        <div class = "alert alert-${type}">
            ${message}
        </div>
    `
}

