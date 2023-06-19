COLOR_CLASSES="wb"

# Récupération du nom du client
def nomClient():
    with open("./output/nomClient.txt") as file:
        clName = file.read()
    return clName

# Récupération du fichier de ping
def pingResult():
    with open("./output/pinglist.txt") as file:
        pingString = file.read()
    return pingString

# Récupération du fichier de test de débit
def debitResult():
    with open("./output/debit.txt") as file:
        debitString = file.read()
    return debitString

# Récupération du fichier de résultat d'un netscan
def netscanResult():
    with open("./output/netscan.txt") as file:
        netscanString = file.read()
    return netscanString

# Récupération du fichier d'historique de ping
def pingHistory():
    with open("/home/theo/pinglist.txt") as file:
        pinghString = file.read()
    return pinghString

# Récupération de l'ip publique
def publicIPFile():
    with open("./output/publicip.txt") as file:
        publicIPString = file.read()
    return publicIPString