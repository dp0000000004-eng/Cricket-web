const imgCont = document.getElementById("img-cont")
const prevBtn = document.getElementById("prev")
const nextBtn = document.getElementById("next")
const frontImg = document.querySelectorAll("#img")
console.log(frontImg)
let slideIndex = 0
let intervalId = null 

addEventListener("DOMContentLoaded", () => {
    initializer(frontImg)
    startAutoPlay()
})


function initializer(arr) {
    frontImg[slideIndex].classList.add("displaySlide")
}

prevBtn.addEventListener("click", function() {
    frontImg[slideIndex].classList.remove("displaySlide")
    slideIndex--
    if (slideIndex < 0) {
        slideIndex = (frontImg.length - 1)
    }
    initializer(frontImg)
    clearInterval(intervalId)
})


nextBtn.addEventListener("click", function () {
    frontImg[slideIndex].classList.remove("displaySlide")
    slideIndex++
    
    if (slideIndex > (frontImg.length - 1)){
        slideIndex = 0
    }
    initializer(frontImg)
    clearInterval(intervalId)
})


function startAutoPlay(){
    intervalId = setInterval(() => {
        frontImg[slideIndex].classList.remove("displaySlide")
        slideIndex++
    
        if (slideIndex > (frontImg.length - 1)){
            slideIndex = 0
        }
    initializer(frontImg)
    }, 5000)

}
