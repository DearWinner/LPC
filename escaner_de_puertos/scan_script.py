import nmap
#Aaron Avila Mata 1998679 Grupo:062
def escaneo_udp(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-sU')
    return scanner.scaninfo()
def escaneo_completo(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-p 1-65535')
    return scanner.scaninfo()
def deteccion_sistema_operativo(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-O')
    return scanner.scaninfo()
def escaneo_con_ping(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, arguments='-sn')
    return scanner.scaninfo()
def seleccionar_opcion(opcion, target):
    if opcion == 1:
        resultado = escaneo_udp(target)
        print(f"Escaneo UDP:\n{resultado}\n")
    elif opcion == 2:
        resultado = escaneo_completo(target)
        print(f"Escaneo completo:\n{resultado}\n")
    elif opcion == 3:
        resultado = deteccion_sistema_operativo(target)
        print(f"Detección de sistema operativo:\n{resultado}\n")
    elif opcion == 4:
        resultado = escaneo_con_ping(target)
        print(f"Escaneo de red con ping:\n{resultado}\n")
    else:
        print("Opción no válida. Por favor, elige un número del 1 al 4.")

# Ejemplo de uso
target = '127.0.0.1'

print("Selecciona el tipo de escaneo:")
print("1) Escaneo UDP")
print("2) Escaneo completo")
print("3) Detección de sistema operativo")
print("4) Escaneo de red con ping")

opcion = int(input("Ingresa el número de opción: "))

seleccionar_opcion(opcion, target)
