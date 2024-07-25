<html>
<head>
  <script src="jquery-3.4.1.min.js"></script>
  <style>
    h1 {
      font-family: Arial, Helvetica, sans-serif;
      font-size: 5em;
      font-weight: bold;
    }
    .button {
      background-color: #4CAF50;
      border: none;
      color: white;
      padding: 32px 64px;
      text-align: center;
      text-decoration: none;
      display: inline-block;
      font-family: Arial, Helvetica, sans-serif;
      font-size: 5em;
      font-weight: bold;
      margin: 4px 2px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <script>
    function opendoor() {
      $.ajax({
        url:"opengarage.php", //the page containing php script
        type: "POST", //request type
      });
    }
    var interval = 1000;
    function checkDoorState() {
      $.ajax({
        type: "POST",
        url: "garagedoorstate.php",
        success: function (data) {
          $('#garagedoorstate').text(data);
        },
        complete: function (data) {
          setTimeout(checkDoorState, interval);
        }
      });
    }
    setTimeout(checkDoorState, interval);
  </script>
  <center>
    <br />
    <br />
    <h1>Garasjeportåpner</h1>
    <br />
    <button class="button" onclick="opendoor()">Klikk!</button>
    <br />
    <span>Status: </span><span id='garagedoorstate'>Ukjent</span>
  </center>
</body>
</html>
