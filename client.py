import socket

def run_client():
    try:
        # Connexion au serveur
        s = socket.socket()
        s.connect(('localhost', 7878))
        print(s.recv(1024).decode(errors='ignore').strip()) # TOKEN:
        
        # Envoi du token
        s.send(b'ENSPD2026\n')
        print(s.recv(1024).decode(errors='ignore').strip()) # OK ou UNAUTHORIZED
        
        print("\n--- Vous êtes connecté au serveur SysWatch ! ---")
        print("Tapez 'help' pour voir les commandes. Tapez 'quit' pour quitter.\n")

        while True:
            cmd = input("syswatch> ")
            s.send((cmd + '\n').encode('utf-8'))
            
            # Lecture de la réponse jusqu'à trouver "END" ou que le serveur ferme
            if cmd.lower() in ('quit', 'exit'):
                print(s.recv(1024).decode(errors='ignore').strip())
                break
                
            response = ""
            while "END" not in response:
                chunk = s.recv(4096).decode(errors='ignore')
                if not chunk:
                    break
                response += chunk
            
            # Afficher sans le mot "END" à la fin
            print(response.replace("END\n", "").strip() + "\n")
            
    except ConnectionRefusedError:
        print("Erreur: Impossible de se connecter. Assurez-vous que le serveur tourne (cargo run).")

if __name__ == "__main__":
    run_client()
