Laser cutter GRBL variables:
```
$3=1 (invert x direction)
$30=1000 (max spindle speed)
$31=0 (min spindle speed)
$32=1 (laser mode)
$100=39.37 (x steps/mm)
$101=39.37 (y steps/mm)
$110=500 (max x rate mm/min)
$111=500 (max y rate mm/min)
$130=200 (max x travel, mm)
$131=200 (max y travel, mm)
```

Full GRBL variable list:

| Settings and defauts | Description           |
|----------------------|-----------------------|
| $0=10        | Step pulse, microseconds      |
| $1=25        | Step idle delay, milliseconds |
| $2=0         | Step port invert, mask        |
| $3=0         | Direction port invert, mask   |
| $4=0         | Step enable invert, boolean   |
| $5=0         | Limit pins invert, boolean    |
| $6=0         | Probe pin invert, boolean     |
| $10=1        | Status report, mask           |
| $11=0.010    | Junction deviation, mm        |
| $12=0.002    | Arc tolerance, mm             |
| $13=0        | Report inches, boolean        |
| $20=0        | Soft limits, boolean          |
| $21=0        | Hard limits, boolean          |
| $22=1        | Homing cycle, boolean         |
| $23=0        | Homing dir invert, mask       |
| $24=25.000   | Homing feed, mm/min           |
| $25=500.000  | Homing seek, mm/min           |
| $26=250      | Homing debounce, milliseconds |
| $27=1.000    | Homing pull-off, mm           |
| $30=1000.    | Max spindle speed, RPM        |
| $31=0.       | Min spindle speed, RPM        |
| $32=0        | Laser mode, boolean           |
| $100=250.000 | X steps/mm                    |
| $101=250.000 | Y steps/mm                    |
| $102=250.000 | Z steps/mm                    |
| $110=500.000 | X Max rate, mm/min            |
| $111=500.000 | Y Max rate, mm/min            |
| $112=500.000 | Z Max rate, mm/min            |
| $120=10.000  | X Acceleration, mm/sec^2      |
| $121=10.000  | Y Acceleration, mm/sec^2      |
| $122=10.000  | Z Acceleration, mm/sec^2      |
| $130=200.000 | X Max travel, mm              |
| $131=200.000 | Y Max travel, mm              |
| $132=200.000 | Z Max travel, mm              |


## Possibly-relevant settings from LaserOverdrive EMC2 .ini file:

EMC2 ini file documentation: http://linuxcnc.org/docs/2.6/html/config/ini_config.html

```
[EMC]
MACHINE = FullSpectrumLaserCutter
DEBUG = 0

[DISPLAY]
DISPLAY = axis
EDITOR = gedit
POSITION_OFFSET = RELATIVE
POSITION_FEEDBACK = ACTUAL
MAX_FEED_OVERRIDE = 1.2
INCREMENTS = 10mm 5mm 1mm .5mm .1mm .05mm .01mm .005mm

[TASK]
TASK = milltask
CYCLE_TIME = 0.010

[RS274NGC]
PARAMETER_FILE = emc.var

[EMCMOT]
EMCMOT = motmod
COMM_TIMEOUT = 1.0
COMM_WAIT = 0.010
BASE_PERIOD = 100000
SERVO_PERIOD = 1000000

[HAL]
HALFILE = FullSpectrumLaserCutter.hal

[TRAJ]
AXES = 3
COORDINATES = X Y Z
LINEAR_UNITS = mm
ANGULAR_UNITS = degree
CYCLE_TIME = 0.010
DEFAULT_VELOCITY = 22.50
MAX_LINEAR_VELOCITY = 225.00

[EMCIO]
EMCIO = io
CYCLE_TIME = 0.100
TOOL_TABLE = tool.tbl

[AXIS_0]
TYPE = LINEAR
HOME = 0.0
MAX_VELOCITY = 225.0
MAX_ACCELERATION = 20000.0
STEPGEN_MAXACCEL = 25000.0
SCALE = 40
FERROR = 1
MIN_FERROR = .25
MIN_LIMIT = -0.001
MAX_LIMIT = 75.0
HOME_OFFSET = 0.000000
HOME_SEARCH_VEL = 0.100000
HOME_LATCH_VEL = -0.050000

[AXIS_1]
TYPE = LINEAR
HOME = 0.0
MAX_VELOCITY = 225.0
MAX_ACCELERATION = 10000.0
STEPGEN_MAXACCEL = 12500.0
SCALE = 40
FERROR = 1
MIN_FERROR = .25
MIN_LIMIT = -0.001
MAX_LIMIT = 140.0
HOME_OFFSET = 0.000000
HOME_SEARCH_VEL = 0.100000
HOME_LATCH_VEL = -0.050000

[AXIS_2]
TYPE = LINEAR
HOME = 0.0
MAX_VELOCITY = 1.0
MAX_ACCELERATION = 30.0
STEPGEN_MAXACCEL = 37.5
SCALE = 20.0
FERROR = 1
MIN_FERROR = .25
MIN_LIMIT = -0.001
MAX_LIMIT = 0.001
HOME_OFFSET = 0.0
HOME_SEARCH_VEL = 0.0
```


## Gcode header settings:

Relevant Gcode commands:

`S`: Sets the spindle speed
`M3`: Sets spindle pin to PWM rate as specified by the `S` command, sets direction pin high.
`M4`: Sets spindle pin to PWM rate as specified by the `S` command, sets direction pin low.
`M5`: Sets spindle pin to Low. Doesn't change direction pin.
`M7`/`M8`: Sets coolant pin high.
`M9`: Sets cooland pin low.

```
G21 (All units in mm)
G0 (stop)
S0 (turn off laser)

```
