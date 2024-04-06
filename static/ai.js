function incrementDuration() {
    var durationInput = document.getElementById('duration');
    durationInput.value = parseInt(durationInput.value) + 1;
  }
  
  function decrementDuration() {
    var durationInput = document.getElementById('duration');
    if (parseInt(durationInput.value) > 1) {
      durationInput.value = parseInt(durationInput.value) - 1;
    }
  }
  