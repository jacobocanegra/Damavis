import unittest
from proyecto_damavis import principal

class TestPrincipal(unittest.TestCase):
    def test_main_valid_labyrinth(self):
        # Prueba para un laberinto válido
        laberinto_valido = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
        resultado = principal.main(laberinto_valido)
        self.assertEqual(resultado, 2)  # El resultado esperado para este laberinto

    def test_main_invalid_labyrinth(self):
        # Prueba para un laberinto inválido
        laberinto_invalido = [[".", ".", "."], [".", "#", "."], [".", ".", "."]]
        resultado = principal.main(laberinto_invalido)
        self.assertEqual(resultado, -1)  # El resultado esperado para este laberinto inválido

    def test_main_invalid_size(self):
        # Prueba para un laberinto muy pequeño
        laberinto_pequeño = [[".", "."], [".", "."], [".", "."]]
        resultado = principal.main(laberinto_pequeño)
        self.assertEqual(resultado, -1)  # El resultado esperado para este laberinto inválido


if __name__ == '__main__':
    unittest.main()
