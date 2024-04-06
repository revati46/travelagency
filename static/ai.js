function generateTrip() {
  var location = document.getElementById("location").value;
  var interest = document.getElementById("interest").value;
  var duration = document.getElementById("duration").value;
  var budget = document.getElementById("budget").value;

  var data = {
      location: location,
      interest: interest,
      duration: duration,
      budget: budget
  };

  $.ajax({
      type: "POST",
      url: "/generate-text",
      data: data,
      success: function(response) {
          document.getElementById("generated-text").innerHTML = response.generated_text;
      }
  });
}

  