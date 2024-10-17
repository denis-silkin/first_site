var modal_you = document.querySelector(".modal_you");
var triggerInst = document.querySelector(".trigger-inst");
var closeButton_you = document.querySelector(".close-button_you");

function toggleModal_you() {
    modal_you.classList.toggle("show-modal_you");
}

function windowOnClick_you(event) {
    if (event.target === modal_you) {
        toggleModal_you();
    }
}

triggerInst.addEventListener("click", toggleModal_you);
closeButton_you.addEventListener("click", toggleModal_you);
window.addEventListener("click", windowOnClick_you);