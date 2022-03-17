#el concepto dir es muy importante en el lenguaje de programacion de python
Ejemplo = "Salvador Enriquez"
print (dir(Ejemplo))
#lo que sale son las cosas que le podemos agregar para editar el texto por ejemplo
#es importante que cada que se ponga algo asi del directorio lleve el () al final como se muestra
print (Ejemplo.upper())
print (Ejemplo.replace("Salvador", "Chavtia"))
#tambien se le pueden agregar mas direcctorios a estos ejemplos como lo siguiente
print (Ejemplo.replace("Salvador", "Chavtia").upper())
#No en todos los casos aplica el punto 5. como se muetsra acontinuacion
#aqui lo que hace es contar el numero de veces que sale lo indicado en ""
print (Ejemplo.count ("Salvador"))
print (Ejemplo.count("a"))
