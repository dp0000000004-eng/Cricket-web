const imgCont = document.getElementById("img-cont")
const prevBtn = document.getElementById("prev")
const nextBtn = document.getElementById("next")
const frontImg = document.querySelectorAll("img")
let slideIndex = 0
let intervalId = null 

addEventListener("DOMContentLoaded", () => {
    intilaizer(frontImg)
    startAutoPlay()
})

function intilaizer(arr) {
    frontImg[slideIndex].classList.add("displaySlide")
}

prevBtn.addEventListener("click", function() {
    frontImg[slideIndex].classList.remove("displaySlide")
    slideIndex--
    if (slideIndex < 0) {
        slideIndex = (frontImg.length - 1)
    }
    intilaizer(frontImg)
    clearInterval(intervalId)
})


nextBtn.addEventListener("click", function () {
    frontImg[slideIndex].classList.remove("displaySlide")
    slideIndex++
    
    if (slideIndex > (frontImg.length - 1)){
        slideIndex = 0
    }
    intilaizer(frontImg)
    clearInterval(intervalId)
})


function startAutoPlay(){
    intervalId = setInterval(() => {
        frontImg[slideIndex].classList.remove("displaySlide")
        slideIndex++
    
        if (slideIndex > (frontImg.length - 1)){
            slideIndex = 0
        }
    intilaizer(frontImg)
    }, 5000)

}
