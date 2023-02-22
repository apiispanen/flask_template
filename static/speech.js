// Implement a listener for speech segment updates
window.onload=function(){
 
var button = document.getElementsByTagName("push-to-talk-button")[0];
// button.addEventListener('mouseup', (e) => {
//   e.preventDefault();
//   for(var b in window) { 
//     if(window.hasOwnProperty(b)) console.log(b); 
//   }


//   return false;  });
  button.addEventListener("speechsegment", (e) => {
    const speechSegment = e.detail;
    const words = speechSegment['words'];
  
    console.log("WORDS", words);
    console.log(speechSegment.entities);

      // Make POST request to save_audio endpoint
  fetch('/save_audio', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      words: words
    })
  }).then(response => {
    // Handle response from server
    console.log(response);
  }).catch(error => {
    console.error(error);
  });

    
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

