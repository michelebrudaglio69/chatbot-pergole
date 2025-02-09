import streamlit as st
import cv2
import numpy as np
import requests
from PIL import Image
import io

st.title("Chatbot Configuratore di Pergole")
st.write("Compila il form per ricevere un progetto personalizzato per la tua pergola.")

# Form per raccogliere informazioni dell'utente
with st.form(key='configuratore_pergole'):
    nome = st.text_input("Nome")
    cognome = st.text_input("Cognome")
    telefono = st.text_input("Numero di telefono")
    email = st.text_input("Email")
    citta = st.text_input("Città")
    
    pergola_type = st.selectbox("Tipologia di pergola", ["Tetto in vetro", "Lamelle orientabili", "Telo retrattile"])
    pergola_width = st.slider("Larghezza dello spazio (m)", 2, 10, 4)
    pergola_depth = st.slider("Profondità dello spazio (m)", 2, 10, 3)
    chiusura_completa = st.radio("Vuoi una pergola chiusa completamente?", ["Sì", "No, solo tetto"])
    installazione_luogo = st.selectbox("Dove verrà installata?", ["Giardino", "Balcone", "Terrazza", "Attività commerciale"])
    uploaded_file = st.file_uploader("Carica una foto dello spazio con misure", type=["jpg", "png", "jpeg"])
    
    submit_button = st.form_submit_button(label="Invia Richiesta")
    
    if submit_button:
        st.success("Grazie! La tua richiesta è stata inviata con successo. Ti contatteremo al più presto!")
