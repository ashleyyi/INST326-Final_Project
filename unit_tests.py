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
        
    # Testing theory class
    
    def test_monochromatic1(self):
        theory1_monochromatic = theory.Theory('#B94685').monochromatic()
        
        self.assertTupleEqual(('#B94685', '#C66B9D'), theory1_monochromatic)
        
    def test_analogous1(self):
        theory1_analogous = theory.Theory('#B94685').analogous()
        
        self.assertTupleEqual(('#B94685', '#B9464B', '#B346B9'), theory1_analogous)
    
if __name__ == '__main__':
    unittest.main()
