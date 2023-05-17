Documentation

The INST326 Final Project by Ashley Yi and Dhruvit Patel models after the color wheel and the color theory. There are seven sub theories in this software deliverable, in which each will take the hexcode provided by the user and return a set of hexcodes that fit the appropriate sub theory. The alternate hexcodes are created by taking the original hexcode and adjusting its hue, light, or saturation values. This project is dedicated towards artists who could utilize this software deliverable to create an appropriate palette of their choosing.

In the terminal, the user can call the appropriate programming language and the theory.py file to initiate the entire software deliverable, with a hex code of their choosing to determine what values will be returned. For example, “python3 theory.py #1ECBE1” will have the Theory class access the color.py file and create a Color object with the taken parameter “#1ECBE1.” The color.py file will translate the parameter and create three attributes into hex code, RGB, and HLS. The Theory object will then take the HLS attribute to create alternate colors in the same format according to the color theory, which at return will be translated back to HLS using a method from the Color class. The color_theory method will call on all seven color theories to print out a string into the terminal of what colors to use in which palette.

