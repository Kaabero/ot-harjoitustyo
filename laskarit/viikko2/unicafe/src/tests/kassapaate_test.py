import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luodun_kassapaatteen_rahamaara_oikea(self):
        kassapaate=Kassapaate()
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_lounaiden_maara_oikea(self):
        kassapaate=Kassapaate()
        self.assertEqual(kassapaate.edulliset, 0)

    def test_myytyjen_maukkaiden_lounaiden_maara_oikea(self):
        kassapaate=Kassapaate()
        self.assertEqual(kassapaate.maukkaat, 0)

    def test_kateisosto_edullinen_kassa_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_maukas_kassa_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_edullinen_oikea_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_kateisosto_maukas_oikea_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_kateisosto_edullinen_lounaiden_maara(self):
        kassapaate=Kassapaate()
        kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(kassapaate.edulliset, 1)

    def test_kateisosto_maukas_lounaiden_maara(self):
        kassapaate=Kassapaate()
        kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(kassapaate.maukkaat, 1)


    def test_kateisosto_edullinen_raha_ei_riita_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_maukas_raha_ei_riita_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_edullinen_raha_ei_riita_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_kateisosto_maukas_raha_ei_riita_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_kateisosto_edullinen__raha_ei_riita_lounaiden_maara(self):
        kassapaate=Kassapaate()
        kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(kassapaate.edulliset, 0)

    def test_kateisosto_maukas_raha_ei_riita_lounaiden_maara(self):
        kassapaate=Kassapaate()
        kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(kassapaate.maukkaat, 0)


    def test_korttiosto_edullinen_kortin_saldo(self):
        kortti=Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 260)

    def test_korttiosto_maukas_kortin_saldo(self):
        kortti=Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 100)

    def test_korttiosto_edullinen_paluuarvo(self):
        kortti=Maksukortti(500)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti), "Test value is not true.")
        

    def test_korttiosto_maukas_paluuarvo(self):
        kortti=Maksukortti(500)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti), "Test value is not true.")

    def test_korttiosto_edullinen_lounaiden_maara(self):
        kortti=Maksukortti(500)
        kassapaate=Kassapaate()
        kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kassapaate.edulliset, 1)

    def test_korttiosto_maukas_lounaiden_maara(self):
        kortti=Maksukortti(500)
        kassapaate=Kassapaate()
        kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kassapaate.maukkaat, 1)


    def test_korttiosto_edullinen_epaonnistui_kortin_saldo(self):
        kortti=Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)

    def test_korttiosto_maukas_epaonnistui_kortin_saldo(self):
        kortti=Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 300)

    def test_korttiosto_edullinen__epaonnistui_paluuarvo(self):
        kortti=Maksukortti(200)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti), "Test value is not false.")
        

    def test_korttiosto_maukas_paluuarvo(self):
        kortti=Maksukortti(300)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti), "Test value is not false.")

    def test_korttiosto_edullinen__epaonnistui_lounaiden_maara(self):
        kortti=Maksukortti(200)
        kassapaate=Kassapaate()
        kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kassapaate.edulliset, 0)

    def test_korttiosto_maukas__epaonnistui_lounaiden_maara(self):
        kortti=Maksukortti(300)
        kassapaate=Kassapaate()
        kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kassapaate.maukkaat, 0)

    def test_kassa_ei_muutu_kortilla_osettaessa_edullisesti(self):
        kortti=Maksukortti(500)
        kassapaate=Kassapaate()
        kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_kassa_ei_muutu_kortilla_osettaessa_maukkaasti(self):
        kortti=Maksukortti(500)
        kassapaate=Kassapaate()
        kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kassapaate.kassassa_rahaa, 100000)

    def test_korttia_ladattaessa_kortin_saldo_muuttuu(self):
        kortti=Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 2000)
        self.assertEqual(kortti.saldo, 3000)

    def test_korttia_ladattaessa_kassan_saldo_muuttuu(self):
        kortti=Maksukortti(1000)
        kassapaate=Kassapaate()
        kassapaate.lataa_rahaa_kortille(kortti, 2000)
        self.assertEqual(kassapaate.kassassa_rahaa, 102000)

    def test_korttia_ladattaessa_nollalla_toimii(self):
        kortti=Maksukortti(1000)
        kassapaate=Kassapaate()
        
        self.assertEqual(kassapaate.lataa_rahaa_kortille(kortti, -1), None)

        




   