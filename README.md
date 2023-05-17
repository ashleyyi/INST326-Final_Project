Documentation

The INST326 Final Project by Ashley Yi and Dhruvit Patel models after the color wheel and the color theory. There are seven sub theories in this software deliverable, in which each will take the hexcode provided by the user and return a set of hexcodes that fit the appropriate sub theory. The alternate hexcodes are created by taking the original hexcode and adjusting its hue, light, or saturation values. This project is dedicated towards artists who could utilize this software deliverable to create an appropriate palette of their choosing.

In the terminal, the user can call the appropriate programming language and the theory.py file to initiate the entire software deliverable, with a hex code of their choosing to determine what values will be returned. For example, “python3 theory.py #1ECBE1” will have the Theory class access the color.py file and create a Color object with the taken parameter “#1ECBE1.” The color.py file will translate the parameter and create three attributes into hex code, RGB, and HLS. The Theory object will then take the HLS attribute to create alternate colors in the same format according to the color theory, which at return will be translated back to HLS using a method from the Color class. The color_theory method will call on all seven color theories to print out a string into the terminal of what colors to use in which palette.

After running the program from the command line, the terminal will return a string that states what the provided hex code is, followed by a list of what other hex codes could be used along with the original. The combination of colors range from two to five hex codes per set, but because the user already knows their provided hex code, the original will be restated at the start and the methods will state either one to four hex codes that are compatible to it. For example, the monochromatic color theory has two colors: the original and an alternate color. The terminal in this case will only state “Monochromatic: “ followed by the alternate color. The same applies to all other color theories, each hex code being separated by a comma if there are more than one alternate colors. It is highly recommended to use all hex codes from a color theory, as they are made to complement each other as a set rather than as a pick-and-choose list of options.

Anas, B. (2020, August 7). Analogous colors (and how to use them in design). Inside Design Blog. https://www.invisionapp.com/inside-design/analogous-colors/ 
	Used to understand which value was supposed to be adjusted in a provided color’s HLS values to create alternate colors.
Color wheel: Use color theory and color calculator. Atmos. (n.d.). https://atmos.style/color-wheel 
	Used to understand how each color theory works through visual representation.
Braun, A. (2022, October 13). Color codes: What’s the difference between hex, RGB, and HSL? Make Tech Easier. https://www.maketecheasier.com/difference-between-hex-rgb-hsl/ 
	Used to determine whether to use HLS or HSV to create the alternate colors.
Color wheel - color theory and calculator | canva colors. Canva. (n.d.). https://www.canva.com/colors/color-wheel/ 
	Used to understand how each color theory works through visual representation.
Hex to RGB Color Converter. RapidTables. (n.d.). https://www.rapidtables.com/convert/color/hex-to-rgb.html 
	Used as a way to confirm that the software deliverable is properly translating hex codes into RGB
Interaction Design Foundation. (2023, March 23). What is color theory?. The Interaction Design Foundation. https://www.interaction-design.org/literature/topics/color-theory#:~:text=Color%20theory%20is%20the%20collection,%2C%20psychology%2C%20culture%20and%20more 
	Used to determine what color theories/methods will be made in the software deliverable.
Krzysztof. (2021, March 26). HSL color model: What it does, when it’s useful, and how it compares to RGB. Merixstudio. https://www.merixstudio.com/blog/hsl-color-model/ 
	Used to understand how HLS works separately from RGB while still displaying the same color.
RGB to HSL color conversion. RapidTables. (n.d.). https://www.rapidtables.com/convert/color/rgb-to-hsl.html 
	Used as a way to confirm that the software deliverable is properly translating RGB into HLS.
