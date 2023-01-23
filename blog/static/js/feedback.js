
// Create Post Menu （+）
var feedback_forum = document.getElementById("feedback-forum");
var feedback_open_btn = document.querySelector(".feedback-button");

// open form
feedback_open_btn.addEventListener('click', ()=>{
    openFeedbackForum();
});

function openFeedbackForum(){
    feedback_forum.style.display ='flex';
    body.style.overflow = 'hidden';
}

function closeFeedbackForum(){
    feedback_forum.style.display ='none';
    body.style.overflow = 'overlay';
}
