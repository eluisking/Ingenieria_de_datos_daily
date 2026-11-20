from logging import exception


def greting(name: str):
    try:
        print("Hola " + name)
    except TypeError:
        print("El tipo de dato enviado en 'name' no es correcto.")


greting(32)


# Simulamos tus funciones para que el código corra
def validate_name(n): return len(n) > 2
def validate_email(e): return "@" in e
def validate_password(p): return len(p) > 5

# Tu función corregida
def validate_user(name, email, password):
    try:
        # Evaluamos directamente el resultado de las 3 funciones como una tupla (Booleano, Booleano, Booleano)
        match (validate_name(name), validate_email(email), validate_password(password)):
            
            # Si el primero es False (no importa el resto, por eso usamos _)
            case (False, _, _):
                raise ValueError("El nombre no es válido!!")
                
            # Si el segundo es False
            case (_, False, _):
                raise ValueError("El email no es válido!!")
                
            # Si el tercero es False
            case (_, _, False):
                raise ValueError("El password no es válido!!")
                
            # Si los tres son True
            case (True, True, True):
                print(f"El registro del usuario: {name}, fue exitoso!")
                return True
                
            case _:
                raise ValueError("Uno o más campos no son válidos!!")
                
    except ValueError as error:
        print(f"El registro falló! --> {error}")
        return False # Es buena práctica retornar False si algo salió mal

# Pruebas
print("Prueba 1:")
validate_user("Luis", "luis@gmail.com", "luis1234")

print("\nPrueba 2 (Falla el email):")
validate_user("Luis", "luisgmail.com", "luis1234")