import unittest
from app import validar_registro, validar_producto, validar_cliente, generar_token

class TestValidarRegistro(unittest.TestCase):

    def test_cuerpo_invalido(self):
        # Comprueba cuando 'data' no es un diccionario
        self.assertEqual(validar_registro(None), "Cuerpo de la peticion invalido")
        self.assertEqual(validar_registro("texto"), "Cuerpo de la peticion invalido")

    # Comprueba que el usuario no este vacio o sea invalido
    def test_username_invalido_o_vacio(self):
        self.assertEqual(validar_registro({"password": "1234"}), "El campo username es obligatorio")
        self.assertEqual(validar_registro({"username": "", "password": "1234"}), "El campo username es obligatorio")

    # Comprueba cuando la contraseña falta, está vacía o tiene menos de 4 caracteres
    def test_password_invalida_o_corta(self):
        self.assertEqual(validar_registro({"username": "user"}), "El campo password debe tener al menos 4 caracteres")
        self.assertEqual(validar_registro({"username": "user", "password": "123"}), "El campo password debe tener al menos 4 caracteres")

    #Crompueba cuando los datos son correctos (contraseña de 4 o mas caracteres y un usuario)
    def test_registro_correcto(self):
        self.assertIsNone(validar_registro({"username": "user", "password": "1234"}))

class TestValidarProducto(unittest.TestCase):
    def test_cuerpo_invalido(self):
        # Comprueba cuando 'data' no es un diccionario
        self.assertEqual(validar_registro(None), "Cuerpo de la peticion invalido")
        self.assertEqual(validar_registro("texto"), "Cuerpo de la peticion invalido")
    
    def test_username_vacio_(self):
        # Comprueba si falta el nombre o está vacío
        self.assertEqual(validar_producto({"precio": 10, "stock": 5}), "El campo nombre es obligatorio")
        self.assertEqual(validar_producto({"nombre": "", "precio": 10, "stock": 5}), "El campo nombre es obligatorio")

    def test_precio_invalido(self):
        # Comprueba si el precio es negativo o falta
        self.assertEqual(validar_producto({"nombre": "Teclado", "precio": -1, "stock": 5}), "El campo precio debe ser un numero >= 0")
        self.assertEqual(validar_producto({"nombre": "Teclado", "stock": 5}), "El campo precio debe ser un numero >= 0")

    def test_stock_invalido(self):
        # Comprueba si el stock es negativo o falta
        self.assertEqual(validar_producto({"nombre": "Teclado", "precio": 10, "stock": -1}), "El campo stock debe ser un entero >= 0")
        self.assertEqual(validar_producto({"nombre": "Teclado", "precio": 10}), "El campo stock debe ser un entero >= 0")

    def test_producto_correcto(self):
        # Comprueba el caso de éxito (devuelve None)
        self.assertIsNone(validar_producto({"nombre": "Teclado", "precio": 19.99, "stock": 10}))
        self.assertIsNone(validar_producto({"nombre": "Ratón", "precio": 0, "stock": 0}))

class TestValidarCliente(unittest.TestCase):
    def test_cuerpo_invalido(self):
        # Comprueba cuando 'data' no es un diccionario
        self.assertEqual(validar_cliente(None), "Cuerpo de la peticion invalido")
        self.assertEqual(validar_cliente("texto"), "Cuerpo de la peticion invalido")

    def test_nombre_vacio(self):
        # Comprueba cuando el nombre falta o está vacío
        self.assertEqual(validar_cliente({"email": "ana@test.com"}), "El campo nombre es obligatorio")
        self.assertEqual(validar_cliente({"nombre": "", "email": "ana@test.com"}), "El campo nombre es obligatorio")

    def test_email_invalido_o_ausente(self):
        # Comprueba cuando el email falta, está vacío o no tiene formato de correo válido (@ y dominio)
        self.assertEqual(validar_cliente({"nombre": "Ana"}), "El campo email no es valido")
        self.assertEqual(validar_cliente({"nombre": "Ana", "email": ""}), "El campo email no es valido")
        self.assertEqual(validar_cliente({"nombre": "Ana", "email": "correo_sin_arroba.com"}), "El campo email no es valido")

    def test_cliente_correcto(self):
        # Comprueba el caso de éxito (devuelve None)
        self.assertIsNone(validar_cliente({"nombre": "Ana", "email": "ana@test.com"}))

class TestGenerarToken(unittest.TestCase):

    def test_formato_y_longitud(self):
        # Comprueba que sea un texto y mida 32 caracteres
        token = generar_token()
        self.assertIsInstance(token, str)
        self.assertEqual(len(token), 32)

    def test_tokens_unicos(self):
        # Comprueba que dos llamadas seguidas generen tokens diferentes
        token1 = generar_token()
        token2 = generar_token()
        self.assertNotEqual(token1, token2)

if __name__ == "__main__":
    unittest.main()