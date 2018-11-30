"""Manejo de excepciones
"""
try:
   edad = input("Ingrese su edad: \n")
   edad = int(edad)
   print("Su edad es %d" % (edad))
except NameError as e:
   print("Existe un error %s" % e)

except ValueError as e:
   print("Existe un error (%s): %s" % (e.__class__, e))