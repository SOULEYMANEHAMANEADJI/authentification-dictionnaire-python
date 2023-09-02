import bcrypt
import time

# Dictionnaire pour stocker les utilisateurs (simulé ici, vous devriez utiliser une base de données)
users = {}

# Dictionnaire pour stocker les tentatives infructueuses
failed_login_attempts = {}

# Fonction pour vérifier la force du mot de passe
def is_password_strong(password):
    # Vous pouvez définir vos propres critères ici, par exemple, une longueur minimale de 8 caractères
    return len(password) >= 8

# Fonction pour enregistrer un nouvel utilisateur
def register_user():
    username = input("Entrez un nom d'utilisateur : ")
    email = input("Entrez une adresse e-mail : ")
    password = input("Entrez un mot de passe : ")
    
    if username in users:
        print("Nom d'utilisateur déjà utilisé. Veuillez en choisir un autre.")
        return
    
    if is_password_strong(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        users[username] = {'email': email, 'password': hashed_password}
        print("Inscription réussie.")
    else:
        print("Le mot de passe ne répond pas aux critères de sécurité.")

# Fonction pour vérifier l'authentification de l'utilisateur
def authenticate_user():
    username = input("Entrez votre nom d'utilisateur : ")
    password = input("Entrez votre mot de passe : ")

    if username not in users:
        print("Nom d'utilisateur incorrect.")
        return
    
    stored_password = users[username]['password']
    
    if bcrypt.checkpw(password.encode('utf-8'), stored_password):
        # Réinitialiser les tentatives infructueuses
        if username in failed_login_attempts:
            failed_login_attempts[username] = 0
        print("Authentification réussie.")
    else:
        # Incrémenter le compteur de tentatives infructueuses
        if username in failed_login_attempts:
            failed_login_attempts[username] += 1
        else:
            failed_login_attempts[username] = 1
        
        # Vérifier si l'utilisateur a dépassé le nombre maximal de tentatives
        if failed_login_attempts[username] >= 3:
            print("Trop de tentatives infructueuses. Veuillez attendre 3 minutes.")
            time.sleep(180)
        else:
            print("Mot de passe incorrect.")

# Exemple d'utilisation
if __name__ == '__main__':
    print("Bienvenue sur notre site d'inscription et d'authentification.")
    
    while True:
        print("\nMenu :")
        print("1. S'inscrire")
        print("2. Se connecter")
        print("3. Lister les utilisateurs enregistrés")
        print("4. Quitter")
        
        choix = input("Choisissez une option (1/2/3/4) : ")
        
        if choix == '1':
            register_user()
        elif choix == '2':
            authenticate_user()
        elif choix == '3':
            if users:
                print("Utilisateurs enregistrés :")
                for username, data in users.items():
                    print(f"Nom d'utilisateur : {username}, Email : {data['email']}")
            else:
                print("Aucun utilisateur inscrit !")
        elif choix == '4':
            print("Bye bye !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
