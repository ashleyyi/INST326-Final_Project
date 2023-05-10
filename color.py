import argparse
import colorsys

class Color:
    """Uses the provided hexcode to identify properties of a color and store them in a Color class instance."""
    
    def __init__(self, hexcode):
        # add docstrings
        self.hexcode = hexcode
        self.rgb = self.hex_to_rgb(self.hexcode)
        
        r = self.rgb[0] / 255
        g = self.rgb[1] / 255
        b = self.rgb[2] / 255
            
        self.hls = colorsys.rgb_to_hls(r, g, b)
       
    def hex_to_rgb(self, hexcode):
        """Converts the provided hexcode value into an RGB value."""
        
        hex = hexcode.replace('#', '')
        rgb = []
        
        for value in (0, 2, 4):
            part = int(hex[value : value + 2], 16)
            rgb.append(part)
        
        return rgb
    
    def rgb_to_hex(rgb):
        """Converts the provided RGB tuple into a hexcode value."""
        
        hex_code = "#" 
        
        for value in rgb:
            
            hex_code += ('{:02X}'.format(value))
        
        return hex_code
    
    def hls_to_hex(hls):
        """Converts the provided HLS tuple into an RGB tuple."""
        
        sub_rgb = colorsys.hls_to_rgb(hls[0], hls[1], hls[2])
        rgb = int(sub_rgb[0] * 255), int(sub_rgb[1] * 255), int(sub_rgb[2] * 255)
        
        return Color.rgb_to_hex(rgb)
    
if __name__ == "__main__":
        
    test = Color('#1ECBE1')
    
    
    
    