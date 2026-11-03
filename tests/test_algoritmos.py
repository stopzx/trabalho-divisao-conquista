import unittest
from algoritmos import (
    max_subarray_bruteforce, max_subarray_divide_conquer, max_subarray_kadane,
    closest_pair_bruteforce, closest_pair_divide_conquer
)

class TestSubarranjo(unittest.TestCase):
    def test_exemplo_misto(self):
        v = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        esperado = (6, 3, 6)
        self.assertEqual(max_subarray_bruteforce(v), esperado)
        self.assertEqual(max_subarray_divide_conquer(v), esperado)
        self.assertEqual(max_subarray_kadane(v), esperado)

    def test_todos_negativos(self):
        v = [-8, -3, -6, -2, -5]
        esperado = (-2, 3, 3)
        for f in (max_subarray_bruteforce, max_subarray_divide_conquer, max_subarray_kadane):
            self.assertEqual(f(v), esperado)

    def test_tamanho_um(self):
        for f in (max_subarray_bruteforce, max_subarray_divide_conquer, max_subarray_kadane):
            self.assertEqual(f([7]), (7, 0, 0))

    def test_empate(self):
        v = [1, -1, 1]
        esperado = (1, 0, 0)
        for f in (max_subarray_bruteforce, max_subarray_divide_conquer, max_subarray_kadane):
            self.assertEqual(f(v), esperado)

    def test_vazio(self):
        for f in (max_subarray_bruteforce, max_subarray_divide_conquer, max_subarray_kadane):
            with self.assertRaises(ValueError):
                f([])

class TestParMaisProximo(unittest.TestCase):
    def comparar(self, pontos):
        a = closest_pair_bruteforce(pontos)
        b = closest_pair_divide_conquer(pontos)
        self.assertAlmostEqual(a[0], b[0], places=10)

    def test_pontos_simples(self):
        self.comparar([(0, 0), (5, 5), (1, 1), (9, 9)])

    def test_pontos_repetidos(self):
        self.comparar([(0, 0), (0, 0), (5, 5), (8, 8)])

    def test_alinhados(self):
        self.comparar([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)])

    def test_dois_pontos(self):
        self.comparar([(2, 3), (5, 7)])

    def test_menos_de_dois(self):
        for f in (closest_pair_bruteforce, closest_pair_divide_conquer):
            with self.assertRaises(ValueError):
                f([(0, 0)])

if __name__ == "__main__":
    unittest.main()
