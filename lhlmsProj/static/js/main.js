const popupbtn = document.querySelector('.popupbtn');

const popup = document.querySelector('.popup-wrapper');

const popupclose = document.querySelector('.popup-close');

// popup

popupbtn.addEventListener('click',() =>{

    popup.style.display = "block";

    console.log("opening modal");

});

popupclose.addEventListener('click', () => {

    popup.style.display = 'none';

});