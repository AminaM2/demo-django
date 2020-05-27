# Demo Django - Installations
Projet séminaire

<p>Étapes pour configurer votre environnement sur Windows*:</p>
<p>*Pour configuration sur un autre système d'eploitation, voir la source fournie en bas du fichier</p>

<p>(Optionnel) : télécharger l'éditeur de texte Sublime que j'utiliserais durant ce séminaire.</p>

<p><b>Partie 1- Installer Python</b></p>

<ol>
	<li>Aller sur https://www.python.org/downloads/ et télécharger la dernière version de python (3.8.3). Télécharger l'installateur adapté à votre système (Windows x86-64 executable installer dans le cas d'un système X64).</li>
	<li>Ouvrir l'installateur Python et sélectionner/cocher l'option "Add Python 3.8 to PATH")</li>
	<li>**Sélectionner/cocher l'option "Customize Installation"</li>
	<li>Cliquer sur "Next"</li>
	<li>Sélectionner/cocher les options suivantes:
			<ul>
				<li>"Install for all users"</li>
				<li>"Add Python to environment variables"</li>
				<li>"Create shortcuts for installed applications"</li>
				<li>"Precompile standard library"</li>
			</ul>
	</li>
	<li>Personnaliser l'emplacement d'installation et entrer plutôt "C:\Python38"</li>
	<li>Cliquer sur "Install"</li>
	<li>
    <p>Vérifier que Python a bien été installé en ouvrant PowerShell et en entrant la commande suivante:</p>
		<code>python -V</code>
	</li>
	<li>
    <p>Vérifier que pip a bien été installé en entrant la commande suivante:</p>
		<code>pip freeze</code>
		<p>Si le message "'pip' is not recognized as the name..." apparaît, c'est que l'installation n'a pas été effectuée correctement.
      Sinon, vous pouvez poursuivre.
    </p>
	</li>
</ol>
  
<p><b>Partie 2 - Modifier les paramètres de PowerShell</b></p>

<ol>
	<li>Ouvrir PowerShell en mode administrateur</li>
	<li>Entrer la commande suivante:<br><br>
		<code>Set-ExecutionPolicy Unrestricted</code>
	</li>
</ol>

<p><b>Partie 3 - Créer l'environnement virtuel </b></p>
<ol>
	<li>
		<p>Ouvrir PowerShell et créer un répertoire "Dev"</p>
		<code>cd ~</code><br>
		<code>mkdir Dev</code><br>
	</li>
	<li>
		<p>Installer Pipenv (gestionnaire d'environnement virtuel)</p>
		<code>python -m pip install pipenv</code>
		<p>L'utilisation de python -m permet de définitivement se servir de la version de python que nous venons d'installer</p>
		<p><b>Lorsque vous verrez > avant une ligne de code, c’est qu’elle devra être exécutée dans PowerShell</b></p>
	</li>
	<li>
		<p>Vérifier que pipenv a bien été installé en entrant la commande suivante:</li></p>
		<code>> pipenv</code></br><br>
		<p>Celle-ci devrait être reconnue comme une commande et des options devraient vous être suggérées.</p>
	</li>
	<li>
  <p>
    Aller dans le dossier Dev et ajouter un nouveau dossier pour créer notre environnement virtuel,puis aller dans ce dossier
    nouvellement créé:
  </p>
    <code>> cd ~Dev</code><br>
    <code>> mkdir demo</code><br>
    <code>> cd demo</code><br>
	</li>
	<li>
    <p>Exéctuer la commande suivante:</p>
		<code>> pipenv install</code>
    <p>L'utilisation de pipenv install permettra d'utiliser votre python par défaut.</p>
	</li>
</ol>

<p><b>Partie 4 - Activer son environnement et vérifier que tout est fonctionnel</b></p>
<ol>
<li>
    <p>Activer son environnement:</p>
    <code>> cd Dev/demo</code><br>
    <code>> pipenv shell</code><br>
	<p>
      Une fois votre environnement activé, vous pouvez installer tous les packages que vous voulez et ils n'auront pas d'impact 
      sur vos autres projets dans d'autres environnements, dans l'éventualité où vous utiliseriez différentes versions du même package
      dans 2 projets différents.
     </p>
	</li>
	<li>
		Le (demo) est le nom du répertoire contenant l'environnement virtuel. Lorsque vous voyez cela, ça signifie que l'environnement
    virtuel a été activé.
  </li>
  <li>
    <p>Exécutez la commande suivante:</p>
    <code>(demo) > pip freeze</code><br>
    <p>Vous ne devriez rien voir à ce point étant donné que nous n'avons installé aucun package à date.</p>
  </li>
  <li>
    <p>Pour désactiver son environnement, il suffit d'exécuter la commande suivante:</p>
    <code>
      deactivate
    </code>
  </li>
</ol>		
		
<p><b>Partie 5 - Clôner le répertoire git</b></p>
<p>Se rendre à l’url suivante et cloner le répertoire git suivant dans votre environnement virtuel (demo) :<p>
<p>https://github.com/AminaM2/demo-django</p>

<code>git clone https://github.com/AminaM2/demo-django.git</code><br>

<p><b>Partie 6 – Installer les dépendances</b></p>
<p>*Avoir son environnement virtuel activé</p>
<pre>
(demo) > cd demo-django
(demo) > pip install -r requirements.txt
</pre>

<p><b>Partie 7 – Partir l’application</p></b>
<p>Partir le serveur et vérifier que l’application part sans problème :</p>
<code>(demo) > python manage.py runserver</code>

<p>Pour installation sur Windows:
https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10</p>

<p>Pour installation sur Linux:
https://www.codingforentrepreneurs.com/blog/install-django-on-linux-ubuntu/</p>

<p>Pour installation sur Mac:
https://www.codingforentrepreneurs.com/blog/install-django-on-mac-or-linux/</p>
