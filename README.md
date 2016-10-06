## Autohat Rig

This board is designed to help automated testing of SBCs (single-board computers), by writing an image to the device and booting it up. It has a USB controlled relay which controls the power supply of the device and a USB controlled multiplexer that switches the SD card connectivity between the device under test and the tester machine.

The software that works together with the board can be found at the [Autohat repo](https://github.com/resin-io/autohat).

We based our design on [Samsung Test Lab’s sd-mux board](https://git.tizen.org/cgit/tools/testlab/sd-mux).
