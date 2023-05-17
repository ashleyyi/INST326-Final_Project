import argparse
import colorsys
import color
import sys

class Theory:
    """Runs provided hexcode values through a series of appropriate theories to test compatability.
    
    Attributes: hexcode, a String that defines the hex code color provided by the user from command line
                color_obj, a Color object created with the given hex code parameter"""
    
    def __init__(self, hexcode):
        """Takes a hexcode value and creates Color object.
        
        Args: hexcode, a String that defines the hex code color provided by the user from command line
              
        Side effects: instantiates the hexcode String and color_obj object of the Theory class"""
        
        self.hexcode = hexcode
        self.color_obj = color.Color(self.hexcode)
            
    def monochromatic(self):
        """Creates an alternate color based off of the hexcode attribute by adjusting the light value, 
           following the monochromatic color theory.
        
        Returns: hex code String of given hexcode
                 hex code String of new_hls alternate color"""
        
        # If light value is greater than or equal to 60%
        if self.color_obj.hls[1] >= 0.6:
            new_hls = self.color_obj.hls[0], self.color_obj.hls[1] - 0.1, self.color_obj.hls[2]
            
            return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(new_hls)
        
        # If light value is less than 60%
        else:
            new_hls = self.color_obj.hls[0], self.color_obj.hls[1] + 0.1, self.color_obj.hls[2]
            
            return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(new_hls)
        
    def analogous(self):
        """Creates two alternate colors based off of the hexcode attribute by adjusting the hue value, 
           following the analogous color theory.
        
        Returns: hex code String of given hexcode
                 hex code String of left_color alternate color
                 hex code String of right_color alternate color"""
        
        # Creating left color
        left_color = self.color_obj.hls[0] + 0.083, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if left_color[0] > 1:
            left_color = 1 - left_color[0], left_color[1], left_color[2]
        
        # Creating right color
        right_color = self.color_obj.hls[0] - 0.083, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if right_color[0] < 0:
            right_color = 1 + right_color[0], right_color[1], right_color[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(left_color), color.Color.hls_to_hex(right_color)
    
    def complementary(self):
        """Creates an alternate color based off of the hexcode attribute by adjusting the hue value, 
           following the complementary color theory.
        
        Returns: hex code String of given hexcode
                 hex code String of second_color alternate color"""
        
        second_color = self.color_obj.hls[0] - 0.5, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if second_color[0] < 0:
            second_color = 1 - second_color[0], second_color[1], second_color[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(second_color)
    
    def split_complementary(self):
        """Creates two alternate colors based off of the hexcode attribute by adjusting the hue value, 
           following the split complementary color theory.
        
        Returns: hex code String of given hexcode
                 hex code String of left_com alternate color
                 hex code String of right_com alternate color"""
        
        # Create center point for opposing analogous colors
        com = self.color_obj.hls[0] - 0.5, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if com[0] < 0:
            com = 1 - com[0], com[1], com[2]
        
        # Creating left color
        left_com = com[0] - 0.083, com[1], com[2]
        
        if left_com[0] < 0:
            left_com = 1 + left_com[0], left_com[1], left_com[2]
            
        # Creating right color
        right_com = com[0] + 0.083, com[1], com[2]
        
        if right_com[0] > 1: 
            right_com = 1 - right_com[0], right_com[1], right_com[2]
        
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(left_com), color.Color.hls_to_hex(right_com)
    
    def triad(self):
        """Creates two alternate colors based off of the hexcode attribute by adjusting the hue value, 
           following the triadic color theory.
        
        Returns: hex code String of given hexcode
                 hex code String of left_color alternate color
                 hex code String of right_color alternate color"""
        
        # Creating left color
        left_color = self.color_obj.hls[0] + 0.33, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if left_color[0] > 1:
            left_color = 1 - left_color[0], left_color[1], left_color[2]
          
        # Creating right color  
        right_color = self.color_obj.hls[0] - 0.33, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if right_color[0] < 0:
            right_color = 1 + right_color[0], right_color[1], right_color[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(left_color), color.Color.hls_to_hex(right_color)
            
    def tetradic(self):
        """Creates four alternate colors based off of the hexcode attribute by adjusting the hue value, 
           following the tetradic color theory.
        
        Returns: hex code String of given hexcode
                 hex code String of left alternate color
                 hex code String of left_com alternate color
                 hex code String of right alternate color
                 hex code String of right_com alternate color"""
        
        # Creating left color
        left = self.color_obj.hls[0] - 0.083, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if left[0] < 0:
            left = 1 + left[0], left[1], left[2]
        
        # Creating left complementary color   
        left_com = left[0] - 0.5, left[1], left[2]
        
        if left_com[0] < 0:
            left_com = 1 + left_com[0], left_com[1], left_com[2]
         
        # Creating right color   
        right = self.color_obj.hls[0] + 0.083, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if right[0] > 1:
            right = 1 - right[0], right[1], right[2]
        
        # Creating right complementary color
        right_com = right[0] - 0.5, right[1], right[2]
        
        if right_com[0] < 0:
            right_com = 1 + right_com[0], right_com[1], right_com[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(left), color.Color.hls_to_hex(left_com), color.Color.hls_to_hex(right), color.Color.hls_to_hex(right_com)
    
    def square(self):
        """Creates three alternate colors based off of the hexcode attribute by adjusting the hue value, 
           following the square color theory.
        
        Returns: hex code String of given hexcode
                 hex code String of dom_com alternate color
                 hex code String of secondary alternate color
                 hex code String of sec_com alternate color"""
        
        # Creating complementary color of given hexcode
        dom_com = self.color_obj.hls[0] - 0.5, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if dom_com[0] < 0:
            dom_com = 1 + dom_com[0], dom_com[1], dom_com[2]
        
        # Creating secondary color
        secondary = self.color_obj.hls[0] - 0.25, self.color_obj.hls[1], self.color_obj.hls[2]
        
        if secondary[0] < 0:
            secondary = 1 + secondary[0], secondary[1], secondary[2]
         
        # Creating complementary color of secondary   
        sec_com = secondary[0] - 0.5, secondary[1], secondary[2]
        
        if sec_com[0] < 0:
            sec_com = 1 + sec_com[0], sec_com[1], sec_com[2]
            
        return color.Color.hls_to_hex(self.color_obj.hls), color.Color.hls_to_hex(secondary), color.Color.hls_to_hex(dom_com), color.Color.hls_to_hex(sec_com)
    
    def color_theory(self):
        """Calls all color theory methods to organize into a String and print.
        
        Side effects: prints String of all Theory class methods into Terminal"""
        
        sub_theories = "Your color is " + self.hexcode + ", here are the alternate colors that you can use with this:"
        sub_theories += "\nMonochromatic: " + self.monochromatic()[1]
        sub_theories += "\nAnalogous: " + self.analogous()[1] + ", " + self.analogous()[2]
        sub_theories += "\nComplementary: " + self.complementary()[1]
        sub_theories += "\nSplit Complementary: " + self.split_complementary()[1] + ", " + self.split_complementary()[2]
        sub_theories += "\nTriad: " + self.triad()[1] + ", " + self.triad()[2]
        sub_theories += "\nTetradic: " + self.tetradic()[1] + ", " + self.tetradic()[2] + ", " + self.tetradic()[3]
        sub_theories += "\nSquare: " + self.square()[1] + ", " + self.square()[2] + ", " + self.square()[3]
        
        print(sub_theories)
    
if __name__ == "__main__":
    """Takes first argument from command line and calls the color_theory method of the Theory class."""
        
    Theory(sys.argv[1]).color_theory()