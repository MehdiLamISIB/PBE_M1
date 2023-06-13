import wikipediaapi

wiki_wiki=wikipediaapi.Wikipedia('fr')
choix_planete='Mars_(planète)' # _(planètes)
choix_generique='exoplanètes' # rien
choix_programm='Python_(langage)' # _(language) --> pour language de programmation
choix_pays='Belgique'
choix_
page_py = wiki_wiki.page('exoplanètes')
if(page_py.exists()):
    full_page=page_py.summary.split('.')
    if(len(full_page[0])<100):
        print('.'.join(full_page[0:2]))
    else:
        print(full_page[0])
else:
    print("Cette recherche est inexsistante sur WIkipédia")



####CODE A REUTILISER
def WikiDefineThis(toDefine):
    WIKI_WIKI=wikipediaapi.Wikipedia('fr')
    page_wiki=WIKI_WIKI.page(toDefine)
    if(page_wiki.exists()):
        full_page = page_wiki.summary.split('.')
        if (len(full_page[0]) < 100):
            return "Selon Wikipédia, "+ '.'.join(full_page[0:2])
        else:
            return "Selon Wikipédia, "+full_page[0]
    else:
        return "Je n'ai pas de définition pour ce que vous demandez"

