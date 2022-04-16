var notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

for(var i = 0; i < notes.length; i++) {
  document.getElementById(notes[i])
  .addEventListener("click", click);
}

function click() {
  const synth = new Tone.Synth().toDestination()
  synth.triggerAttackRelease(event.target.id, '32n')
  
  Tone.Transport.start();
  Tone.Transport.stop();
}


function sound(note) {
  const synth = new Tone.Synth().toDestination()
  synth.triggerAttackRelease(note, '32n')
  
  Tone.Transport.start();
  Tone.Transport.stop();
}

Mousetrap.bind('a', function() {sound('C4')});
Mousetrap.bind('s', function() {sound('D4')});
Mousetrap.bind('d', function() {sound('E4')});
Mousetrap.bind('f', function() {sound('F4')});
Mousetrap.bind('g', function() {sound('G4')});
Mousetrap.bind('h', function() {sound('A4')});
Mousetrap.bind('j', function() {sound('B4')});
Mousetrap.bind('k', function() {sound('C5')});
