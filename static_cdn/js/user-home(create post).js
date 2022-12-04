//--------------Create Post Area start--------------




//----Functions Start----//
// Feeling Menu(笑脸按钮)
function feelingsMenuToggle(){
  feelingsmenu.classList.toggle("feelings-menu-height");
}


// Add image Btn(相机选择文件按钮)
var imageAdder = function(){
    var browser = document.getElementById('images-selector');
    var images = browser.getElementsByTagName('img');
    
    //Add click event to all images within image browser
    for(var i=0;i<images.length;i++){
        images[i].onclick = update;
    }
    
    //function to update the textarea
    function update(){
        var content = document.getElementById('message');
        content.value = content.value + ' <img src="'+this.src+'" />';  
    } 
}
// Refresh
window.onload = function(){
    imageAdder();
}

// ----Functions End-----//


