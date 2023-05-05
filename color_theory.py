import argparse
import sys

class Theory:
    """Runs provided hexcode values through a series of appropriate theories to test compatability."""
    
    def __init__(self, hexcode):
        """Takes in a maximum number of three hexcode values and creates Color object."""
        self.hexcode = hexcode
        
        if hexcode is None:
            # throw insufficient parameters error
            pass
        else:
            self.hexcode = Color(hexcode)
            
    def monochromatic(rgb):
        """A color theory that accepts 2-3 color values to test compatability by hue and light."""
        pass
        
    def analogous(first_color, second_color, third_color):
        """A color theory that accepts 3 color values to test compatability by hue and chroma."""
        
        if Theory.duo_set == True:
            # throw insufficient parameters error
            pass
        else:
            
            if (Color.saturation(first_color) == Color.saturation(second_color) == Color.saturation(third_color)):
                
                if (Color.light(first_color) == Color.light(second_color) == Color.light(third_color)):
                    print("The given colors support the Analogous Color Theory.")
                    return True
                else:  
                    print("The given colors do not support the Analogous Color Theory.")
                    return False
            else:
                print("The given colors do not support the Analogous Color Theory.")
                return False
    
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
        # add docstrings
        
        self.rgb = Color.hex_to_rgb(hexcode)
            
        self.hsl = [Color.hue(self.rgb()), Color.chroma(self.rgb()), Color.light(self.rgb())]
       
    def hex_to_rgb(hexcode):
        """Converts the provided hexcode value into an RGB value."""
        
        rgb = []
        
        for sub_value in (0, 2, 4):
            value = hexcode[sub_value : sub_value + 2]
            
            rgb.append(value)
            
        return rgb
    
    def rgb_to_hex(rgb):
        """Converts the provided RGB tuple into a hexcode value."""
        pass
    
    def hsl_to_rgb(hsl):
        """Converts the HSL tuple into an RGB tuple."""
        pass
       
    def hue(rgb):
        """Identifies the base color of the RGB value."""
        nrgb = []
        
        for color in rgb:
            new_color = color / 255
            nrgb.append(new_color)
        
        max = max(nrgb)
        min = min(nrgb)
        
        if (max - min == 0):
            base = 0
        elif (max == nrgb[0]):
            base = 60 * (((nrgb[1]-nrgb[2]) / (max-min)) % 6)
        elif (max == nrgb[1]):
            base = 60 * (((nrgb[0]-nrgb[2]) / (max-min)) + 2)
        else:
            base = 60 * (((nrgb[0]-nrgb[1]) / (max-min)) + 4)
            
        if (base < 0):
            base += 360
            
        return base
    
    def chroma(rgb):
        """Identifies the saturation of the RGB value."""
        
        if (max - min == 0):
            saturation = 0
        else:
            saturation = (max - min) / (1 - abs(max + min - 1))
            
        return saturation
    
    def light(rgb):
        """Identifies the brightness of the RGB value."""
        
        return (max + min) / 2