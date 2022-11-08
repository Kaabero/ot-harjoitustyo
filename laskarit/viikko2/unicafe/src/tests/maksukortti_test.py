import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_rahan_ottaminen_toimii_jos_rahaa_tarpeeksi(self):
        kortti=Maksukortti(1000)
        kortti.ota_rahaa(500)
        
        self.assertEqual(str(kortti), "Kortilla on rahaa 5.00 euroa")
        

    def test_rahan_ottaminen_toimii_jos_rahaa_liian_vahan(self):
        kortti=Maksukortti(500)
        kortti.ota_rahaa(1000)

        self.assertEqual(str(kortti), "Kortilla on rahaa 5.00 euroa")
        

    def test_rahan_otto_palauttaa_true_toimiessaan(self):
        kortti=Maksukortti(1000)
        
        self.assertTrue(kortti.ota_rahaa(500), "Test value is not true.")

    def test_rahan_otto_palauttaa_false_jos_rahaa_liian_vahan(self):
        kortti=Maksukortti(500)
        
        self.assertFalse(kortti.ota_rahaa(1000), "Test value is not false.")
