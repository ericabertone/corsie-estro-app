import streamlit as st
import random

# Titolo dell'app
st.title("Distribuzione degli Allievi nelle Corsie")

# Lista dei capi corsia e degli allievi
capi_corsia = ["Bertone", "Pintaudi", "Porro", "Betty", "Ale", "Rosy"]
altri_allievi = ["Beppe", "Gianlu", "Aref", "Emiliano", "Adam", "Luca", "Marco", 
                 "Noemi", "Andrea", "Walter", "Davide", "Guido", "Gledi", "Matteo", "Paola"]

# Selezione dei presenti
st.header("Seleziona gli allievi presenti")
presenti_capi = st.multiselect("Capi corsia presenti:", capi_corsia, default=capi_corsia)
presenti_altri = st.multiselect("Altri allievi presenti:", altri_allievi, default=altri_allievi)

# Coppie obbligatorie e da evitare
st.header("Coppie di allievi")
coppie_obbligatorie = st.text_input("Specifica coppie obbligatorie (separate da virgole, es. Beppe-Noemi, Davide-Guido):")
coppie_da_evitare = st.text_input("Specifica coppie da evitare (separate da virgole, es. Beppe-Noemi, Davide-Guido):")

# Funzione per processare le coppie obbligatorie e da evitare
def process_coppie(coppie_str):
    coppie = []
    if coppie_str:
        coppie = [tuple(c.strip() for c in coppia.split("-")) for coppia in coppie_str.split(",")]
    return coppie

coppie_obbligatorie_list = process_coppie(coppie_obbligatorie)
coppie_da_evitare_list = process_coppie(coppie_da_evitare)

# Distribuzione casuale
def distribuisci_allievi(presenti_capi, presenti_altri, coppie_obbligatorie, coppie_da_evitare):
    # Controllo che ci siano esattamente 6 capi corsia
    if len(presenti_capi) > 6:
        st.error("Troppi capi corsia presenti!")
        return
    elif len(presenti_capi) < 6:
        st.warning("Mancano capi corsia, le corsie saranno assegnate agli altri allievi.")
    
    # Shuffle degli allievi presenti
    random.shuffle(presenti_capi)
    random.shuffle(presenti_altri)
    
    # Inizializzazione delle corsie
    corsie = {i: [] for i in range(1, 7)}
    
    # Assegna i capi corsia
    for i, capo in enumerate(presenti_capi):
        corsie[i + 1].append(capo)
    
    # Distribuzione degli altri allievi
    for i, allievo in enumerate(presenti_altri):
        corsie[(i % 6) + 1].append(allievo)
    
    # Verifica delle coppie obbligatorie e da evitare
    for coppia in coppie_obbligatorie:
        trovato = False
        for corsia in corsie.values():
            if coppia[0] in corsia and coppia[1] in corsia:
                trovato = True
                break
        if not trovato:
            st.warning(f"Coppia obbligatoria non soddisfatta: {coppia}")
    
    for coppia in coppie_da_evitare:
        for corsia in corsie.values():
            if coppia[0] in corsia and coppia[1] in corsia:
                st.warning(f"Coppia da evitare trovata nella stessa corsia: {coppia}")

    return corsie

# Bottone per la distribuzione
if st.button("Distribuisci gli allievi"):
    corsie = distribuisci_allievi(presenti_capi, presenti_altri, coppie_obbligatorie_list, coppie_da_evitare_list)
    
    if corsie:
        st.header("Distribuzione finale:")
        for corsia, allievi in corsie.items():
            st.write(f"Corsia {corsia}: {', '.join(allievi)}")

# Visualizzazione del dado (immagine simulata di un dado)
st.header("Simulazione dado")
if st.button("Lancia il dado"):
    dado_result = random.randint(1, 6)
    st.image(f"https://upload.wikimedia.org/wikipedia/commons/thumb/{dado_result}.svg", width=100)
    st.write(f"Risultato del dado: {dado_result}")
