import serial
import time
import os

# --- Configuration du port série ---
PORT = "/dev/ttyUSB0"   # À adapter selon ton système (ex: COM3 sous Windows)
BAUD = 9600

# --- Fichier de sortie dans le répertoire de l'application ---
fichier_sortie = "/tmp/mesureV.txt"

def main():
    try:
        # Ouverture du port série
        ser = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(20)  # Laisse le temps à l'Arduino de se réinitialiser

        # Envoi de la commande
        ser.write(b"V")
        ser.flush()

        # Lecture de la réponse
        time.sleep(0.2)
        ligne = ser.readline().decode(errors="ignore").strip()
        print(ligne)

        # Sauvegarde dans le fichier
        with open(fichier_sortie, "w") as f:
            f.write(ligne + "\n")

        print(f"Mesure enregistrée dans : {fichier_sortie}")

        ser.close()

    except Exception as e:
        print("Erreur :", e)

if __name__ == "__main__":
    main()
