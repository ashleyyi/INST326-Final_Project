import argparse
import colorsys

class Color:
    """Uses the provided hexcode to identify properties of a color and store them in a Color class instance.
    
    Attributes: hexcode, a String that defines the hex code color provided by the Theory class
                rgb, a list with r, g, and b values of the hexcode attribute
                hls, a Tuple with hue, light, and saturation values of the rgb attribute"""
    
    def __init__(self, hexcode):
        """Takes in the hexcode argument and translates the parameter into rgb and hls attributes.
        
        Args: hexcode, a String that defines the hex code color attribute given by the parameter
        
        Side effects: instantiates the hexcode String, rgb list, and hls Tuple attributes of the Color class"""
        
        self.hexcode = hexcode
        self.rgb = self.hex_to_rgb(self.hexcode)
        self.hls = colorsys.rgb_to_hls(self.rgb[0] / 255, self.rgb[1] / 255, self.rgb[2] / 255)
       
    def hex_to_rgb(self, hexcode):
        """Converts the provided hexcode value into an RGB value.
        
        Args: hexcode, a String that defines the hex code color that will be translated
        
        Returns: rgb, a translated list that carries the r, g, and b values of the given hexcode"""
        
        hex = hexcode.replace('#', '')
        rgb = []
        
        # Iterates through each two characters of hexcode into decimal values
        for value in (0, 2, 4):
            part = int(hex[value : value + 2], 16)
            rgb.append(part)
        
        return rgb
    
    def rgb_to_hex(rgb):
        """Converts the provided rgb list into a hexcode value.
        
        Args: rgb, a list with r, g, and b values of the given hexcode
        
        Returns: hex_code, a translated String that defines the rgb list in hex code format"""
        
        hex_code = "#" 
        
        # Iterates through each rgb value to convert to String and base 16 system
        for value in rgb:
            hex_code += ('{:02X}'.format(value))
        
        return hex_code
    
    def hls_to_hex(hls):
        """Converts the provided hls tuple into an rgb tuple.
        
        Args: hls, a tuple with hue, light, and saturation values of the given hexcode
        
        Returns: a hex code translation of rgb tuple translated from hls"""
        
        sub_rgb = colorsys.hls_to_rgb(hls[0], hls[1], hls[2])
        rgb = int(sub_rgb[0] * 255), int(sub_rgb[1] * 255), int(sub_rgb[2] * 255)
        
        return Color.rgb_to_hex(rgb)
    
if __name__ == "__main__":
    """Tests the Color class by creating a Color object with #1ECBE1 hex code.
    
    Side effects: prints rgb list and hls tuple of test Color object"""
    
    test = Color('#1ECBE1')
    
    print(test.rgb)
    print(test.hls)