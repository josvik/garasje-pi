<?php
// Remember to setup gpio 18 with:
// echo "18" > /sys/class/gpio/export
// echo "out" > /sys/class/gpio/gpio18/direction
//
// Run these lines at boot, for example in /etc/rc.local

exec('echo "1" > /sys/class/gpio/gpio18/value');
sleep(1);
exec('echo "0" > /sys/class/gpio/gpio18/value');
?>
