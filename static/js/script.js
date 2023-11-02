const dropdownMenu = document.getElementsByClassName("dropdownMenu");
const dropdownButton = document.getElementsByClassName("dropdownButton");

if (dropdownButton) {
    dropdownButton[0].addEventListener("click", () => {
        dropdownMenu[0].classList.toggle("show");
    });

    dropdownButton[1].addEventListener("click", () => {
        dropdownMenu[1].classList.toggle("show");
    });
}

const form1 = document.getElementById('form1');
const form2 = document.getElementById('form2');

