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

    console.log("WORDS",e.detail['words']);
    console.log(speechSegment.entities);
    
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

