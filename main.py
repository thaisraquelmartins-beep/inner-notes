import streamlit as st
import random

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=VT323&display=swap');

.stApp {
    background: #050505;
    color: #ffffff;
    font-family: 'VT323', monospace;
}

.block-container {
    max-width: 850px;
    padding-top: 55px;
}

.title {
    font-family: 'Press Start 2P', cursive;
    font-size: 34px;
    text-align: center;
    color: #ffcc00;
    text-shadow: 4px 4px 0px #ff006e;
    margin-bottom: 25px;
}

.subtitle {
    font-family: 'VT323', monospace;
    text-align: center;
    font-size: 34px;
    color: #00f5ff;
    margin-bottom: 12px;
}

.description {
    font-family: 'VT323', monospace;
    text-align: center;
    color: #ffffff;
    font-size: 24px;
    margin-bottom: 35px;
}

.divider {
    text-align: center;
    font-size: 32px;
    color: #ffcc00;
    margin: 25px 0;
}

.arcade-card {
    background: #111111;
    padding: 35px;
    border: 4px solid #ffcc00;
    box-shadow: 0 0 20px #00f5ff, 0 0 35px #ff006e;
    text-align: center;
    margin-top: 30px;
    border-radius: 8px;
}

.arcade-card h3 {
    font-family: 'VT323', monospace;
    font-size: 36px;
    color: #ffffff;
    line-height: 1.4;
}

.stSelectbox label {
    font-family: 'Press Start 2P', cursive;
    color: #ffcc00;
    font-size: 12px;
}

.stButton > button {
    background: #ffcc00;
    color: #050505;
    border: 4px solid #ffffff;
    border-radius: 6px;
    padding: 14px 28px;
    font-family: 'Press Start 2P', cursive;
    font-size: 12px;
    width: 100%;
    box-shadow: 5px 5px 0px #ff006e;
}

.stButton > button:hover {
    background: #00f5ff;
    color: #050505;
    border: 4px solid #ffcc00;
    transform: translateY(-2px);
}

.footer {
    font-family: 'VT323', monospace;
    text-align: center;
    color: #00f5ff;
    font-size: 22px;
    margin-top: 35px;
}
</style>
""", unsafe_allow_html=True)

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
  "Você não precisa ser perfeito.",
  "Don't stop until ypu'r proud.",
  "Keep showing up. Your future self will thank you."
  
]

frases_autoestima = [
  "Voçê não precisa se comparar.", 
  "Seu valor não depende da opnião dos outros.",
  "Você esta evoluindo no seu tempo.",
  "You are enough exacly as you are.",
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

st.markdown('<div class="title">INNER NOTES</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Press Start for Motivation</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Escolha sua fase e receba uma frase bônus.</div>', unsafe_allow_html=True)
st.markdown('<div class="divider">🟡 🟡 🟡 👾 🟡 🟡 🟡</div>', unsafe_allow_html=True)

categoria = st.selectbox(
  "Escolha uma categoria :",
  ["Foco", "Recomeço", "Autoestima", "Estudos"]
  
)

frase = ""

if st.button("Gerar frases"):
  if categoria == "Foco":
    frase = random.choice(frases_foco)
  elif categoria == "Recomeço":
    frase = random.choice(frases_recomeço)
  elif categoria == "Autoestima":
    frase = random.choice(frases_autoestima)
  elif categoria == "Estudos":
    frase = random.choice(frases_estudos)

st.markdown(f"""
<div class="arcade-card">
    <h3>▶ {frase}</h3>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown('<div class="footer">LEVEL 01 · Criado com Python + Streamlit · by Thais Raquel</div>', unsafe_allow_html=True)
