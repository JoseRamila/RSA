import Crypto.Util.number
import hashlib

#Número de bits
bits = 1024

#Obtener los primos para Alice y Bob
pA = Crypto.Util.number.getPrime(bits, randfunc= Crypto.Random.get_random_bytes)
qA = Crypto.Util.number.getPrime(bits, randfunc= Crypto.Random.get_random_bytes)
print("PA es: ",pA,"\n")
print("QA es: ",qA,"\n")

pB = Crypto.Util.number.getPrime(bits, randfunc= Crypto.Random.get_random_bytes)
qB = Crypto.Util.number.getPrime(bits, randfunc= Crypto.Random.get_random_bytes)
print("PB es: ",pB,"\n")
print("QB es: ",qB,"\n")

#Obtener la primera parte de la llave pública de Alice y Bob
nA = pA * qA
print("NA es: ", nA,"\n")
nB = pB * qB
print("NB es: ", nB,"\n")

#Calculamos el indicador de Euer Phi
phiA = (pA - 1)*(qA - 1)
print("PHIA es: ", phiA,"\n")
phiB = (pB - 1)*(qB - 1)
print("PHIB es: ", phiB,"\n")

#Por razones de eficiencia usaremos el número 4 de Fermat, 65537, debido a que es un primo largo y no tiene potencia de 2 y como forma parte
# de la clave pública no es necesario calcularlo 

Fermat = 65537

#Calcular la llave privada de Alice y Bob
dA = Crypto.Util.number.inverse(Fermat, phiA)
print("DA es: ", dA,"\n")
dB = Crypto.Util.number.inverse(Fermat, phiB)
print("DB es: ", dB,"\n")

#Ciframos el mensaje 
msg = 'Hola mundo'
print("Mensaje original: ", msg,"\n")
print("Longitud de mensajes en bytes: ", len(msg.encode('utf-8')))
hashed_msg = hashlib.sha256(msg.encode()).hexdigest()
hashed_msg_integer = int(hashed_msg, 16)



#Convertir mensaje a número 
m = int.from_bytes(msg.encode('utf-8'), byteorder='big')
print("Mensaje convertido en entero: ", m, "\n")

c = pow(m,Fermat,nB)
print("Mensaje cifrado: ", c, "\n")

#Desciframos el mensaje
des = pow(c,dB,nB)
print("Mensaje descifrado: ", des, "\n")

msg_final = int.to_bytes(des,len(msg), byteorder = 'big').decode('utf-8')
print("Mnesaje final: ", msg_final, "\n")

#Verificar firma
C = pow(hashed_msg_integer,dA,nA)
comprobar = pow(C,Fermat,nA)
if comprobar == hashed_msg_integer:
    print("La firma es correcta", "\n")
else:
    print("La forma es incorrecta", "\n")


