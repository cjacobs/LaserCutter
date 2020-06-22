# Notes


## Arduino-to-parallel port (for using GRBL)
http://diy3dtech.com/how-to-wire-arduino-wgrbl-for-parallel-port-control/


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


