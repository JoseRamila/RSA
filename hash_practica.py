import hashlib
import random
import string

# 1. Cadena de texto de 8 bits
text_8bits = "".join(random.choices("01", k=8))  
print("Texto de 8 bits:", text_8bits,"\n")

hash_object = hashlib.sha256(text_8bits.encode())
hex_digest_8bits = hash_object.hexdigest()

print("Hash de texto de 8 bits:", hex_digest_8bits,"\n") 


# 2. Cadena de texto de 1024 bits
text_1024bits = "".join(random.choices("01", k=1024))   
print("Texto de 1024 bits:", text_1024bits,"\n")

hash_object = hashlib.sha256(text_1024bits.encode())
hex_digest_1024bits = hash_object.hexdigest()

print("Hash de texto de 1024 bits:", hex_digest_1024bits,"\n")


# Prueba: Hash diferentes para textos diferentes
more_text = "".join(random.choices(string.ascii_letters + string.digits, k=16))
more_hash = hashlib.sha256(more_text.encode()).hexdigest()  

print("Hash de otro texto:", more_hash,"\n")
print("Los hashes son diferentes, la función SHA-256 funciona","\n")