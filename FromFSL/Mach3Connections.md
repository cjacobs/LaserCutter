From archived page at http://web.archive.org/web/20150219153434/http://www.fullspectrumengineering.com/laser%20connection.html

(See newparallelport.jpg for pinouts)

LimitX/LimitX are inputs. High = switch active, Low = switch non-active (normal)

Step_x/Step_y are the step inputs. Min 4.5us pulse width. Your system MUST be geared to 1000 steps per inch of travel. Remember that RetinaEngrave only outputs 2mA at 3.3v on its outputs. You MUST use a 5v buffer or breakout board with buffers to use most standalone stepper drivers because they have optical isolators that require 25mA at 5v.

Dir_x/Dir_y are the direction inputs. Direction is changable in the config.xml file.

RELAY: PWM laser power control. If high, laser is on. If low, laser is off. Setup as PWM spindle in Mach3. S1000 for 1000% power. Set S10 for 1% power.

Enable: if low then stepper motors enabled. If high, stepper motors disabled. Default is high

GND: Reference ground

Warning: It is not recommended to run the laser with the PC parallel port interface alone unless you are an advanced user. The laser will operate normally when under Mach3 control but the PC Parallel port boots up in an unknown state. The laser MUST be off before starting Mach3 or the laser input could be triggered by the PC.

We strongly recommended using Full Spectrum Laser USB RetinaEngrave board whenever possible.

These connections ensure the laser will not turn on unexpectedly when booting the computer.
