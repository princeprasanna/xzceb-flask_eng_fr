from translator import englishtofrench,frenchtoenglish
import unittest

class testenfr(unittest.TestCase):
    def test_eng_fr(self):
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertEqual(englishtofrench('Cabbage'),'Chou')
        self.assertNotEqual(englishtofrench('Table'),'Tableau')
        self.assertEqual(englishtofrench(''),'Empty')

class testfren(unittest.TestCase):
    def test_fr_eng(self):
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertEqual(frenchtoenglish('Chou'),'Cabbage')
        self.assertNotEqual(frenchtoenglish('Tableau'),'Table')
        self.assertEqual(frenchtoenglish(''),'Empty')

unittest.main()