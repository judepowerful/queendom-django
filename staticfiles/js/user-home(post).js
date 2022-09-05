//-----------User Home Page All Post Area start-----------

// ---Define Variables Start---//
// Create Post
let createBtn = document.querySelector('.create-post-icon');
// Block Menu
var blockmenu = document.querySelector(".block-menu");
function blockMenuToggle(){
blockmenu.classList.toggle("block-menu-height");
}
// delect Menu
let delectButton = document.querySelector('.delect-choice');
let selfmorelist = document.querySelector('.selfmore-menu');
let delectlist = document.querySelector('.delect-menu');
let delectbtn = document.querySelector('.delect-btn');
let postList = document.querySelector('.self-post-container');
let cancelbtn = document.querySelector('.cancel-btn');
let privacyButton = document.querySelector('.privacy-choice');
// Friend More
let friendmorelist = document.querySelector('.friendmore-menu');
let reportButton = document.querySelector('.report-choice');
let reportbtn = document.querySelector('.reportbtn');
// Create Post的Feelings Menu
var feelingsmenu = document.querySelector(".feelings-menu");

// Post右上角的friendmore Menu
var friendmoremenu = document.querySelector(".friendmore-menu");

// ---Define Variables End---//




// -----Functions Start-----//
//--Self Post Start
//Self Post More menu
var selfmoremenu = document.querySelector(".selfmore-menu");

function selfmoreMenuToggle(){
  selfmoremenu.classList.toggle("selfmore-menu-height");
}
// Self Post More Menu中的Delect Menu
var delectmenu = document.querySelector(".delect-menu");
function delectMenuToggle(){
  delectmenu.classList.toggle("delect-menu-height");
}
// Delect Self Post
delectButton.addEventListener('click', ()=>{
  selfmoreMenuToggle();
  delectMenuToggle();
})
delectbtn.addEventListener('click', ()=>{
  delectMenuToggle();
  postList.remove();
})
// Cancel to Delect Self Post
cancelbtn.addEventListener('click', ()=>{
  delectMenuToggle();
})
// Privacy Btn Trigger
privacyButton.addEventListener('click', ()=>{
  selfmoreMenuToggle();
  blockMenuToggle();
})
//--Self Post End


// --Friend Post More Start
function friendmoreMenuToggle(){
  friendmoremenu.classList.toggle("friendmore-menu-height");
}
// FriendPost More Menu中的report Menu
var reportmenu = document.querySelector(".report-menu");
function reportMenuToggle(){
  reportmenu.classList.toggle("report-menu-height");
}
// Friend Post report successMenu
var reportsuccessmenu = document.querySelector(".report-success-menu");
function reportsuccessMenuToggle(){
  reportsuccessmenu.classList.toggle("report-success-menu-height");
}
// Friend more Trigger
reportButton.addEventListener('click', ()=>{
  friendmoreMenuToggle();
  reportMenuToggle();
})
reportbtn.addEventListener('click', ()=>{
  reportsuccessMenuToggle();
  reportMenuToggle();
})
//---Friend Post More End
// -----Functions End-----//









