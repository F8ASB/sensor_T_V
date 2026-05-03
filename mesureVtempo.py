import serial
import time

# --- Configuration du port série ---
PORT = "/dev/ttyUSB0"
BAUD = 9600

# --- Fichier de sortie ---
fichier_sortie = "/tmp/mesureV.txt"

# --- Temporisation avant la mesure (en secondes) ---
attente_avant_mesure = 10   # réglable

def main():
    try:
        print(f"Attente de {attente_avant_mesure} secondes avant la mesure...")
        time.sleep(attente_avant_mesure)

        ser = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(2)  # Laisse le temps à l'Arduino de se réinitialiser

        # Vide tout ce que l'Arduino a envoyé au démarrage
        ser.reset_input_buffer()

        # Envoi de la commande
        ser.write(b"V")
        ser.flush()

        # Lecture de la réponse
        time.sleep(0.3)
        ligne = ser.readline().decode(errors="ignore").strip()

        print("Reçu :", ligne)

        # Vérification de la validité
#        if ligne == "" or "Tension" not in ligne:
#            ligne = "erreur com"

        # Écriture en écrasant le fichier
        with open(fichier_sortie, "w") as f:
            f.write(ligne + "\n")

        print("Écrit dans :", fichier_sortie)

        ser.close()

    except Exception as e:
        with open(fichier_sortie, "w") as f:
            f.write("erreur com\n")
        print("Erreur :", e)

if __name__ == "__main__":
    main()
