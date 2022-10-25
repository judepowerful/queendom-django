
// Create Post Menu （+）
var createpostmenu = document.getElementById("create-post-forum");
var createpost_open_btn = document.querySelector(".create-post-icon");
const body = document.querySelector("body");

var file_upload_area = document.querySelector(".file-upload");
var file_input = document.getElementById("image_input")
var delete_img_button = document.getElementById("delete-img-btn")

createpost_open_btn.addEventListener('click', ()=>{
    openCreatePostMenu();
});


function openCreatePostMenu(){
   createpostmenu.style.display ='flex';
   body.style.overflow = 'hidden';
}

function closeCreatePostMenu(){
    createpostmenu.style.display ='none';
    body.style.overflow = 'overlay';
}

file_upload_area.addEventListener('dragover', (event)=>{
    event.preventDefault();
    file_upload_area.classList.add('active');
});

file_upload_area.addEventListener('dragleave', (event)=>{
    file_upload_area.classList.remove('active');
});

file_upload_area.addEventListener('drop', (event)=>{
    event.preventDefault();
    file_upload_area.classList.remove('active');
    file_input.files = event.dataTransfer.files;
    displayImage();
});

file_input,addEventListener('change', function(){
    file = this.files;
    displayImage();
});

function displayImage(){
    let fileReader = new FileReader();
    fileReader.onload = () => {
        let fileURL = fileReader.result;
        let imgTag = `<img src="${fileURL}" alt="" class="post-img">`;
        let deleteTag = `<button id="delete-img-btn" class="fa-solid fa-trash" type="button" onclick="delete_input_files()"></button>`;
        file_upload_area.innerHTML = imgTag;
        file_upload_area.innerHTML += deleteTag;
        file_upload_area.classList.add('uploaded');
    };
    
    Array.from(file_input.files).forEach(file => {
        fileReader.readAsDataURL(file);
    });
}

function delete_input_files(){
    file_input.value = null;
    if(file_input.files.length == 0){
        let originTag = `<div class="icon" id="file-upload-item">
        <i class="fas fa-images"></i>
    </div>
    <div class="up-header" id="file-upload-item">
        Drag photos here
    </div>
    <label type="button" for="image_input" class="file-upload-button" id="file-upload-item">
        Upload from computer
    </label>`;
        file_upload_area.innerHTML = originTag;
        file_upload_area.classList.remove('uploaded');
    }
}
