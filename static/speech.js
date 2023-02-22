// Implement a listener for speech segment updates
window.onload=function(){
 
var button = document.getElementsByTagName("push-to-talk-button")[0];

button.addEventListener("speechsegment", (e) => {
  const speechSegment = e.detail;

  // Check if the speech segment is the final segment
  if (speechSegment.isFinal) {
    const words = speechSegment.words;

    // Make POST request to save_audio endpoint
    fetch('/save_audio', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        words: words
      })
    })
    .then(response => {
      // Handle response from server
      let url = '/temp/output.mp3';

      // create an Audio object and set the source to the URL
      let audio = new Audio(url);

      // play the audio file
      audio.play();

      console.log(response);
    })
    .catch(error => {
      console.error(error);
    }); 
    }

    
    speechSegment.entities.forEach(entity => {
      
      let select = document.getElementById(entity.type);  
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
  });

  


}

