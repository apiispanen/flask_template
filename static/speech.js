// Implement a listener for speech segment updates
window.onload=function(){
 
var button = document.getElementsByTagName("push-to-talk-button")[0];

if (button){
// SPACE BAR SUBSTITUTE FOR BUTTON PUSH
document.addEventListener("keydown", (event) => {
  // Check if the currently focused element is a textarea element
  const focusedElement = document.activeElement;
  const isTextarea = focusedElement.tagName === "TEXTAREA";
  
  if (event.key === ' ' && !isTextarea) {
    event.preventDefault();
    button.click();
  }
});

document.addEventListener("keyup", (event) => {
  if (event.key === ' ') {
    button.release();
  }
});

// END SPACE BAR SUBSTITUTE FOR BUTTON PUSH


// NOW SPEECH SPEECH SPEEEEECCCHHH
button.addEventListener("speechsegment", (e) => {
  
  const speechSegment = e.detail;

      // OLD JS
      speechSegment.entities.forEach(entity => {
      
        let select = document.getElementById(entity.type);  
        console.log(select);
        let options = Array
          .from(select.getElementsByTagName("option"))
          .map(option => option.innerHTML);
        
        const found = options
          .find(option => 
                entity
                .value
                .toLowerCase()
                .startsWith(option.toLowerCase()));
        
        if (found) select.value = found;
      })





  // Check if the speech segment is the final segment
  if (speechSegment.isFinal) {
    const words = speechSegment.words;
    const wordsString = speechSegment.words.map(word => word.value).join(' ');

    // ADD TO PROMPT

    const inputElement = document.querySelector('#response textarea');

    // Set the value of the input element
    inputElement.value = wordsString;
  
    // Make POST request to save_audio endpoint
    save_audio(wordsString);
    }


  });


// IF SOMEONE FILLS OUT THE PROMPT AND WANTS TO RESEND:
const responseTextArea = document.querySelector("#response textarea");
// add an event listener for when the user submits the form
responseTextArea.addEventListener("keydown", function(event) {
  // check if the user pressed the "Enter" key
  if (event.key === "Enter") {
    event.preventDefault();
    const responseText = responseTextArea.value;
    console.log(responseText);
    // call your desired function here
    var airesponse = save_audio(responseText);

  }
});
function return_prompt(audio, response) {


};


// define the function that you want to perform
function save_audio(words) {

  // code to perform the desired function goes here
  return fetch('/save_audio', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      words: words
    })
  })  .then(response => response.json())
  .then(data => {
    const audioContent = data.audioContent;
    const audioSrc = `data:audio/mpeg;base64,${audioContent}`;
    const audio = new Audio(audioSrc);
    const airesponse = data.airesponse;
    console.log(airesponse);
    const airesponseTextArea = document.querySelector("#airesponse textarea");
    airesponseTextArea.value = airesponse;


    audio.play();
  })
  .catch(error => {
    console.error(error);
  });
  
  
  
    
  console.log("Your function has been performed!");
}
};

window.onload.resize=function() {
  var scrollWidth = $('.tbl-content').width() - $('.tbl-content table').width();
  $('.tbl-header').css({'padding-right':scrollWidth});
};


var hoverlog = document.getElementById("hoverlog");
var log = document.getElementById("log");

hoverlog.onclick=function(){
  $("#log").slideToggle( "slow", function() {
    // Animation complete.
  });

}



}

