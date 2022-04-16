document.getElementById("play-button")
  .addEventListener("click", click);

function click() {
  if(event.target.innerHTML == "Play") {
    event.target.innerHTML = "Stop"
    
    const synth = new Tone.Synth().toDestination()
    synth.triggerAttackRelease('C4', '8n')
    
    Tone.Transport.start();
  } else {
    event.target.innerHTML = "Play";
    
    Tone.Transport.stop();
  }
}


// Error: The AudioContext was not allowed to start. It must be resumed (or created) after a user gesture on the page. <URL>

/*
const synth = new Tone.Synth().toMaster()
synth.triggerAttackRelease('C4', '8n')

document.getElementById("play-button").addEventListener("click", function() {
  if (Tone.Transport.state !== 'started') {
    Tone.Transport.start();
  } else {
    Tone.Transport.stop();
  }
});
*/