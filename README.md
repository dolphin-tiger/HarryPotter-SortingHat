# HarryPotter-SortingHat
**Sorting Hat** - Raspian/Python/Neopixel controller to sort a participant into a house.

This is a project with my kids (age 6 and 9) to learn about Python, Raspberry Pi, and the GPIO interface.  It uses a physical button connected to a GPIO pin to start the Sorting, then uses an [Adafruit Neopixel Ring 12 x 5050](https://www.adafruit.com/product/1643) LED ring to sort and display the results.

This is a very simple codeset and a work in progress as we learn to code in Python.

It's currently just run from a shell by running the command "sudo python3 sortingHat.py".  Because of the interface for the Neopixel it must be run in sudo mode to allow for direct memory access.

Here is a link to more about Neopixel on Raspbery Pi: [Link](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview)

We used this method of wiring with a separate 5Vdc power supply:

![Raspberry Pi Neopixel wiring with diode](https://cdn-learn.adafruit.com/assets/assets/000/064/122/medium640/led_strips_raspi_NeoPixel_Diode_bb.jpg?1540315941)
