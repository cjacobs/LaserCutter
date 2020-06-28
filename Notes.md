# Notes

## bCNC (Gcode sender)
https://github.com/vlachoudis/bCNC.git

## UGS (Universal Gcode Sender) for RPi
https://winder.github.io/ugs_website/


## Arduino-to-parallel shield
https://www.tindie.com/products/ron/arduino-grbl-to-db25-cnc-shield-kit/#product-reviews


## Arduino-to-parallel port (for using GRBL)
http://diy3dtech.com/how-to-wire-arduino-wgrbl-for-parallel-port-control/

## GRBL-to-parallel project
https://hackaday.io/project/166574-grbl-to-parallel-port


## GRBL pins
https://github.com/grbl/grbl/wiki/Connecting-Grbl
https://github.com/gnea/grbl/wiki/Connecting-Grbl



## From https://cnc4pc.com/db25-motion-controller-arduino-shield.html

### OVERVIEW

This is a motherboard for convert of ARDUINO to a connector DB25

### FEATURES

Plugs into into an Arduino UNO and provides a DB25 connector to emulate a parallel port.


DB25 side

| Arduino | Function          | DB25 pin |
|---------|-------------------|----------|
| 2       | STEP_X_AXIS       | 2        |
| 3       | STEP_Y_AXIS       | 4        |
| 4       | STEP_Z_AXIS       | 6        |
| 5       | DIRECTION_X_AXIS  | 3        |
| 6       | DIRECTION_Y_AXIS  | 5        |
| 7       | DIRECTION_Z_AXIS  | 7        |
| 9       | LIMIT_X_AXIS      | 11       |
| 10      | LIMIT_Y_AXIS      | 12       |
| 11      | LIMIT_Z_AXIS      | 13       |
| 12      | SPINDLE ENABLE    | 14       |
| 13      | SPINDLE DIRECTION | 16       |
| A3      | COOLANT ENABLE    | 1        |
| GND     | GND               |18-25     |

Sorted by DB25 pin:
| Arduino | Function          | DB25 pin |
|---------|-------------------|----------|
| A3      | COOLANT ENABLE    | 1        |
| 2       | STEP _X_AXIS      | 2        |
| 5       | DIRECTION_X_AXIS  | 3        |
| 3       | STEP_Y_AXIS       | 4        |
| 6       | DIRECTION_Y_AXIS  | 5        |
| 4       | STEP_Z_AXIS       | 6        |
| 7       | DIRECTION_Z_AXIS  | 7        |
| 9       | LIMIT_X_AXIS      | 11       |
| 10      | LIMIT_Y_AXIS      | 12       |
| 11      | LIMIT_Z_AXIS      | 13       |
| 12      | SPINDLE ENABLE    | 14       |
| 13      | SPINDLE DIRECTION | 16       |
| GND     | GND               |18-25     |




## LinuxCNC documentation on parallel port:
http://www.linuxcnc.org/docs/2.4/html/hal_parallel_port.html



## Pin functions derived from LaserOverdrive stepconf file:

### All 'inv' are False except when noted
| pin | function      |
|-----|---------------|
|   1 | unused-output |
|   2 | xstep         |
|   3 | xdir (INV)    |
|   4 | ystep         |
|   5 | ydir          |
|   6 | unused-output |
|   7 | unused-output |
|   8 | unused-output |
|   9 | unused-output |
|  10 | home-x        |
|  11 | home-y        |
|  12 | unused-input  |
|  13 | unused-input  |
|  14 | unused-output |
|  15 | unused-input  |
|  16 | spindle-on    |
|  17 | spindle-pwm   |
