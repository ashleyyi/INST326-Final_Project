import argparse
import sys

class Theory:
    """Runs provided hexcode values through a series of appropriate theories to test compatability."""
    count = 0
    duo_set = False
    
    def __init__(self, first_hex, second_hex, third_hex):
        """Takes in a maximum number of three hexcode values and creates Color object."""
        self.first_hex = first_hex
        self.second_hex = second_hex
        self.third_hex = third_hex
        
        if first_hex is None:
            # throw insufficient parameters error
            pass
        else:
            self.first_color = Color(hexcode)
        
        if second_hex is None:
            # throw insufficient parameters error
            pass
        else:
            self.second_color = Color(hexcode)
        
        if third_hex is None:
            duo_set = True
        else:
            self.third_color = Color(hexcode)
            
    def monochromatic(first_color, second_color, third_color):
        """A color theory that accepts 2-3 color values to test compatability by hue and light."""
        pass
        
    def analogous(first_color, second_color, third_color):
        """A color theory that accepts 3 color values to test compatability by hue and chroma."""
        pass
    
    def complementary(first_color, second_color, third_color):
        """A color theory that accepts 2 color values to test compatability by hue and saturation."""
        pass
    
    def split_complementary(first_color, second_color, third_color):
        """A color theory that accepts 3 color values to test compatability by hue and saturation."""
        pass
    
    def triad(first_color, second_color, third_color):
        """A color theory that accepts 3 color values to test compatability by hue and saturation."""
        pass
                                     
class Color:
    """Uses the provided hexcode to identify properties of a color and store them in a Color class instance."""
    
    def __init__(self, hexcode):
        """Converts the provided hexcode value into an RGB value."""
        
        self.rgb = []
        for sub_value in (0, 2, 4):
            value = hexcode[sub_value : sub_value + 2]
            
            self.rgb.append(value)
            
    def hue(rgb):
        """Identifies the base color of the RGB value."""
        pass
    
    def chroma(rgb):
        """Identifies the saturation of the RGB value."""
        pass
    
    def light(rgb):
        """Identifies the brightness of the RGB value."""
        pass