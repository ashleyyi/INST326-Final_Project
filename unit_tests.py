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
        theory1_complementary = theory.Theory('#B94685').complementary() 
        
        self.assertTupleEqual(('#B94685', '#46B97A'), theory1_complementary)  
        
    def test_split_complementary(self): 
        theory1_split_complementary = theory.Theory('#B94685').split_complementary() 
        
        self.assertTupleEqual(('#B94685', '#4BB946', '#B9B746'), theory1_split_complementary) 
        
    def test_triad(self): 
        theory1_triad = theory.Theory('#B94685').triad() 
        
        self.assertTupleEqual(('#B94685', '#85B946', '#4685B9'), theory1_triad) 
        
    def test_tetradic(self): 
        theory1_tetradic = theory.Theory('#B94685').tetradic()
        
        self.assertTupleEqual(('#B94685', '#B346B9', '#B9464C', '#4CB946', '#46B9B3'), theory_tetradic)
        
    def test_square(self): 
        theory1_square = theory.Theory('#B94685').square()
       
        self.assertTupleEqual(('#B94685', '#B9B346', '#46B97A', '#464CB9'), theory1_square)
    
    
if __name__ == '__main__':
    unittest.main()
