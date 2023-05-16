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
        
        second_color = self.color_obj.hls[0] - 0.5, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if second_color[0] < 0:
            second_color = 1 - second_color[0], second_color[1], second_color[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(second_color)
    
    def split_complementary(self):
        """A color theory that accepts 3 color values to test compatability by hue and saturation."""
        
        com = self.color_obj.hls[0] - 0.5, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if com[0] < 0:
            com = 1 - com[0], com[1], com[2]
            
        left_com = com[0] - 0.083, com[1], com[2]
        
        if left_com[0] < 0:
            left_com = 1 + left_com[0], left_com[1], left_com[2]
            
        right_com = com[0] + 0.083, com[1], com[2]
        
        if right_com[0] > 1: 
            right_com = 1 - right_com[0], right_com[1], right_com[2]
        
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(left_com), color.Color.hls_to_hex(right_com)
    
    def triad(self):
        """A color theory that accepts 3 color values to test compatability by hue and saturation."""
        
        left_color = self.color_obj.hls[0] + 0.33, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if left_color[0] > 1:
            left_color = 1 - left_color[0], left_color[1], left_color[2]
            
        right_color = self.color_obj.hls[0] - 0.33, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if right_color[0] < 0:
            right_color = 1 + right_color[0], right_color[1], right_color[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(left_color), color.Color.hls_to_hex(right_color)
            
    def tetradic(self):
        # add docstrings
        
        dom_com = self.color_obj.hls[0] - 0.5, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if dom_com[0] < 0:
            dom_com = 1 + dom_com[0], dom_com[1], dom_com[2]
        
        secondary = self.color_obj.hls[0] - 0.166, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if secondary[0] < 0:
            secondary = 1 + secondary[0], secondary[1], secondary[2]
            
        sec_com = secondary[0] - 0.5, secondary[1], secondary[2]
        
        if sec_com[0] < 0:
            sec_com = 1 + sec_com[0], sec_com[1], sec_com[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(secondary), color.Color.hls_to_hex(dom_com), color.Color.hls_to_hex(sec_com)
    
    def square(self):
        # add docstrings
        
        dom_com = self.color_obj.hls[0] - 0.5, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if dom_com[0] < 0:
            dom_com = 1 + dom_com[0], dom_com[1], dom_com[2]
        
        secondary = self.color_obj.hls[0] - 0.25, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if secondary[0] < 0:
            secondary = 1 + secondary[0], secondary[1], secondary[2]
            
        sec_com = secondary[0] - 0.5, secondary[1], secondary[2]
        
        if sec_com[0] < 0:
            sec_com = 1 + sec_com[0], sec_com[1], sec_com[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(secondary), color.Color.hls_to_hex(dom_com), color.Color.hls_to_hex(sec_com)
    
if __name__ == "__main__":
        
    test = Theory('#1ECBE1')
    
    print(test.square())