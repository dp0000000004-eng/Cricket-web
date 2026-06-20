const imgCont = document.getElementById("img-cont")
const prevBtn = document.getElementById("prev")
const nextBtn = document.getElementById("next")
const frontImg = [
    "/static/pl/img/cmp1.avif", 
    "/static/pl/img/ent.avif",
    "/static/pl/img/vk.avif",
    "/static/pl/img/vk2.avif"
]
let slideIndex = 0

intilaizer(frontImg)


function intilaizer(arr) {
    imgCont.innerHTML = `<img src=${arr[slideIndex]}>`
}

prevBtn.addEventListener("click", function() {
    if (slideIndex > 0) {
        slideIndex--
    }
    intilaizer(frontImg)
})


nextBtn.addEventListener("click", function() {
    if((frontImg.length-1) > slideIndex){
        slideIndex++
    }
    intilaizer(frontImg)
})