## Université Numérique
### Authentification
  Ce projet vise à créer une plateforme d'université numérique via un site web, avec un accent particulier sur l'authentification des utilisateurs.       L'authentification sécurisée est essentielle pour garantir la confidentialité et la sécurité des données des étudiants et du personnel.

## Fonctionnalités de l'Authentification
  1. Inscription des Utilisateurs
      Pour s'inscrire sur la plateforme, les utilisateurs doivent fournir les informations suivantes :

        Nom d'utilisateur
        Adresse e-mail
        Mot de passe
      Le processus d'inscription garantit que les informations sont valides et stocke les utilisateurs inscrits dans une base de données sécurisée.

  2. Vérification de la Force du Mot de Passe
      Lors de l'inscription, les utilisateurs sont guidés pour créer un mot de passe fort, qui doit respecter les critères suivants :
      
      Longueur minimale de 8 caractères
      Inclusion de lettres majuscules et minuscules
      Inclusion de chiffres
      Inclusion de caractères spéciaux
    Les utilisateurs sont informés des exigences de mot de passe et invités à réessayer en cas d'échec. Après trois tentatives infructueuses, un            utilisateur doit attendre 3 minutes avant de pouvoir faire une nouvelle tentative.

  3. Changement de Mot de Passe Périodique
      Les utilisateurs sont tenus de changer leur mot de passe tous les trois mois pour des raisons de sécurité. Des rappels sont intégrés pour               informer les utilisateurs du besoin de changer leur mot de passe.

  4. Cryptage des Mots de Passe
    Les mots de passe des utilisateurs sont stockés de manière sécurisée en utilisant l'algorithme de hachage bcrypt. Cela garantit que les mots de         passe ne sont pas stockés en texte brut dans la base de données et sont protégés contre les attaques de force brute.
  
  ## Instructions d'Utilisation
    Clonez ce référentiel sur votre système local.
    Assurez-vous d'avoir Python installé sur votre système.
    Exécutez le programme en utilisant python app.py.
  ## Auteur
   # Souleymane HAMANE ADJI
