//-----Friends Profile Start----

// Profile Friend Menu(Friend按钮)
var friendmenu = document.querySelector(".profile-friend-menu");

function friendMenuToggle(){
  friendmenu.classList.toggle("profile-friend-menu-height");
}

const tabBtn = document.querySelectorAll(".profile-tabs");
const tab = document.querySelectorAll(".profile-tabshow");

function profile_tabs(panelIndex){
    tab.forEach(function(node){
        node.style.display = "none";
    });
    tab[panelIndex].style.display = "block";
}

profile_tabs(0);

//--Emphasize Active tab--//
$(".profile-tabs").click(function(){
    $(this).addClass("active").siblings().removeClass("active");
});
