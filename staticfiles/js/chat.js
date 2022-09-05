
//---------------------Chat Page Start-------------------------
// Search Bar search message(有bug)
const messages = document.querySelector('.message-sender-message');
const chatMessage = messages. querySelectorAll('.message-sender-message');
const messageSearch = document.querySelector('#message-search'); // input
const searchMessage = () => {
  console.log('yes');
  const val = messageSearch.value.toLowerCase();  // val = input
  console.log(val); // print
  messageSearch.forEach(chat =>{
    let name = chat.querySelector('.sender-name').textContent.toLowerCase();
    
  })
}
//Search Chat
messageSearch.addEventListener('keyup', searchMessage);
