//-----------Navigation Bar Start-------------

//----nav bar右边的3个btn Start----//
// Create Post Menu （+）
var createpostmenu = document.querySelector(".createpost-menu");

function createpostMenuToggle(){
  createpostmenu.classList.toggle("createpost-menu-height");
}


// Setting Menu (用户头像)
var settingsmenu = document.querySelector(".settings-menu");

function settingsMenuToggle(){
  settingsmenu.classList.toggle("settings-menu-height");
}

// Navigation Menu （铃铛）
var navigationsmenu = document.querySelector(".navigations-menu");

function navigationsMenuToggle(){
  navigationsmenu.classList.toggle("navigations-menu-height");
}
// 铃铛按钮上的Notification-Number
const messagesNotification = document.querySelector('#messages-notification');

messagesNotification.addEventListener('click', () =>{ // Click Event
  // Click -> notification count = none
  messagesNotification.querySelector('.notification-count').style.display = 'none';
})
const navBtn = document.querySelectorAll(".nav-tab");
const nav = document.querySelectorAll(".nav-tabShow");
//----nav bar右边的3个btn End----//



//--- Functions Start----//
// Create Post
createBtn.addEventListener('click', ()=>{
  createpostMenuToggle();
})

//--- Functions End----//