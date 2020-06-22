#!/bin/bash

FILE=$1
OUTPUT="/home/matti/SAMPLE01.gcode"
HEADER='; filename = composition.3w
; machine = daVinciF10
; material = abs
; layer_height = 0.3
; total_layers = 173
; total_filament = 0.00
; extruder = 1
G21 ; set units to millimeters
M107
M190 S85 ; wait for bed temperature to be reached
M104 S225 ; set temperature
M109 S225 ; wait for temperature to be reached
G90 ; use absolute coordinates
G92 E0
M82 ; use absolute distances for extrusion
G1 F1800.000 E-1.00000
G92 E0
G1 Z0.600 F3600.000'

echo "$HEADER" > "$OUTPUT"
sed -e '1,/G1 Z0.600 F3600.000/ d' "$FILE" >> "$OUTPUT"

exit 0
