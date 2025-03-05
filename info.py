# Ne supprimez pas le crédit @VJ_Botz
# Abonnez-vous à la chaîne YouTube pour des bots incroyables @Tech_VJ
# Posez vos questions sur Telegram @KingVJ01


import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')

# Informations du bot
SESSION = environ.get('SESSION', 'TechVJBot')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Image(s) pour le message de démarrage. Vous pouvez en ajouter plusieurs en les séparant par un espace.
PICS = (environ.get('PICS', 'https://graph.org/file/ce1723991756e48c35aa1.jpg')).split()

# Administrateurs & utilisateurs
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()] # Pour plusieurs ID, séparez-les par un espace.
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]  # Pour plusieurs ID, séparez-les par un espace.
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Ce canal est utilisé pour enregistrer les utilisateurs qui démarrent le bot. Même chose pour les groupes.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))

# Ce canal est utilisé pour stocker automatiquement les fichiers téléchargés.
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]  # Pour plusieurs ID, séparez-les par un espace.

# auth_channel signifie le canal d'abonnement forcé.
# Si REQUEST_TO_JOIN_MODE est activé, l'abonnement forcé fonctionne comme une demande d'adhésion.
REQUEST_TO_JOIN_MODE = bool(environ.get('REQUEST_TO_JOIN_MODE', False)) # Vrai ou Faux
TRY_AGAIN_BTN = bool(environ.get('TRY_AGAIN_BTN', False)) # Vrai ou Faux (Ce bouton "Réessayer" fonctionne uniquement pour l'abonnement forcé en mode demande d'adhésion)

# Canal d'abonnement forcé
auth_channel = environ.get('AUTH_CHANNEL', '') # ID du canal d'abonnement forcé, sinon laissez vide
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# Ce canal est utilisé lorsqu'un utilisateur demande un fichier avec une commande ou un hashtag comme - /request ou #request
reqst_channel = environ.get('REQST_CHANNEL', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None

# Ce canal est utilisé pour les demandes d'indexation
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

# ID du groupe de support du bot. Le bot ne fournira pas de fichiers dans ce groupe.
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# Ce canal est utilisé pour la commande /batch afin de stocker des fichiers.
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]  # Pour plusieurs ID, séparez-les par un espace.

# Ce canal est utilisé pour supprimer un fichier indexé. Envoyez un fichier ici pour le supprimer de la base de données.
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]  # Pour plusieurs ID, séparez-les par un espace.

# Informations MongoDB
DATABASE_URI = environ.get('DATABASE_URI', "")   # Si MULTIPLE_DATABASE est désactivé, remplissez uniquement cette URL.
DATABASE_NAME = environ.get('DATABASE_NAME', "techvjclonefilterbot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'vjcollection')

MULTIPLE_DATABASE = bool(environ.get('MULTIPLE_DATABASE', False)) # Vrai ou Faux

# Si MULTIPLE_DATABASE est activé, remplissez ces trois bases de données.
O_DB_URI = environ.get('O_DB_URI', "")   # Base de données pour stocker d'autres données.
F_DB_URI = environ.get('F_DB_URI', "")   # Base de données pour stocker les fichiers.
S_DB_URI = environ.get('S_DB_URI', "")   # Base de secours pour les fichiers si la première est pleine.

# Paramètres Premium et Parrainage
PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True)) # Vrai ou Faux

# Si PREMIUM_AND_REFERAL_MODE est activé, remplissez ces variables :
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '20')) # Nombre de parrainages requis
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1mois') # Durée du premium (ex: 1 semaine, 1 mois)
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/ce1723991756e48c35aa1.jpg') # URL du code de paiement.
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '<b>- PLANS DISPONIBLES - \n\n- 30 Rs - 1 SEMAINE\n- 50 Rs - 1 MOIS\n- 120 Rs - 3 MOIS\n- 220 Rs - 6 MOIS\n\n🎁 AVANTAGES PREMIUM 🎁\n\n○ Pas besoin de vérification\n○ Pas besoin d’ouvrir de lien\n○ Accès direct aux fichiers\n○ Expérience sans publicité\n○ Téléchargement haute vitesse\n○ Streaming multi-lecteur\n○ Accès illimité aux films et séries\n○ Support complet\n○ Les demandes sont traitées sous 1h si disponibles\n\n✨ UPI ID - <code>demo@okxyz</code>\n\nCliquez pour vérifier votre abonnement /myplan\n\n💢 Envoyez une capture d’écran après le paiement\n\n‼️ Attendez un peu après l’envoi de la capture d’écran pour être ajouté au premium</b>')

# Informations sur la duplication de bot
CLONE_MODE = bool(environ.get('CLONE_MODE', False)) # Vrai ou Faux
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', "") # Obligatoire si CLONE_MODE est activé
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', '') # Nom d'utilisateur du canal public (sans @)

# Liens
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/vj_bot_disscussion')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/vj_botz')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'vj_bot_disscussion') # Nom d'utilisateur sans https:// ou @
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/kingvj01')

# Vrai ou Faux
AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))
STREAM_MODE = bool(environ.get('STREAM_MODE', True)) # Active ou désactive le mode streaming
RENAME_MODE = bool(environ.get('RENAME_MODE', False)) # Permet de renommer les fichiers ou non
AUTO_APPROVE_MODE = bool(environ.get('AUTO_APPROVE_MODE', False)) # Approuve automatiquement les nouvelles demandes d'adhésion

# Réactions pour la commande de démarrage
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] # Liste d'émojis pris en charge par Telegram.

# Ne supprimez pas le crédit @VJ_Botz
# Abonnez-vous à la chaîne YouTube @Tech_VJ
# Posez vos questions sur Telegram @KingVJ01
