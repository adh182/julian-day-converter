from JDMasehiConverter import JDKeMasehi, MasehiKeJD
import unittest

class Test(unittest.TestCase):

	def test_greg1(self):
		year = 2021
		month = 4
		day = 9
		expected = 2459313.5
		result = MasehiKeJD(year, month, day).konversi_ke_JD()
		self.assertEqual(expected, result)

	def test_greg2(self):
		year = 1945
		month = 8
		day = 17
		expected = 2431684.5
		result = MasehiKeJD(year, month, day).konversi_ke_JD()
		self.assertEqual(expected, result)

	def test_jd1(self):
		jd = 2345214.5
		expected = '1708/11/17   0:0:0'
		result = JDKeMasehi(jd).konversi_ke_masehi()
		self.assertEqual(expected, result)

	def test_jd2(self):
		jd = 2652314.5
		expected = '2549/9/9   0:0:0'
		result = JDKeMasehi(jd).konversi_ke_masehi()
		self.assertEqual(expected, result)

unittest.main()