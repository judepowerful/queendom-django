
// Create Post Menu （+）
var createpostmenu = document.getElementById("create-post-forum");
var createpost_open_btn = document.querySelector(".create-post-icon");
const body = document.querySelector("body");

var file_upload_area = document.querySelector(".file-upload");
var delete_img_button = document.getElementById("delete-img-btn");


// open form
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


// drag and drop css
file_upload_area.addEventListener('dragover', (event)=>{
    event.preventDefault();
    file_upload_area.classList.add('active');
});

file_upload_area.addEventListener('dragleave', (event)=>{
    file_upload_area.classList.remove('active');
});


let filelist_url = [];
let filelist_file = new DataTransfer();


var file_input = document.getElementById("image_input") // file input html

// upload by drag and drop
file_upload_area.addEventListener('drop', async (event)=>{
    if(file_input.files.length == 0){
        event.preventDefault();

        // css
        file_upload_area.classList.remove('active');

        // add file to input
        for(var i=0; i<event.dataTransfer.files.length; i++){
            filelist_file.items.add(event.dataTransfer.files[i]);
        }

        file_input.files = event.dataTransfer.files;

        // push url to list for purpose of display
        let filelist = file_input.files;
        for(var i=0; i<filelist.length; i++){
            const fileURL = await read_file_to_url(filelist[i]);
            filelist_url.push(fileURL);
        }

        changeHTMLToSlider();
        displayImage();
        setSplideUp(0);
    }
});

// upload by click button
file_input.addEventListener('change', async (event)=>{
    // read files
    let filelist = file_input.files;

    // store locally
    for(var i=0; i<filelist.length; i++){
        filelist_file.items.add(filelist[i]);
    }

    // push url to list for purpose of display
    for(var i=0; i<filelist.length; i++){
        const fileURL = await read_file_to_url(filelist[i]);
        filelist_url.push(fileURL);
    }

    changeHTMLToSlider();
    displayImage();
    setSplideUp(0);
});

// function to convert file to url for purpose of display
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
    }
    
    changeHTMLToSlider();
    displayImage();
    setSplideUp(filelist_url.length - 1);

    // update total file input html
    file_input.files = filelist_file.files;
});


function changeHTMLToSlider(){
    // change the uploaded area ready to show images
    file_upload_area.innerHTML = "";
    file_upload_area.classList.add('uploaded');

    // add "splide" slider to innerHTML
    var img_slider =`<section id="upload_img" class="splide" aria-label="Beautiful Images">
                        <div class="splide__track">
                                <ul class="splide__list" id="upload__list">

                                </ul>
                        </div>
                    </section>`;
    file_upload_area.innerHTML += img_slider;

    // modify images buttons
    let addBtn = `<label style="display: flex; justify-content: center; align-items: center;" type="button" for="add_more_imgs" class="img-btn-bg fa-solid fa-plus" id="add-img-btn"></label>`;
    let deleteBtn = `<button id="delete-img-btn" class="img-btn-bg fa-solid fa-trash" type="button" onclick="delete_input_files()"></button>`;
    file_upload_area.innerHTML += addBtn;
    file_upload_area.innerHTML += deleteBtn;
}


function displayImage(){
    // locate ul list in image slider html
    var img_list = document.getElementById("upload__list");

    // show images, add images into slider
    Array.from(filelist_url).forEach(fileURL =>{
        let imgTag =`<li class="splide__slide">
                        <img src="${fileURL}" alt="" class="post-img forum-post-img">
                    </li>`;
        img_list.innerHTML += imgTag;
    })
}

function setSplideUp(number){
    // set splide up
    new Splide( '#upload_img', {
        start : number,
    } ).mount();
}



function delete_input_files(){
    var active_img = document.getElementById("upload__list").getElementsByClassName("is-active")[0];
    var active_img_index_char = active_img.id.charAt(active_img.id.length - 1);
    var active_img_index = parseInt(active_img_index_char) - 1;
    
    // remove the file that currently looking at
    filelist_file.items.remove(active_img_index);
    file_input.files = filelist_file.files;
    
    // also remove the view
    filelist_url.splice(active_img_index, 1);
    
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
        displayImage();
        setSplideUp(active_img_index - 1);
    }
}
