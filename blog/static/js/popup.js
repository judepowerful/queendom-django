
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


let filelist_url = [];
let filelist_file = new DataTransfer();
let imgIndex = 0;

// upload by drag and drop
file_upload_area.addEventListener('drop', async (event)=>{
    if(file_input.files.length == 0){
        event.preventDefault();

        file_upload_area.classList.remove('active');

        // add file to input
        for(var i=0; i<event.dataTransfer.files.length; i++){
            filelist_file.items.add(event.dataTransfer.files[i]);
        }

        file_input.files = event.dataTransfer.files;

        let filelist = file_input.files;
        for(var i=0; i<filelist.length; i++){
            const fileURL = await read_file_to_url(filelist[i]);
            filelist_url.push(fileURL);
        }

        displayImage();
    }
});

// upload by click button
file_input.addEventListener('change', async (event)=>{

    let filelist = file_input.files;

    for(var i=0; i<filelist.length; i++){
        filelist_file.items.add(filelist[i]);
    }

    for(var i=0; i<filelist.length; i++){
        const fileURL = await read_file_to_url(filelist[i]);
        filelist_url.push(fileURL);
    }
    displayImage();
});

// add more files
var more_file_input = document.getElementById("add_more_imgs");
more_file_input.addEventListener('change', async (event)=>{
    let morefilelist = more_file_input.files;
    for(var i=0; i<morefilelist.length; i++){
        // update stored file list
        filelist_file.items.add(morefilelist[i]);
        // update stored file list url
        const fileURL = await read_file_to_url(morefilelist[i]);
        filelist_url.push(fileURL);
        // add a new img tag
        let imgTag = `<img src="${fileURL}" alt="" class="post-img forum-post-img">`;
        file_upload_area.innerHTML += imgTag;
    }
    file_input.files = filelist_file.files;

    // show the newly uploaded img
    let images = document.getElementsByClassName("forum-post-img");
    imgIndex = images.length-1
    change_img_index(0);
});

function changeHTMLToSlider(){
    // change the uploaded area ready to show images
    file_upload_area.innerHTML = "";
    file_upload_area.classList.add('uploaded');

    // show images
    Array.from(filelist_url).forEach(fileURL =>{
        let imgTag = `<img src="${fileURL}" alt="" class="post-img forum-post-img">`;
        file_upload_area.innerHTML += imgTag;
    })

    let addBtn = `<label style="display: flex; justify-content: center; align-items: center;" type="button" for="add_more_imgs" class="img-btn-bg fa-solid fa-plus" id="add-img-btn"></label>`;
    let deleteBtn = `<button id="delete-img-btn" class="img-btn-bg fa-solid fa-trash" type="button" onclick="delete_input_files()"></button>`;
    let prev_btn = `<button id="prev-img-btn" class="img-btn-bg fa-solid fa-angle-left" type="button" onclick="change_img_index(-1)"></button>`;
    let next_btn = `<button id="next-img-btn" class="img-btn-bg fa-solid fa-angle-right" type="button" onclick="change_img_index(1)"></button>`;
    file_upload_area.innerHTML += addBtn;
    file_upload_area.innerHTML += deleteBtn;
    file_upload_area.innerHTML += next_btn;
    file_upload_area.innerHTML += prev_btn;
}

function displayImage(){

    changeHTMLToSlider();

    // initially view img at 0 index
    imgIndex = 0;

    // and show images
    change_img_index(0);
}


const read_file_to_url = (inputFile) => {
    const temporaryFileReader = new FileReader();
  
    return new Promise((resolve, reject) => {
      temporaryFileReader.onerror = () => {
        temporaryFileReader.abort();
        reject(new DOMException("Problem parsing input file."));
      };
  
      temporaryFileReader.onload = () => {
        resolve(temporaryFileReader.result);
      };
      temporaryFileReader.readAsDataURL(inputFile);
    });
};

function delete_input_files(){

    // remove the file that currently looking at
    filelist_file.items.remove(imgIndex);
    file_input.files = filelist_file.files;
    
    // also remove the view
    filelist_url.splice(imgIndex, 1);
    
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
    } else {
        changeHTMLToSlider();
        if (imgIndex > 0){
            imgIndex -= 1;
        }
        change_img_index(0);
    }
}

function change_img_index(n){
    let images = document.getElementsByClassName("forum-post-img");
    imgIndex += n;
    if(imgIndex <= images.length && imgIndex >= 0){
        show_img_index(imgIndex, images);
        show_nav_arrow();
    }
}

function show_img_index(i, images){
    // make all images to disappear
    for (y = 0; y < images.length; y++) {
        images[y].style.display = "none";
    }
    // make target visible
    images[i].style.display = "block";
}

function show_nav_arrow(){
    let nextBtn = document.getElementById("next-img-btn");
    let prevBtn = document.getElementById("prev-img-btn");
    if(filelist_url.length >= 2){
        // viewing first image
        if(imgIndex == 0){
            nextBtn.style.display = "block";
            prevBtn.style.display = "none";
        }
        // viewing last image
        else if(imgIndex == filelist_url.length - 1){
            nextBtn.style.display = "none";
            prevBtn.style.display = "block";
        }
        // viewing middle images
        else {
            nextBtn.style.display = "block";
            prevBtn.style.display = "block";
        }
    }
    else {
        nextBtn.style.display = "none";
        prevBtn.style.display = "none";
    }
}