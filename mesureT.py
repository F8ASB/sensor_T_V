import serial
import time
import re

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Laisse l'Arduino redémarrer
time.sleep(2)

# Vide tout ce que l'Arduino a envoyé au démarrage
ser.reset_input_buffer()

# Envoie la commande T
ser.write(b'T\r\n')

# Lit la réponse
response = ser.readline().decode(errors='ignore').strip()
print("Réponse brute :", response)

match = re.search(r"T=([0-9]+\.[0-9]+)", response)
if match:
    print("Température :", match.group(1))
else:
    print("Format inattendu :", response)

ser.close()
