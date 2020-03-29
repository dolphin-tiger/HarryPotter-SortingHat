# HarryPotter-SortingHat
Sorting Hat - Raspian/Python/Neopixel controller to sort participant into a house.

This is a project done with the kids to learn about Python, Raspberry Pi, and the GPIO interface.  It uses a physical button connected to a GPIO pin to start the Sorting, then uses an Adafruit Neopixel 12 5050 LED ring to sort and display the results.

This is a very simple codeset and a work in progress as we learn to code in Python.

It's currently just run from a shell by running the command "sudo python3 sortingHat.py".  Because of the interface for the Neopixel it must be run in sudo mode to allow for direct memory access.