<?php
  $bottomstatus = exec("cat /sys/class/gpio/gpio14/value");
  if ($bottomstatus == "0") {
    echo "Closed";
  } else { 
    $topstatus = exec("cat /sys/class/gpio/gpio15/value");
    if ($topstatus == "0") {
      echo "Open";
    } else {
      echo "Between";
    }
  }
?>
