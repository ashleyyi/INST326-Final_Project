import color
import theory
import unittest

class TestColorTheory(unittest.TestCase):
    
    # Testing color class
    
    def test_hue1(self):
        color1 = color.Color('#31E21D')
        
        self.assertAlmostEqual(0.316, color1.hls[0], 3)
        
    def test_light1(self):
        color1 = color.Color('#31E21D')
        
        self.assertAlmostEqual(0.5, color1.hls[1], 3)
        
    def test_saturation1(self):
        color1 = color.Color('#31E21D')
        
        self.assertAlmostEqual(0.773, color1.hls[2], 3) 
        
    def test_hue2(self): 
        color2 = color.Color('#1974E6') 
        
        self.assertAlmostEqual(0.591, color2.hls[0], 3) 
        
    def test_light2(self): 
        color2 = color.Color('#1974E6')  
        
        self.assertAlmostEqual(0.804, color.hls[1], 3) 
        
    def test_saturation2(self): 
        color2 = color.Color('#1974E6') 
        
        self.assertAlmostEqual(0.5, color.hls[2], 3) 
              
        
    # Testing theory class
    
    def test_monochromatic1(self):
        theory1_monochromatic = theory.Theory('#B94685').monochromatic()
        
        self.assertTupleEqual(('#B94685', '#C66B9D'), theory1_monochromatic)
        
    def test_analogous1(self):
        theory1_analogous = theory.Theory('#B94685').analogous()
        
        self.assertTupleEqual(('#B94685', '#B9464B', '#B346B9'), theory1_analogous) 
        
    def test_complementary1(self): 
        
        self.assertTupleEqual(('#B94685', '#46B97A'), theory1_complementary) 
    
if __name__ == '__main__':
    unittest.main()
