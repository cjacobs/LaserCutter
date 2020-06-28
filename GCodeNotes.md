(Fast move to center)
G00 X0 Y0

(Move up and to the left by 1 unit)
G00 X1 Y1

(Move at a given feed rate)
G01 X2 Y2 F100 ; pretty slow
G01 X0 Y0 F50 ; even slower
G01 X-20 Y-20 F500 ; faster

G1 X1 Y1 F500 S10
G0


