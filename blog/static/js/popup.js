
// Create Post Menu （+）
var createpostmenu = document.getElementById("create-post-forum");
var createpost_open_btn = document.querySelector(".create-post-icon");


createpost_open_btn.addEventListener('click', ()=>{
    openCreatePostMenu();
})


function openCreatePostMenu(){
   createpostmenu.style.display ='block';
}

function closeCreatePostMenu(){
    createpostmenu.style.display ='none';
 }
