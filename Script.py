# N'enlevez pas le crédit @VJ_Botz
# Abonnez-vous à la chaîne YouTube pour un bot incroyable @Tech_VJ
# Posez vos questions sur Telegram @KingVJ01

class script(object):
    START_TXT = """<b><blockquote>Salut {} 👋,</blockquote>

Je suis le dernier robot de filtrage automatique avancé et puissant. Vous pouvez m'utiliser dans votre groupe pour gagner de l'argent sans limite...💸</b>"""

    CLONE_START_TXT = """<b><blockquote>Salut {}, je m'appelle <a href=https://t.me/{}>{}</a></blockquote>

Je suis un robot de filtrage automatique avancé et puissant avec des fonctionnalités étonnantes, tapez simplement ce que vous voulez puis voyez ma puissance 💘</b>"""
    
    HELP_TXT = """<b>Salut {}
Voici toutes mes fonctionnalités utiles.</b>"""

    ABOUT_TXT = """<b><blockquote>⍟───[ MES DÉTAILS ]───⍟</blockquote>

‣ Mon nom : <a href=https://t.me/{}>{}</a>
‣ Mon meilleur ami : <a href='tg://settings'>Cette personne</a>
‣ Développeur : <a href={}>Propriétaire</a>
‣ Bibliothèque : <a href='https://docs.pyrogram.org/'>Pyrogram</a>
‣ Langage : <a href='https://www.python.org/download/releases/3.0/'>Python 3</a>
‣ Base de données : <a href='https://www.mongodb.com/'>Mongo DB</a>
‣ Serveur Bot : <a href='https://heroku.com'>Heroku</a>
‣ État de la construction : v2.7.1 [stable]></b>"""

    CLONE_ABOUT_TXT = """<b><blockquote>⍟───[ À PROPOS DE MOI ]───⍟</blockquote>

‣ Mon nom : {}
‣ Mon meilleur ami : <a href='tg://settings'>Cette personne</a>
‣ Cloné de : <a href=https://t.me/{}>{}</a>
‣ Bibliothèque : <a href='https://docs.pyrogram.org/'>Pyrogram</a>
‣ Langage : <a href='https://www.python.org/download/releases/3.0/'>Python 3</a>
‣ Base de données : <a href='https://www.mongodb.com/'>Mongo DB</a>
‣ État de la construction : v2.7.1 [stable]></b>"""

    CLONE_TXT = """<b>🌟 <u>MODE CLONE</u>

- Vous créez votre propre Bot Clone par la commande /clone
- Vous pouvez diffuser dans vos Bots Clones
- Et des millions de fichiers indexés déjà, pas besoin d'ajouter de fichier

👨‍💻 Commande : /clone</b>"""

    SUBSCRIPTION_TXT = """
<b>Parrainez votre lien à vos amis, votre famille, votre chaîne et votre groupe pour obtenir gratuitement Premium pendant {}

Lien de parrainage - https://telegram.me/{}?start=VJ-{}

Si {} utilisateur unique démarre le bot avec votre lien de parrainage, vous serez automatiquement ajouté à la liste Premium.

Acheter un forfait payant par - /plan</b>"""

    MANUELFILTER_TXT = """Aide: <b>Filtres</b>
- Le filtre est une fonctionnalité où les utilisateurs peuvent définir des réponses automatiques pour un mot clé particulier et je répondrai chaque fois qu'un mot clé est trouvé dans le message
<b>Remarque:</b>
1. Ce bot doit avoir des privilèges d'administrateur.
2. Seuls les administrateurs peuvent ajouter des filtres dans un chat.
3. Les boutons d'alerte ont une limite de 64 caractères.
Commandes et utilisation:
• /filter - <code>ajouter un filtre dans un chat</code>
• /filters - <code>lister tous les filtres d'un chat</code>
• /del - <code>supprimer un filtre spécifique dans un chat</code>
• /delall - <code>supprimer tous les filtres d'un chat (propriétaire du chat uniquement)</code>"""

    BUTTON_TXT = """Aide: <b>Boutons</b>
- Ce bot prend en charge les boutons URL et les boutons d'alerte en ligne.
<b>Remarque:</b>
1. Telegram ne vous permettra pas d'envoyer des boutons sans contenu, le contenu est donc obligatoire.
2. Ce bot prend en charge les boutons avec n'importe quel type de média Telegram.
3. Les boutons doivent être correctement analysés au format markdown
<b>Boutons URL:</b>
<code>[Texte du bouton](buttonurl:https://t.me/vjupdates2/3)</code>
<b>Boutons d'alerte:</b>
<code>[Texte du bouton](buttonalert:Ceci est un message d'alerte)</code>"""

    AUTOFILTER_TXT = """Aide: <b>Filtre automatique</b>
<b>Remarque: Index de fichier</b>
1. Faites de moi l'administrateur de votre chaîne si elle est privée.
2. Assurez-vous que votre chaîne ne contient pas de camrips, de porno et de faux fichiers.
3. Transférez-moi le dernier message avec des citations. J'ajouterai tous les fichiers de cette chaîne à ma base de données.

<b>Remarque: AutoFiltre</b>
1. Ajoutez le bot en tant qu'administrateur à votre groupe.
2. Utilisez /connect et connectez votre groupe au bot.
3. Utilisez /settings dans les messages privés du bot et activez AutoFiltre dans le menu des paramètres."""


    CONNECTION_TXT = """Aide: <b>Connexions</b>
- Utilisé pour connecter le bot aux messages privés pour gérer les filtres
- Cela permet d'éviter le spam dans les groupes.
<b>Remarque:</b>
1. Seuls les administrateurs peuvent ajouter une connexion.
2. Envoyez <code>/connect</code> pour me connecter à vos messages privés
Commandes et utilisation:
• /connect  - <code>connecter un chat particulier à vos messages privés</code>
• /disconnect  - <code>se déconnecter d'un chat</code>
• /connections - <code>lister toutes vos connexions</code>"""


    EXTRAMOD_TXT = """Aide: Modules supplémentaires
<b>Remarque:</b>
 <b>✯ Maintenu par : <a href={}>Propriétaire</a></b>
  
 <b>✯ Rejoignez ici : <a href={}>Chaîne de mise à jour</a></b> 
  
 ./id - <code>obtenir l'ID d'un utilisateur spécifié.
 code> 
  
 ./info  - <code>obtenir des informations sur un utilisateur.</code> 
  
 ./song - Télécharger n'importe quelle chanson [<code>exemple /song chanson vaa vaathi</code>] 
  
 ./telegraph - <code>Générateur Telegraph envoyer une vidéo ou une photo de moins de 5 Mo, je donne un lien telegraph</code> 
  
 ./tts - <code>Cette commande utilise un convertisseur texte-parole</code> 
  
 ./video - Cette commande utilise n'importe quel téléchargement vidéo YouTube hd [<code>exemple /video https://youtu.be/exemple...</code>]

./font - Cette commande utilise un générateur de polices élégant et cool [<code>exemple /font salut</code>]"""


    ADMIN_TXT = """Aide: Modes Admin
<b>Remarque:</b>
Ce module ne fonctionne que pour mes administrateurs
Commandes et utilisation:
• /logs - <code>pour obtenir les erreurs récentes</code>
• /stats - <code>pour obtenir l'état des fichiers dans la base de données. [Cette commande peut être utilisée par n'importe qui]</code>
• /delete - <code>pour supprimer un fichier spécifique de la base de données.</code>
• /users - <code>pour obtenir la liste de mes utilisateurs et leurs ID.</code>
• /chats - <code>pour obtenir la liste de mes chats et leurs ID</code>
• /leave  - <code>pour quitter un chat.</code>
• /disable  -  <code>pour désactiver un chat.</code>
• /ban  - <code>pour bannir un utilisateur.</code>
• /unban  - <code>pour débannir un utilisateur.</code>
• /channel - <code>pour obtenir la liste de tous les canaux connectés</code>
• /broadcast - <code>pour diffuser un message à tous les utilisateurs</code>
• /grp_broadcast - <code>Pour diffuser un message à tous les groupes connectés.</code>
• /gfilter - <code>pour ajouter des filtres globaux</code>
• /gfilters - <code>pour afficher la liste de tous les filtres globaux</code>
• /delg - <code>pour supprimer un filtre global spécifique</code>
• /request - <code>Pour envoyer une requête de film/série aux administrateurs du bot. Ne fonctionne que sur le groupe de support. [Cette commande peut être utilisée par n'importe qui]</code>
• /delallg - <code>Pour supprimer tous les filtres globaux de la base de données du bot.</code>
• /deletefiles - <code>Pour supprimer les fichiers CamRip et PreDVD de la base de données du bot.</code>"""

    SEC_STATUS_TXT = """<b>★ Utilisateurs totaux: <code>{}</code>
★ Chats totaux: <code>{}</code>
★ Fichiers totaux: <code>{}</code>
★ Stockage utilisé: <code>{} Mo</code>
★ Stockage libre: <code>{} Mo</code></b>"""
    
    STATUS_TXT = """<b>Nombre total de fichiers de toutes les bases de données : <code>{}</code>

BASE DE DONNÉES UTILISATEURS :-
★ Nombre total d’utilisateurs : <code>{}</code>
★ Nombre total de discussions : <code>{}</code>

PREMIÈRE BASE DE DONNÉES DE FICHIERS :-
★ Nombre total de fichiers : <code>{}</code>
★ Stockage utilisé : <code>{} Mo</code>
★ Stockage libre : <code>{} Mo</code>

DEUXIÈME BASE DE DONNÉES DE FICHIERS :-
★ Nombre total de fichiers : <code>{}</code>
★ Stockage utilisé : <code>{} Mo</code>
★ Stockage libre : <code>{} Mo</code>

AUTRE BASE DE DONNÉES :-
★ Stockage utilisé : <code>{} Mo</code>
★ Stockage libre : <code>{} Mo</code></b>"""
    
    LOG_TEXT_G = """#NouveauGroupe
Groupe = {}(<code>{}</code>)
Membres totaux = <code>{}</code>
Ajouté par - {}"""

    LOG_TEXT_P = """#NouvelUtilisateur
ID - <code>{}</code>
Nom - {}"""

    ALRT_TXT = """Salut {},
ce n'est pas votre requête de film,
demandez la vôtre..."""

    OLD_ALRT_TXT = """Hé {},
vous utilisez un de mes anciens messages,
veuillez renvoyer la requête."""

    CUDNT_FND = """Je n'ai rien trouvé en rapport avec {}
Vouliez-vous dire l'un de ceux-ci?"""

    I_CUDNT = """<b>Désolé, aucun fichier n'a été trouvé pour votre requête {} 😕

Vérifiez votre orthographe dans Google et réessayez 😃

Format de requête de film 👇

Exemple : Uncharted ou Uncharted 2022 ou Uncharted En

Format de requête de série 👇

Exemple : Loki S01 ou Loki S01E04 ou Lucifer S03E24

🚯 N’utilisez pas ➠ ':(!,./)</b>"""


    I_CUD_NT = """Je n'ai trouvé aucun film en rapport avec {}.
Veuillez vérifier l'orthographe sur Google ou IMDb..."""

    MVE_NT_FND = """Film introuvable dans la base de données..."""

    TOP_ALRT_MSG = """Recherche du film dans la base de données..."""

    MELCOW_ENG = """<b>Salut {} 😍, et bienvenue dans le groupe {} ❤️</b>"""

    SHORTLINK_INFO = """

🫵 Sélectionnez votre langue et gagnez de l'argent 💰"""

    REQINFO = """
⚠ INFORMATIONS ⚠

Après 5 minutes, ce message sera automatiquement supprimé

Si vous ne voyez pas le fichier film/série demandé, regardez la page suivante"""

    SELECT = """Sélectionnez votre langue, qualité, saison et épisode préférés"""

    SINFO = """
🫣 Pour le film, rejoignez d'abord puis cliquez sur le bouton Réessayer 😅"""

    NORSLTS = """ 
★ #AucunRésultat ★

ID <b>: {}</b>

Nom <b>: {}</b>

Message <b>: {}</b>"""

    CAPTION = """<b>📂 Nom du fichier : {file_name}

<b>⚙️ Taille : {file_size}</b>""" 

    IMDB_TEMPLATE_TXT = """
<b>Requête: {qurey}

Données IMDb:

<b>🏷 Titre</b>: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Année: <a href={url}/releaseinfo>{year}</a>
🌟 Note: <a href={url}/ratings>{rating}</a> / 10 (basé sur {votes} évaluations d'utilisateurs.)
☀️ Langues : <code>{languages}</code>
📀 Durée d'exécution: {runtime} Minutes
📆 Informations sur la sortie : {release_date}
🎛 Pays : <code>{countries}</code>


⏰Résultat affiché en: {remaining_seconds} <i>secondes</i> 🔥

Demandé par : {message.from_user.mention}</b>"""
    ALL_FILTERS = """
<b>Salut {}, voici mes trois types de filtres.</b>"""
    GFILTER_TXT = """
<b>Bienvenue dans les filtres globaux. Les filtres globaux sont les filtres définis par les administrateurs du bot qui fonctionneront sur tous les groupes.</b>
    
Commandes disponibles :
• /gfilter - <code>Pour créer un filtre global.</code>
• /gfilters - <code>Pour afficher tous les filtres globaux.</code>
• /delg - <code>Pour supprimer un filtre global particulier.</code>
• /delallg - <code>pour supprimer tous les filtres globaux.</code>"""
    FILE_STORE_TXT = """
<b>Le stockage de fichiers est la fonctionnalité qui créera un lien partageable d’un ou plusieurs fichiers.</b>

Commandes disponibles :
• /batch - <code>Pour créer un lien par lot de plusieurs fichiers.</code>
• /link - <code>Pour créer un lien de stockage de fichier unique.</code>
• /pbatch - <code>Tout comme /batch, mais les fichiers seront envoyés avec des restrictions de transfert.</code>
• /plink - <code>Tout comme /link, mais le fichier sera envoyé avec une restriction de transfert.</code>"""
    SONG_TXT = """<b>module de téléchargement de chansons</b> 
      
 <b>module de téléchargement de chansons, pour ceux qui aiment la musique. vous pouvez utiliser cette fonctionnalité pour télécharger n'importe quelle chanson à une vitesse ultra rapide. fonctionne uniquement sur les bots et les groupes...</b> 
  
 <b>commandes</b> :<b> 𝄟⃝.  /song nom de la chanson</b></b>""" 
    YTDL_TXT = """<b>vous aide à télécharger des vidéos depuis youtube. 
  
 utilisation : vous pouvez télécharger n'importe quelle vidéo depuis youtube 
  
 comment utiliser : tapez - /video ou /mp4 
  
 exemple :<code>/mp4 https://youtu.be/exemple...</code></b>""" 
    TTS_TXT = """<b>module tts 🎤 : traduire du texte en parole 
  
 commandes et utilisation : /tts</b>""" 
    GTRANS_TXT = """<b>aide : traducteur google 
  
 cette commande vous aide à traduire un texte dans n'importe quelle langue de votre choix. cette commande fonctionne à la fois sur les messages privés et les groupes
  
 commandes et utilisation : /tr - pour traduire des textes dans une langue spécifique 
  
 remarque : lorsque vous utilisez /tr, vous devez spécifier le code de langue 
  
 exemple : /tr ml 
 • en = anglais 
 • ml = malayalam 
 • hi = hindi</b>""" 
    TELE_TXT = """<b>aide : telegraph faites ce que vous voulez avec le module telegra.ph ! 
  
 utilisation : /telegraph - envoyez-moi une image ou une vidéo de moins de (5 Mo) 
  
 remarque : 
 cette commande est disponible dans les groupes et les messages privés 
 cette commande peut être utilisée par tout le monde</b>""" 
    CORONA_TXT = """<b>aide : covid 
  
 cette commande vous aide à connaître les informations quotidiennes sur le covid 
  
 commandes et utilisation : 
  
 /covid - utilisez cette commande avec le nom de votre pays pour obtenir des informations sur le covid 
 exemple :<code>/covid Inde</code> 
  
 ⚠️ ce service a été arrêté 
  
 </b>""" 
    PROGRESS_BAR = """\n
╭━━━━❰ Le fichier est en cours de renommage... ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """
    ABOOK_TXT = """<b>aide : livre audio 
  
 vous pouvez convertir un fichier pdf en un fichier audio avec cette commande ✯ 
  
 commandes et utilisation : 
 /audiobook : répondez à cette commande sur n'importe quel pdf pour générer l'audio 
</b>""" 
    PINGS_TXT = """<b>test de ping : vous aide à connaître votre ping🪄 
  
 commandes : 
 • /alive - pour vérifier que vous êtes en vie. 
 • /help - Pour obtenir de l'aide. 
 • /ping - <b>pour obtenir votre ping. 
  
 utilisation : 
 • ces commandes peuvent être utilisées dans les messages privés et les groupes 
 • ces commandes peuvent être utilisées par tout le monde dans les groupes et les messages privés des bots 
 • partagez-nous pour plus de fonctionnalités 
  </b>""" 
    STICKER_TXT = """<b>vous pouvez utiliser ce module pour trouver n'importe quel ID d'autocollants. 
 • utilisation : pour obtenir un autocollant 
   
 ⭕ comment utiliser 
 /stickerid
 </b>""" 
    FONT_TXT= """<b>utilisation 
  
 vous pouvez utiliser ce module pour changer le style de police   
  
 commande : /font votre texte (facultatif) 
 ex :- /font bonjour 
  
 </b>""" 
    PURGE_TXT = """<b>purger 
      
 supprimer beaucoup de messages des groupes !  
      
  admin  
  
 ◉ /purge :- supprimer tous les messages du message auquel on a répondu, jusqu'au message actuel</b>""" 
    WHOIS_TXT = """<b>module whois 
  
 remarque :- donner les détails d'un utilisateur 
 /whois :- donner tous les détails d'un utilisateur 📑 
 </b>""" 
    JSON_TXT = """<b> 
 json :  
 le bot renvoie json pour tous les messages auxquels on a répondu avec /json 
  
 fonctionnalités : 
  
 modification de message json 
 prise en charge des messages privés 
 prise en charge des groupes 
  
 remarque : 
  
 tout le monde peut utiliser cette commande, en cas de spam, le bot vous bannira automatiquement du groupe.</b>""" 
    URLSHORT_TXT = """<b>aide : raccourcisseur d'URL 
  
 <i><b>Cette commande vous aide à raccourcir une URL</i></b> 
  
 commandes et utilisation : 
  
 /short : <b>utilisez cette commande avec votre lien pour obtenir des liens courts</b> 
 exemple :<code>/short https://youtu.be/exemple...</code> 
</b>""" 
    CARB_TXT = """<b>aide pour le carbone 
  
 le carbone est une fonctionnalité pour créer l'image comme indiqué en haut avec vos textes. 
 pour utiliser le module, envoyez simplement le texte et répondez-y avec la commande /carbon, le bot répondra avec l'image carbone 
</b>""" 
    GEN_PASS = """<b>Aide : Générateur de mots de passe 
  
 Il n’y a rien de plus à savoir. Envoyez-moi la limite de votre mot de passe. 
 - Je donnerai le mot de passe de cette limite. 
  
 Commandes et utilisation : 
 • /genpassword ou /genpw 20 
  
 REMARQUE : 
 • Seuls les chiffres sont autorisés 
 • Chiffres maximum autorisés jusqu’à 84  
 (Je ne peux pas générer de mots de passe au-dessus de la longueur 84) 
 • IMDʙ doit avoir des privilèges d’administrateur. 
 • Ces commandes fonctionnent à la fois sur les messages privés et les groupes. 
 • Ces commandes peuvent être utilisées par n’importe quel membre du groupe.</b>""" 
    SHARE_TXT = """<b>Obtenez l’URL de partage de votre texte. 
  
 - ex :- /share
  
 </b>""" 
    PIN_TXT = """<b>module d’épinglage 
 épingler un message... 
  
 toutes les commandes liées à l’épinglage peuvent être trouvées ici : 
  
 📌commandes et utilisation📌 
  
 /pin :- pour épingler le message sur vos chats 
 /unpin :- pour désépingler le message actuellement épinglé</b>"""
    RESTART_TXT = """
<b>Bot redémarré !

📅 Date : <code>{}</code>
⏰ Heure : <code>{}</code>
🌐 Fuseau horaire : <code>Asie/Kolkata</code>
🛠️ État de la construction : <code>v2.7.1 [ Stable ]</code></b>"""
    LOGO = """
████████╗███████╗███████╗██╗  ██╗    ╔██        ██╗       ██╗
╚═ ██╔══╝██╔════╝██╔════╝██║  ██║     ║██      ██║        ██║
   ██║    █████╗  ██║      ███████║      ║██    ██║         ██║
   ██║    ██╔══╝  ██║      ██╔══██║       ║██  ██║  ╔██     ██║
   ██║    ███████╗███████╗██║  ██║        ║████║   ║████████║
   ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═╝        ╚════╝   ╚════════╝"""

    TAMIL_INFO = """
Salut <a href='tg://settings'>mon ami</a> 


 Vous pouvez désormais gagner de l'argent sur Telegram.

 Pour gagner de l'argent via Telegram, vous devez avoir 1 groupe.
 Si vous avez un groupe, vous pouvez gagner de l'argent en ajoutant notre bot à votre groupe.

 Plus vous avez de membres dans votre groupe, plus vos revenus seront élevés.

 Comment et quoi faire

 Étape 1 : Ajoutez ce bot VJ-FILTER-BOT en tant qu'administrateur de votre groupe

 Étape 2 : Ajoutez votre site Web et votre API

 Exemple : /shortlink xtz.in 4b392f8eb6ad711fbe58

 Ajouter une vidéo

 👇 Comment ajouter 👇

 Exemple : /set_tutorial lien vidéo

De plus, un tutoriel vidéo sera ajouté à votre groupe..."""

    ENGLISH_INFO = """ # Déjà traduit plus haut
"""

    TELUGU_INFO = """ # Déjà traduit plus haut
"""

    HINDI_INFO = """
Salut <a href='tg://settings'>mon ami</a> 


 Maintenant, vous pouvez également gagner de l'argent sur Telegram.

 Vous devez avoir 1 groupe pour gagner de l'argent via Telegram.
 Si vous avez un groupe, vous pouvez gagner de l'argent en ajoutant notre bot à votre groupe.


 Plus vous avez de membres dans votre groupe, plus vos revenus seront élevés.


 Comment et quoi faire

 Étape 1 : Définissez ce bot VJ-FILTER-BOT comme administrateur de votre groupe

 Étape 2 : Ajoutez votre site Web et votre API

 Exemple : /shortlink xtz.in 4b392f8eb6ad711fbe58

 Ajouter une vidéo

 👇 Comment ajouter 👇

 Exemple : /set_tutorial lien de la vidéo

De plus, votre équipe formera également une collection de vidéos..."""


    MALAYALAM_INFO = """
Salut <a href='tg://settings'>mon ami</a> 


 Maintenant, vous pouvez également gagner de l'argent sur Telegram.

 Vous devez avoir 1 groupe pour gagner de l'argent via Telegram.
 Si vous avez un groupe, vous pouvez gagner de l'argent en ajoutant notre bot à votre groupe.


 Plus vous avez de membres dans votre groupe, plus vos revenus seront élevés.


 Comment et quoi faire

 Étape 1 : Ajoutez ce bot VJ-FILTER-BOT en tant qu'administrateur de votre groupe.

 Étape 2 : Ajoutez votre site Web et votre API

 Exemple : /shortlink xtz.in 4b392f8eb6ad711fbe58

 Ajouter une vidéo


 👇 Comment ajouter 👇


 Exemple : /set_tutorial lien de la vidéo

Aussi, votre équipe formera également la collection de vidéos..."""

    URTU_INFO = """ # Déjà traduit plus haut.
"""

    GUJARATI_INFO = """ # Déjà traduit plus haut.
"""


    KANNADA_INFO = """
Salut <a href='tg://settings'>mon ami</a> 


 Maintenant, vous pouvez également gagner de l'argent sur Telegram.


 Vous devez avoir 1 groupe pour gagner de l'argent via Telegram.
 Si vous avez un groupe, vous pouvez gagner de l'argent en ajoutant notre bot à votre groupe.


 Plus vous avez de membres dans votre groupe, plus vos revenus seront élevés.


 Comment et quoi faire


 Étape 1 : Gérez ce bot VJ-FILTER-BOT dans votre groupe


 Étape 2 : Ajoutez votre site Web et votre API


 Exemple : /shortlink xtz.in 4b392f8eb6ad711fbe58


 Ajouter une vidéo


 👇 Comment ajouter 👇


 Exemple : /set_tutorial lien vidéo

De plus, votre équipe formera une collection de vidéos..."""


    BANGLADESH_INFO = """
Salut <a href='tg://settings'>mon ami</a> 


 Vous pouvez désormais gagner de l'argent sur Telegram.


 Vous devez avoir 1 groupe pour gagner de l'argent via Telegram.
 Si vous avez un groupe, vous pouvez gagner de l'argent en ajoutant notre bot à votre groupe.


 Plus vous avez de membres dans votre groupe, plus vos revenus seront élevés.


 Comment et quoi faire


 Étape 1 : Gérez ce bot VJ-FILTER-BOT dans votre groupe


 Étape 2 : Ajoutez votre site Web et votre API


 Exemple : /shortlink xtz.in 4b392f8eb6ad711fbe58


 Ajouter une vidéo


 👇 Comment ajouter 👇


 Exemple : /set_tutorial lien vidéo


De plus, votre équipe formera une collection de vidéos..."""

    RENAME_TXT = """
🌌 <b><u>COMMENT DÉFINIR UNE MINIATURE</u></b>

•> /set_thumb - envoyez n'importe quelle image pour définir automatiquement la miniature.
•> /del_thumb utilisez cette commande et supprimez votre ancienne miniature.
•> /view_thumb utilisez cette commande pour afficher votre miniature actuelle.

📑 <b><u>COMMENT DÉFINIR UNE LÉGENDE PERSONNALISÉE</u></b>

•> /set_caption - définir une légende personnalisée
•> /see_caption - voir votre légende personnalisée
•> /del_caption - supprimer la légende personnalisée

Exemple :- /set_caption 📕 Nom du fichier : {filename}
💾 Taille : {filesize}
⏰ Durée : {duration}

✏️ <b><u>COMMENT RENOMMER UN FICHIER</u></b>

•> /rename - envoyez n'importe quel fichier et cliquez sur l'option renommer et tapez le nouveau nom du fichier et \np sélectionnez ensuite [ document, vidéo, audio ]👈 choisissez ceci.
"""

    STREAM_TXT = """<b><u>COMMENT OBTENIR UN LIEN DE DIFFUSION ET DE TÉLÉCHARGEMENT :</u>

/stream - obtenir un lien diffusable et téléchargeable de n'importe quel fichier</b>"""


# N'enlevez pas le crédit @VJ_Botz
# Abonnez-vous à la chaîne YouTube pour un bot incroyable @Tech_VJ
# Posez vos questions sur Telegram @KingVJ01
