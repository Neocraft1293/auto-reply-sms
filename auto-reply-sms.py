import subprocess
import json
import time

# Définir le message automatique avec des sauts de ligne
automatic_response_message = (
    "Ceci est un message automatique. Pour des raisons de sécurité, je ne communique plus via SMS.\n\n"
    "Vous pouvez me contacter sur Signal avec le même numéro de téléphone : https://signal.org/fr/ (si vous préférez la simplicité).\n"
    "ou sur Element (Matrix) avec l'identifiant @neocraft1293:matrix.org.\n"
    "https://element.io/"
)

# Définir les préfixes des numéros autorisés
allowed_prefixes = ["+337", "+336", "07", "06"]

def is_allowed_number(number):
    # Vérifie si le numéro commence par l'un des préfixes autorisés
    return any(number.startswith(prefix) for prefix in allowed_prefixes)

def get_sms():
    # Exécute la commande termux pour obtenir les SMS
    result = subprocess.run(['termux-sms-list'], stdout=subprocess.PIPE)
    
    # Parse le résultat en JSON
    sms_list = json.loads(result.stdout.decode('utf-8'))
    
    return sms_list

def get_last_sent_message():
    # Exécute la commande termux pour obtenir le dernier message envoyé
    result = subprocess.run(['termux-sms-list', '-d', 'sent', '--limit', '1', '--columns', 'body,number'], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

def send_response(number):
    # Obtient le dernier message envoyé
    last_sent_message = get_last_sent_message()

    # Vérifie si le dernier message envoyé n'est pas identique au message automatique et au message actuel
    if last_sent_message != automatic_response_message and last_sent_message != automatic_response_message:
        # Envoie une réponse automatique
        subprocess.run(['termux-sms-send', '-n', number, automatic_response_message])

def main():
    while True:
        # Charge l'état précédent depuis un fichier (ou initialise une liste vide si c'est la première exécution)
        try:
            with open('previous_sms_state.json', 'r') as file:
                previous_sms_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            previous_sms_list = []

        # Obtient la liste actuelle des SMS
        current_sms_list = get_sms()
        
        # Filtrer les nouveaux messages entrants autorisés
        new_incoming_messages = [sms for sms in current_sms_list if sms not in previous_sms_list
                                 and sms['type'] == 'inbox'
                                 and is_allowed_number(sms['number'])]

        # Affiche et répond aux nouveaux messages entrants autorisés
        for sms in new_incoming_messages:
            print(f"New incoming message from: {sms['number']}\nMessage: {sms['body']}\n")

            # Vérifie si le message entrant est identique à la réponse automatique
            if sms['body'] != automatic_response_message:
                # Envoie une réponse automatique uniquement si le dernier message envoyé n'est pas identique au message actuel
                send_response(sms['number'])

        # Enregistre la liste actuelle comme état précédent pour la prochaine itération
        with open('previous_sms_state.json', 'w') as file:
            json.dump(current_sms_list, file, indent=2)

        # Pause de 5 secondes
        time.sleep(5)

if __name__ == "__main__":
    main()
