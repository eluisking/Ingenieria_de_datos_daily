def greting(name):
    if type(name) == str:
        print(f"Hola {name}")
    else:
        raise TypeError(
            "Lo siento el argumento 'name' solo admite el tipo de String, por favor validalo."
        )


greting("Luis")
