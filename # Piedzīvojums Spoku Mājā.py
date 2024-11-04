# Piedzīvojums Spoku Mājā
import random

# Inicializē mainīgos
inventory = []
player_alive = True
key_found = False
available_rooms = ["foajē", "virtuve", "dzīvojamā istaba", "pagrabs"]

def start_game():
    global player_alive
    while player_alive:
        entrance()

def entrance():
    print("Tu atrodies spoku mājas ieejā. Vai vēlies iet 'iekšā', bēgt 'prom', 'inventārs' vai 'karte'?")
    choice = ""
    while choice not in ["iekšā", "prom", "inventārs", "karte"]:
        choice = input(">>> ").lower()
        if choice == "iekšā":
            foyer()
        elif choice == "prom":
            print("Tu izbēdzi droši. Spēle beigusies!")
            end_game()
        elif choice == "inventārs":
            check_inventory()
        elif choice == "karte":
            show_map()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def foyer():
    print("Tu ieej foajē. Ir tumšs, bet redzi durvis uz 'virtuve', 'dzīvojamā istaba', un 'pagrabs'.")
    choice = ""
    while choice not in ["virtuve", "dzīvojamā istaba", "pagrabs", "inventārs", "karte", "bēgt"]:
        choice = input(">>> ").lower()
        if choice == "virtuve":
            kitchen()
        elif choice == "dzīvojamā istaba":
            living_room()
        elif choice == "pagrabs":
            if "atslēga" in inventory:  # Pārbauda, vai spēlētājam ir atslēga
                basement()
            else:
                print("Durvis uz pagrabu ir aizslēgtas. Tev nepieciešama atslēga.")
                foyer()
        elif choice == "inventārs":
            check_inventory()
            foyer()  # Izsauc pašreizējo funkciju atkārtoti
        elif choice == "karte":
            show_map()
            foyer()  # Izsauc pašreizējo funkciju atkārtoti
        elif choice == "bēgt":
            print("Tu izbēdzi droši. Spēle beigusies!")
            end_game()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")
            foyer()

def kitchen():
    global key_found
    print("Tu esi virtuvē. Tā ir biedējoša, un tu atrod rūsinātu nazi. Vai tu to 'ņem' vai atstāj 'aizvērtu'?")
    choice = ""
    while choice not in ["ņem", "aizvērtu"]:
        choice = input(">>> ").lower()
        if choice == "ņem":
            inventory.append("nazis")
            print("Tu paņēmi nazi.")
        
        # Nejauša spoka parādīšanās
        if random.choice([True, False]):
            print("Pēkšņi parādās spoks! Vai tu vēlies 'cīnīties' vai 'bēgt'?")
            action = input(">>> ").lower()
            if action == "cīnīties":
                if "nazis" in inventory:
                    print("Tu uzvarēji spoku ar nazi! Tu atgriezies foajē.")
                    foyer()
                else:
                    print("Tev nav ar ko aizstāvēties. Spēle beigusies.")
                    end_game()
            elif action == "bēgt":
                print("Tu aizbēdzi atpakaļ uz foajē.")
                foyer()
            else:
                print("Nepareiza izvēle.")
        else:
            print("Virtuvē viss ir mierīgi.")
        kitchen() 

def basement():
    print("Tu atrodi durvis uz pagrabu. Tās ir aizslēgtas. Ja tev būtu atslēga, tu varētu tās 'atvērt'.")
    choice = ""
    while choice not in ["atvērt"]:
        choice = input(">>> ").lower()
        
       
        if choice == "atvērt":
            if "atslēga" in inventory: 
                print("Tu esi nonācis pagrabā. Telpa ir tumša un mitra, un tās centrā atrodas altāris. Pie altāra ir galvaskausi, un daži izskatās, ka tiem ir vairāk nekā 1000 gadu. Uz altāra guļ senlaicīga rokassprādze.")
                
                pagrabs()
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")
def pagrabs():   
    print("Vai tu vēlatvērties 'uzvilkt' rokassprādzi vai 'bēgt' ano maja?")
    choice = ""
    while choice not in ["uzvilkt", "bēgt"]:
        choice = input(">>> ").lower()  
        if choice == "uzvilkt":
            print("Tu jūties labi, aizej ar rokassprādzi. Tiklīdz jūs aiziet, rokassprādze sāk mirdzēt. Kas zina, kas notika, bet jūs to vairs neredzēsit.")
            end_game()
        elif choice == "bēgt":
            print("Jūs nolemjat, ka tas ir dīvaini, jūs vienkārši sākat doties prom, kad aiz jums parādās spoks. Tu tikko pagriezies, domādams skriet, bet ieraugi savu ķermeni netālu no spoka, kurš skatās uz jaunu galvu savai kolekcijai.")
            end_game()    
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")

def living_room():
    global key_found
    print("Dzīvojamā istaba ir putekļaina un tajā ir dīvains spogulis. Vari apskatīt 'meklēt' istabā, vai iet 'atpakaļ' uz foajē.")
    choice = ""
    while choice not in ["spoguli", "meklēt", "atpakaļ", "inventārs", "karte"]:
        choice = input(">>> ").lower()
        
        if choice == "spoguli":
            print("Ha-ha-ha mēs visi nomirsim. 'nāc no pagraba'")
            
        
        elif choice == "meklēt":
            if not key_found and random.choice([True, False]):  # 50% iespēja atrast atslēgu
                print("Tu atradi atslēgu! Tagad vari doties uz pagrabu.")
                inventory.append("atslēga")
                key_found = True
                living_room()
            else:
                print("Tu neko neatradi. Istaba šķiet tukša.")
                living_room()
        
        elif choice == "atpakaļ":
            foyer()
        
        elif choice == "inventārs":
            check_inventory()
            living_room()  # Atgriež spēlētāju atpakaļ uz šo funkciju
        
        elif choice == "karte":
            show_map()
            living_room()  # Atgriež spēlētāju atpakaļ uz šo funkciju
        
        else:
            print("Nepareiza izvēle. Mēģini vēlreiz.")
    
    # Pievieno atslēgas atrašanas iespēju
    if not key_found and random.choice([True, False]):  # 50% iespēja atrast atslēgu
        print("Tu atradi atslēgu! Tagad vari doties uz pagrabu.")
        inventory.append("atslēga")
        key_found = True
        print("Tu vari atgriezties uz foajē vai doties uz pagrabu.")
    
    # Pievieno atslēgas atrašanas iespēju
    if not key_found and random.choice([True, False]):  # 50% iespēja atrast atslēgu
        print("Tu atradi atslēgu! Tagad vari doties uz pagrabu.")
        inventory.append("atslēga")
        key_found = True
        print("Tu vari atgriezties uz foajē vai doties uz pagrabu.")

def end_game():
    global player_alive
    player_alive = False
    print("Paldies, ka spēlēji Piedzīvojums Spoku Mājā!")

def check_inventory():
    if inventory:
        print("Tavs inventārs: " + ", ".join(inventory))
    else:
        print("Tavs inventārs ir tukšs.")

def show_map():
    print("Pieejamās istabas: " + ", ".join(available_rooms))

# Sāk spēli
print("Sveicināts Piedzīvojumā Spoku Mājā!")
start_game()