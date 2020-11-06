import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0" )

    def test_rahan_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 11.0")

    def test_vaheneeko_saldo_kortilta(self):
        maara = 240
        self.maksukortti.ota_rahaa(maara)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        return True

    def test_vaheneeko_saldo_kortilta_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(1200)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
        return False
    