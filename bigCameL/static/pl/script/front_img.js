const imgCont = document.getElementById("img-cont")
const prevBtn = document.getElementById("prev")
const nextBtn = document.getElementById("next")
const frontImg = document.querySelectorAll("img")
let slideIndex = 0
let autoPlay 

intilaizer(frontImg)

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
})


nextBtn.addEventListener("click", function() {
    frontImg[slideIndex].classList.remove("displaySlide")
    slideIndex++
    
    if (slideIndex > (frontImg.length - 1)){
        slideIndex = 0
    }
    intilaizer(frontImg)
})


function startAutoPlay(){
    autoPlay = setInterval(() => {
        (slideIndex + 1 ) % frontImg.length
        intilaizer(frontImg)
    }, 3000)

}

startAutoPlay()