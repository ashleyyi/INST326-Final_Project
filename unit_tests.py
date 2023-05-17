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
        
        self.assertAlmostEqual(0.593, color2.hls[0], 3) 
        
    def test_light2(self): 
        color2 = color.Color('#1974E6')  
        
        self.assertAlmostEqual(0.5, color2.hls[1], 3) 
        
    def test_saturation2(self): 
        color2 = color.Color('#1974E6') 
        
        self.assertAlmostEqual(0.804, color2.hls[2], 3) 
              
    def test_hue3(self): 
        color3 = color.Color('#B59D4A') 
        
        self.assertAlmostEqual(0.129, color3.hls[0], 3) 
        
    def test_light3(self): 
        color3 = color.Color('#B59D4A') 
        
        self.assertAlmostEqual(0.5, color3.hls[1], 3) 
        
    def test_saturation3(self): 
        color3 = color.Color('#B59D4A') 
        
        self.assertAlmostEqual(0.42, color3.hls[2], 3) 
        
    # Testing theory class
    
    def test_monochromatic1(self):
        theory1_monochromatic = theory.Theory('#B94685').monochromatic()
        
        self.assertTupleEqual(('#B94685', '#C66B9D'), theory1_monochromatic)
        
    def test_monochromatic2(self):
        theory2_monochromatic = theory.Theory('#1974E6').monochromatic()
        
        self.assertTupleEqual(('#1873E6', '#478FEA'), theory2_monochromatic)
        
    def test_analogous1(self):
        theory1_analogous = theory.Theory('#B94685').analogous()
        
        self.assertTupleEqual(('#B94685', '#B9464B', '#B346B9'), theory1_analogous) 
        
    def test_analogous2(self):
        theory2_analogous = theory.Theory('#1974E6').analogous()
        
        self.assertTupleEqual(('#1873E6', '#2418E6', '#18DAE6'), theory2_analogous)
        
    def test_complementary1(self): 
        theory1_complementary = theory.Theory('#B94685').complementary() 
        
        self.assertTupleEqual(('#B94685', '#46B979'), theory1_complementary)  
        
    def test_complementary2(self):
        theory2_complementary = theory.Theory('#1974E6').complementary()
        
        self.assertTupleEqual(('#1873E6', '#E68B18'), theory2_complementary)
        
    def test_split_complementary1(self): 
        theory1_split_complementary = theory.Theory('#B94685').split_complementary() 
        
        self.assertTupleEqual(('#B94685', '#4BB946', '#46B9B3'), theory1_split_complementary) 
        
    def test_split_complementary2(self):
        theory2_split_complementary = theory.Theory('#1974E6').split_complementary()
        
        self.assertTupleEqual(('#1873E6', '#E62418', '#DAE618'), theory2_split_complementary) 
        
    def test_triad1(self): 
        theory1_triad = theory.Theory('#B94685').triad() 
        
        self.assertTupleEqual(('#B94685', '#8746B9', '#4682B9'), theory1_triad) 
        
    def test_triad2(self):
        theory2_triad = theory.Theory('#1974E6').triad()
        
        self.assertTupleEqual(('#1873E6', '#E61878', '#6FE618'), theory2_triad) 
        
    def test_tetradic1(self): 
        theory1_tetradic = theory.Theory('#B94685').tetradic()
        
        self.assertTupleEqual(('#B94685', '#B346B9', '#4BB946', '#B9464B', '#46B9B3'), theory1_tetradic)
        
    def test_tetradic2(self):
        theory2_tetradic = theory.Theory('#1974E6').tetradic()
        
        self.assertTupleEqual(('#1873E6', '#18DAE6', '#E62418', '#2418E6', '#DAE618'), theory2_tetradic)
        
    def test_square1(self): 
        theory1_square = theory.Theory('#B94685').square()
       
        self.assertTupleEqual(('#B94685', '#464BB9', '#46B979', '#B9B346'), theory1_square)
    
    def test_square2(self):
        theory2_square = theory.Theory('#1974E6').square()
        
        self.assertTupleEqual(('#1873E6', '#18E624', '#E68B18', '#E618DA'), theory2_square)
    
if __name__ == '__main__':
    unittest.main()
