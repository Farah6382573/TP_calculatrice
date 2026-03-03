# tests/test_calculatrice.py
import unittest
from src.calculatrice import division, puissance, moyenne

class TestCalculatrice(unittest.TestCase):

    # DIVISION 

    def test_division_entiers(self):
        self.assertEqual(division(10, 2), 5)

    def test_division_decimales(self):
        self.assertEqual(division(5, 2), 2.5)

    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(10, 0)

    # PUISSANCE 

    def test_puissance_positive(self):
        self.assertEqual(puissance(2, 3), 8)

    def test_puissance_exposant_zero(self):
        self.assertEqual(puissance(5, 0), 1)

    def test_puissance_exposant_negatif(self):
        with self.assertRaises(ValueError):
            puissance(2, -3)

    # MOYENNE

    def test_moyenne_plusieurs_valeurs(self):
        self.assertEqual(moyenne([2, 4, 6, 8]), 5)

    def test_moyenne_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])
     # Exécution des tests
                
unittest.TextTestRunner().run( unittest.TestLoader().loadTestsFromTestCase(TestCalculatrice) )