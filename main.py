import streamlit as st
import random

frases_foco = [
  "Um passo por vez.",
  "Disciplina vence motivação.",
  "Continue mesmo devagar.",
  "Keep going, even  when progress feels do today.",
  "Dream big, start small, act now."
  
]

frases_recomeço = [
  "Hoje pode ser um novo começo.",
  "Recomeço também é progresso.",
  "Você não ser perfeito.",
  "Don't stop until ypu'r proud.",
  "Keep showing up. Your future self will thank you."
  
]

frases_autoestima = [
  "Voçê não precisa  se comoarar.", 
  "Seu valor não depende da opnião dos outros.",
  "Você esta evoluindo no seu tempo.",
  "Ypu are enough exacly as you are.",
  "You deserve the life you're working for."
  
]

frases_estudos = [
  "Estudar um pouco todos os dias muda tudo.",
  "Voçê não precisa entender tudo de primeira.",
  "A pratica transforma confusão em clarez",
  "Never stop learning.",
  "Focus on progress , not perfection."
]
st.set_page_config(

  page_title="INNER NOTES",
  page_icon="✨",
  layout="centered"
)
st.title("✨INNER NOTES")
st.subheader("Pequenas frases para foco, autoestima e recomeços.")

st.write(
  "Escolha uma categoria abaixo e clique no botão para receber uma frase."
)

categoria = st.selectbox(
  "Escolha uma categoria :",
  ["Foco", "Recomeço", "Autoestima", "Estudos"]
  
)

if st.button("Gerar frase"):
  if categoria == "Foco":
    frase = random.choice(frases_foco)
  elif categoria == "Recomeço":
    frase = random.choice(frases_recomeco)
  elif categoria == "Autoestima":
    frase == random.choice(frases_autoestima)
  elif categoria == "Estudos":
    frase = random.choice(frases_estudos)

st.success(frase)

st.divider()

st.caption("Criado cpm Python e Streamlit.")
