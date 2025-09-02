usuarios_web = {"Ana", "Luis", "Pedro", "Carla", "Sofía"}
usuarios_app = {"Pedro", "María", "Ana", "José"}
print("----"*20)
#Determine los usuarios que usan ambas plataformas.
print(f"Usuarios que usan ambas plataformas: {usuarios_web & usuarios_app}")
print("----"*20)
#Determine los usuarios que usan solo la aplicación móvil
print(f"Usuarios que usan solo la aplicación móvil: {usuarios_app - usuarios_web}")

print("----"*20)
# Determine todos los usuarios únicos (sin repetición).
print(f"Todos los usuarios únicos: {usuarios_web | usuarios_app}")
print("----"*20)