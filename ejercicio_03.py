def versiones_de(biblioteca, versiones, cancion_id) -> list:
    """Lista de (titulo, tipo) de todo lo derivado, sin incluir la canción original."""
    biblioteca.obtener(cancion_id)
    directas = []
    for v_id, version_de_id, tipo in versiones:
        if version_de_id == cancion_id:
            directas.append((v_id, tipo))
    if not directas:
        return []
    directas.sort()
    resultado = []
    for v_id, tipo in directas:
        cancion = biblioteca.obtener(v_id)
        resultado.append((cancion.titulo, tipo))
        resultado.extend(versiones_de(biblioteca, versiones, v_id))
    return resultado
'''
TEORÍA

Caso base: si ninguna canción en versiones tiene version_de_id == cancion_id, devuelve [].
Secuencia de llamadas para versiones_de(..., 12):
    1. versiones_de(..., 12) encuentra la versión directa 13 ("Ji Ji Ji", "live") y llama a versiones_de(..., 13).   
    2. versiones_de(..., 13) encuentra la versión directa 70 ("Ji Ji Ji (Remix)", "remix") y llama a versiones_de(..., 70).   
    3. versiones_de(..., 70) no tiene versiones derivadas (caso base) y devuelve [].
    4. Vuelve a versiones_de(..., 13), suma lo que devolvió la 70 y retorna [("Ji Ji Ji (Remix)", "remix")].
    5. Vuelve a versiones_de(..., 12), suma lo que devolvió la 13 y retorna [("Ji Ji Ji", "live"), ("Ji Ji Ji (Remix)", "remix")].  
'''