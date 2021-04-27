#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file presents an interface for interacting with the Playstation 4 Controller
# in Python. Simply plug your PS4 controller into your computer using USB and run this
# script!
#
# NOTE: I assume in this script that the only joystick plugged in is the PS4 controller.
#       if this is not the case, you will need to change the class accordingly.
#
# Copyright © 2015 Clay L. McLeod <clay.l.mcleod@gmail.com>
#
# Distributed under terms of the MIT license.

import os
import pprint
import pygame

class PS4Controller(object):
    """Class representing the PS4 controller. Pretty straightforward functionality."""

    controller = None
    axis_data = None
    button_data = None
    hat_data = None

    def init(self):
        """Initialize the joystick components"""

        pygame.init()
        pygame.joystick.init()
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

    def listen(self):
        """Listen for events to happen"""

        if not self.axis_data:
            self.axis_data = {}

        if not self.button_data:
            self.button_data = {}
            for i in range(self.controller.get_numbuttons()):
                self.button_data[i] = False

        if not self.hat_data:
            self.hat_data = {}
            for i in range(self.controller.get_numhats()):
                self.hat_data[i] = (0, 0)

        while True:
                  while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    if event.axis == 0:
                        if event.value > 0:
                            print "right"
							# os.system("echo -n -e '\xFE\x6C\x01' > NAME_OF_YOUR_CHIP")
                        if event.value < 0:
                            print "left"
                            #os.system("echo -n -e '\xFE\x6C\x01' > NAME_OF_YOUR_CHIP")
                    if event.axis == 1:
                        if event.value > 0:
                            print "down"
                            #os.system("echo -n -e '\xFE\x6C\x01' > NAME_OF_YOUR_CHIP")
                        if event.value < 0:
                            print "up"
                            #os.system("echo -n -e '\xFE\x6C\x01' > NAME_OF_YOUR_CHIP")
                elif event.type == pygame.JOYBUTTONDOWN:
                    if event.button == 1:
                        print "wow pressed the X button"
                        #os.system("echo -n -e '\xFE\x6C\x01' > NAME_OF_YOUR_CHIP")
                    if event.button == 2:
                        print "I think this is O"
                        #os.system("echo -n -e '\xFE\x6C\x01' > NAME_OF_YOUR_CHIP")
                    if event.button == 3:
                        print "I think this is triangle"
                        #os.system("echo -n -e '\xFE\x6C\x01' > NAME_OF_YOUR_CHIP")
                    if event.button == 4;
                        print "Maybe square"
                        #os.system("echo -n -e '\xFE\x6C\x01' > NAME_OF_YOUR_CHIP")
                elif event.type == pygame.JOYBUTTONUP:
                    if event.button == 1:
                        print "he-yump"
                elif event.type == pygame.JOYHATMOTION:
                    if event.hat == 0:
                        if event.value == (1, 0):
                            print "right"
                        if event.value == (-1, 0):
                            print "left"
                        if event.value == (0, 1):
                            print "up"
                        if event.value == (0, -1):
                            print "down"

                os.system('clear')
                pprint.pprint(self.button_data)
                pprint.pprint(self.axis_data)
                pprint.pprint(self.hat_data)


if __name__ == "__main__":
    ps4 = PS4Controller()
    ps4.init()
    ps4.listen()
