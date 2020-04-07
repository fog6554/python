###############################################################################
# Pokračuj ve své první webové aplikaci z minula :-)
#
# Postupuj v následujících krocích:
#   0. Spusť si aplikaci z minula a ověř že stále funguje, pročti si zdrojový kód a ověř, že všemu rozumíš :-)
#   1. Proveď refaktoring kódu - přesuň hlavičku a patičku home stránky do samostatných souborů
#       - vytvoř nové subory header.tpl a footer.tpl
#       - home.tpl obsahuje komentáře, které naznačují členění stránky na hlavičku, hlavní tělo a patičku
#       - rozděl tyto sekce do jednotlivých souborů header.tpl, home.tpl, footer.tpl
#       - spusť aplikaci a zjisti co funguje a co nefunguje
#           - pošli Vítkovi do chatu co vše ti přestalo fungovat`
#       - pokud něco nefunguje zamysli se proč 
#   2. Sprav aplikaci do původního stavu
#       - podívej se do dokumentace jak složit původní stránku z více souborů
#           - https://bottlepy.org/docs/dev/stpl.html#template-functions
#       - použij funkci % include pro vložení hlavičky a patičky do šablony home.tpl
#       - zkontroluj jestli se podařilo opravit, všechny chyby
#   3. Vytvoř novou stránku na kterou přesuneme seznam vedoucích hráčů
#       - tato stráka bude přístupná na adrese http://localhost:8080/leaders
#       - na domovské stránce můžeme přidat nějaký zajímavý text
#       - vytvoř pro tuto stránku novou šablonu leaders.tpl
#       - můžeš se inspirovat u home stránky
#       - otestuj, že vše funguje
#   4. Vytvoř v hlavičce menu
#       - přidej do hlavičky (header.tpl) odkazy
#           - na domovskou stránku '/'
#           - stránku se seznamem vedoucích hráčů '/leaders'
#       - texty (labely) odkazů předej do šablony jako parametry (nechceme je mít v HTML šabloně!)
#           - podobně jako title, inspiruj se
#       - pro odkaz použij HTML tag <a>
#           - dokumentace viz https://www.w3schools.com/tags/tag_a.asp
#       - otestuj
#   5. Refactoring - předej popisky funkcím template jako slovník v jednom paramteru
#       - vytvoř slovník obsahující všechny popisky, např. pod názvem labels
#       - tento slovník předej jako paramter funkcím template takto: **labels
#           - ty dvě hvězdičky udělají to, že slovník rozloží do jednotlivých čárkou oddělených paramterů klíč=hodnota
#       - otestuj, že vše funguje
#   6. Lokalizace
#       - přidej do menu odkaz, který přepne všechny popisky do druhého jazyka a zpět
#       - vytvoř druhý slovník jako v bodu 5. se stejnými klíči a s hodnotami textů v druhém jazyku, např. v angličtině
#       - vytvoř nový endpoint, který v paramteru dostane příslušný jazyk
#           - nápověda @app.get('/lang/<lang_code>')
#       - podle jazyka vloží do proměnné labels slovník s příslušným jazykem
#       - a vykreslí domovskou obrazovku pomocí funkce template v novém jazyku
#       - Poznámka: v reálných webových aplikacích se lokalizace řeší,
#                   pomocí nástrojů příslušného frameworku pro knihovnu bottle je to např. modul bottle_utils.i18n
###############################################################################
from bottle import Bottle, run, template

players = ['Karel', 'Lojza', 'Vítek', 'Venca']

# 5. vytvoř slovník se všemi popsiky a ulož do proměnné labels
# 6. vytvoř slovníky pro jednotlivé jazyky a do proměnné labels ulož výchozí slovník

app = Bottle()

@app.get('/')
def home():
    # 4. předej funkci template příslušné parametry pro popisky odkazů
    # 5. předej funkci template místo jednotlivých parametrů celý slovník **labels
    return template('home.tpl', title = 'Hráčův Ráj', players = players)

# 3. vytvoř novou funkci leaders, která zobrazí novou stránku na endpointu '/leaders'
    # 4. předej funkci template příslušné parametry pro popisky odkazů
    # 5. předej funkci template místo jednotlivých parametrů celý slovník **labels

# 6. vytvoř nový endpoint '/lang/<lang_code>', který přepne jazyk a vykreslí domovskou obrazovku

run(app, host='localhost', port=8080)
