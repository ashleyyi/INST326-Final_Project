import argparse
import colorsys
import color

class Theory:
    """Runs provided hexcode values through a series of appropriate theories to test compatability."""
    
    def __init__(self, hexcode):
        """Takes in a maximum number of three hexcode values and creates Color object."""
        
        self.hexcode = hexcode
        self.color_obj = color.Color(self.hexcode)
            
    def monochromatic(self):
        """A color theory that accepts 2-3 color values to test compatability by hue and light."""
        
        if self.color_obj.hls[1] >= 0.6:
            new_hls = self.color_obj.hls[0], self.color_obj.hls[1] - 0.1, self.color_obj.hls[2]
            
            return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(new_hls)
        else:
            new_hls = self.color_obj.hls[0], self.color_obj.hls[1] + 0.1, self.color_obj.hls[2]
            
            return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(new_hls)
        
    def analogous(self):
        """A color theory that accepts 3 color values to test compatability by hue and chroma."""
        
        left_color = self.color_obj.hls[0] + 0.083, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if left_color[0] > 1:
            left_color = 1 - left_color[0], left_color[1], left_color[2]
            
        right_color = self.color_obj.hls[0] - 0.083, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if right_color[0] < 0:
            right_color = 1 + right_color[0], right_color[1], right_color[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(left_color), color.Color.hls_to_hex(right_color)
    
    def complementary(self):
        """A color theory that accepts 2 color values to test compatability by hue and saturation."""
        
        second_color = Color.hue(rgb) - 180, Color.chroma(rgb), Color.light(rgb)
        
        if second_color[0] < 0:
            second_color = 360 - second_color[0], second_color[1], second_color[2]
            
        return rgb, second_color
    
    def split_complementary(self, rgb):
        """A color theory that accepts 3 color values to test compatability by hue and saturation."""
        
        split = Theory.analogous(Theory.complementary(rgb)[1])
        
        return rgb, split[1], split[2]
    
    def triad(self, rgb):
        """A color theory that accepts 3 color values to test compatability by hue and saturation."""
        
        left_color = Color.hue(rgb) + 120, Color.chroma(rgb), Color.light(rgb)
        
        if left_color[0] > 360:
            left_color = 360 - left_color[0], left_color[1], left_color[2]
            
        right_color = Color.hue(rgb) - 120, Color.chroma(rgb), Color.light(rgb)
        
        if right_color < 0:
            right_color = 360 + right_color[0], right_color[1], right_color[2]
            
    def tetradic(self, rgb):
        pass
    
    def square(self, rgb):
        pass
    
if __name__ == "__main__":
        
    test = Theory('#1ECBE1')
    
    print(test.analogous())