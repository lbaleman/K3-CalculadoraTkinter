import unittest
from romanosClase import romano_a_arabigo, contarParentesis, arabigo_a_romano, dividirgt1000
from romannumber import RomanNumber

class RomanNumberTest(unittest.TestCase):
    def test_symbols_romas(self):
        self.assertEqual(romano_a_arabigo('I'),1)
        self.assertEqual(romano_a_arabigo('V'),5)
        self.assertEqual(romano_a_arabigo('X'),10)
        self.assertEqual(romano_a_arabigo('XIV'),14)
        self.assertEqual(romano_a_arabigo('XV'),15)
        self.assertEqual(romano_a_arabigo('XL'),40)
        self.assertEqual(romano_a_arabigo('L'),50)
        self.assertEqual(romano_a_arabigo('C'),100)
    
    def test_crecients_romas(self):
        self.assertEqual(romano_a_arabigo('III'),3)
        self.assertEqual(romano_a_arabigo('XVI'),16)
        self.assertEqual(romano_a_arabigo('XIV'),14)
        self.assertEqual(romano_a_arabigo('XXXX'),0)
        self.assertEqual(romano_a_arabigo('XLVII'),47)
        self.assertEqual(romano_a_arabigo('IIII'),0)
        self.assertEqual(romano_a_arabigo('LXXIII'),73)
        self.assertEqual(romano_a_arabigo('CMXCIX'),999)
        self.assertEqual(romano_a_arabigo('MIIX'),0)
        self.assertEqual(romano_a_arabigo('CLIX'),159)
        self.assertEqual(romano_a_arabigo('VC'),0)
        self.assertEqual(romano_a_arabigo('IC'),0)
        self.assertEqual(romano_a_arabigo('IX'),9)
        self.assertEqual(romano_a_arabigo('XC'),90)
        self.assertEqual(romano_a_arabigo('IL'),0)
        self.assertEqual(romano_a_arabigo('CM'),900)
        self.assertEqual(romano_a_arabigo('VV'),0)

    def test_procesar_parentesis(self):
        self.assertEqual(contarParentesis('(IV)'),[[1,'IV'],[0,'']])
        self.assertEqual(contarParentesis('((VII))(XL)CCCXXII'),[[2,'VII'],[1,'XL'],[0,'CCCXXII']])
        self.assertEqual(contarParentesis('(VI)((VII))'),0)
        self.assertEqual(contarParentesis('(VI)((VII)'),0)
        #self.assertEqual(contarParentesis('VI)((VII'),0)

class ArabicNumberTest(unittest.TestCase):
    def test_unidades(self):
        self.assertEqual(arabigo_a_romano(1), 'I')
        self.assertEqual(arabigo_a_romano(23), 'XXIII')
        self.assertEqual(arabigo_a_romano(4), 'IV')

    def test_arabic_a_roman(self):
        self.assertEqual(arabigo_a_romano(2123), 'MMCXXIII')
        self.assertEqual(arabigo_a_romano(2444), 'MMCDXLIV')
        self.assertEqual(arabigo_a_romano(3555), 'MMMDLV')
        self.assertEqual(arabigo_a_romano(1678), 'MDCLXXVIII')
        self.assertEqual(arabigo_a_romano(2999), 'MMCMXCIX')

    def test_arabic_a_roman_gt_3999(self):
        self.assertEqual(arabigo_a_romano(4000), '(IV)')
        self.assertEqual(arabigo_a_romano(7763147686), '(((VII)))((DCCLX))(MMMCXLVII)DCLXXXVI')
        
    def test_gruposde1000(self):
        self.assertEqual(dividirgt1000(7763147686), [[3,7],[2,760],[1,3147],[0,686]])
        self.assertEqual(dividirgt1000(3763142686), [[3,0], [2,3760],[1,3140],[0,2686]])
        self.assertEqual(dividirgt1000(763142686), [[2,760],[1,3140],[0,2686]])

class RomanNumberClassTest(unittest.TestCase):
    def test_create_romannumber(self):
        nr = RomanNumber(23)
        self.assertEqual((str(nr)), 'XXIII')

        otro= RomanNumber('XXIII')
        self.assertEqual(otro.value, 23)
    
if __name__=='__main__':
    unittest.main()
