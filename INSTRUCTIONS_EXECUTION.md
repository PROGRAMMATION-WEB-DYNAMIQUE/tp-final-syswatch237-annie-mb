# SysWatch : Instructions d'Exécution

Ce guide vous explique étape par étape comment lancer le serveur SysWatch et comment interagir avec lui en utilisant le client de test.

## Étape 1 : Lancer le Serveur Rust

Le serveur est le cœur du projet. Il collecte les métriques de votre ordinateur et attend les connexions.

1. Ouvrez un terminal dans VS Code (ou PowerShell/CMD).
2. Assurez-vous d'être dans le dossier du projet : `tp-final-syswatch237-KetsiaAnnaelle`.
3. Tapez la commande suivante pour compiler et lancer le serveur :
   ```bash
   cargo run
   ```
4. Vous devriez voir les métriques initiales s'afficher, suivies du message :
   **"Serveur en écoute sur port 7878..."**
5. **NE FERMEZ PAS** ce terminal. Le serveur doit continuer à tourner en arrière-plan. Il affichera `[refresh] Métriques mises à jour` toutes les 5 secondes.

---

## Étape 2 : Lancer le Client Python pour tester

Pour communiquer avec le serveur et voir le résultat des commandes (`cpu`, `mem`, etc.), nous allons utiliser un deuxième terminal.

1. Ouvrez un **nouveau terminal** (dans VS Code, cliquez sur l'icône `+` dans le panneau des terminaux pour ouvrir un nouvel onglet).
2. Vérifiez que vous êtes toujours dans le dossier `tp-final-syswatch237-KetsiaAnnaelle`.
3. Lancez le client interactif avec Python en tapant :
   ```bash
   python client.py
   ```
4. Le client va automatiquement se connecter au serveur et envoyer le mot de passe d'authentification (`ENSPD2026`).
5. Une fois connecté, vous verrez l'invite de commande : `syswatch>`.

---

## Étape 3 : Envoyer des requêtes au serveur

Depuis le terminal du client (où il est écrit `syswatch>`), vous pouvez taper les commandes suivantes et appuyer sur Entrée :

- **`cpu`** : Affiche l'usage actuel du processeur et une barre de progression.
- **`mem`** : Affiche l'état de la mémoire RAM (utilisée/totale).
- **`ps`** : Affiche le Top 5 des processus qui consomment le plus de ressources sur votre machine.
- **`all`** : Affiche un résumé complet (CPU + Mémoire + Processus).
- **`help`** : Affiche le menu d'aide.
- **`quit`** ou **`exit`** : Ferme la connexion du client.

---

## Étape 4 : Consulter les logs (Journalisation)

Le serveur enregistre l'historique de toutes les connexions dans un fichier texte.

1. Ouvrez le fichier **`syswatch.log`** situé à la racine du projet.
2. Vous y verrez l'heure exacte de chaque connexion, l'IP de l'utilisateur, et les commandes qui ont été tapées (ex: `commande: 'cpu'`).

---

## Comment tout arrêter ?

1. Dans le terminal du **Client** : Tapez `quit` pour arrêter le client.
2. Dans le terminal du **Serveur** : Appuyez sur `Ctrl + C` pour stopper le serveur proprement.
