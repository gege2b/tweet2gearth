tweet2gearth
============

Petit script python pour "traquer"  les gens qui géolocalisent leurs tweet et exporter ça dans un fichier KML

A la base, je l'ai fais pour m'entrainer à utiliser Python et Git 

Installation :
Installer Python (fonctionne normalement avec Python 2.7 et 3+)

Avant de pouvoir utiliser ce script, il faut installer la librairie TwitterAPI disponible ici : https://github.com/geduldig/TwitterAPI


**Configuration :**

Créer un fichier "oauth.py" contenant les informations suivantes : 

consumer_key='' 

consumer_secret='' 

access_token_key='' 

access_token_secret=''

et placez-le dans le même répertoire que le script. Il s'agit des clés pour l'API Twitter

Ces informations sont obligatoires, et pour les avoir il faut créer un compte "developpeur" sur Twitter ( https://dev.twitter.com/ ) et créer une application (qui sera utilisée par ce script par la suite)


**Fonctionnement :**

Depuis une ligne de commande, lancer le script : 
python tweet2geart pseudo_twitter

Si le pseudo est valide et s'il possède des tweet géolocalisés, un fichier KML sera créé.

**Paramètres :**

    python tweet2gearth.py [options] screen_name  
         -c X : retourne X tweets (defaut : 400)  
         -r : inclu les réponses aux tweet dans les résultats  
         -t : inclu les données de l'utilisateur dans les résultats  
         -rts : inclus les retweets  
         -n : Ne pas sauvegarder le fichier KML  
         -i : récupère les images de profile  
         screen_name : nom de l'utilisateur à tracker, obligatoire  