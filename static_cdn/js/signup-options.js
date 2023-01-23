const signup_tab_button = document.querySelectorAll(".signup-type-btn");
const signup_tab = document.querySelectorAll(".signup-tabshow");

function signup_tabs(panelIndex){
    signup_tab.forEach(function(node){
        node.style.display = "none";
    });
    signup_tab[panelIndex].style.display = "block";
}

signup_tabs(0);

//--Emphasize Active tab--//
$(".signup-type-btn").click(function(){
    $(this).addClass("active").siblings().removeClass("active");
});