addEventListener("DOMContentLoaded", function() {
    const navHome = document.getElementById("nav-home")
    const navTeams = document.getElementById("nav-teams")
    const navMatchs = document.getElementById("nav-matches")


    navHome.addEventListener("click" , function() {
        navHome.classList.add(" active")
        navTeams.classList.remove("active")
        navMatchs.classList.remove("active")
    })

    navTeams.addEventListener("click" , function() {
        navHome.classList.remove("active")
        navTeams.classList.add("active")
        navMatchs.classList.remove("active")
    })

    navMatchs.addEventListener("click", function() {
        navHome.classList.remove("active");
        navTeams.classList.remove("active");
        navMatchs.classList.add("active");
    });

})