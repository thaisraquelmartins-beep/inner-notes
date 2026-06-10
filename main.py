import streamlit as st
import random

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Great+Vibes&family=Libre+Baskerville:wght@400;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at top left, rgba(255, 240, 245, 0.85), transparent 35%),
        linear-gradient(135deg, #f8efe2 0%, #ead7c0 45%, #d8bfa3 100%);
    color: #3b2f2f;
}

.block-container {
    max-width: 780px;
    padding-top: 60px;
}

.title {
    font-family: 'Great Vibes', cursive;
    font-size: 78px;
    text-align: center;
    color: #7a3e3e;
    margin-bottom: 0px;
    text-shadow: 1px 1px 2px rgba(255,255,255,0.6);
}

.subtitle {
    font-family: 'Cormorant Garamond', serif;
    text-align: center;
    font-size: 28px;
    font-weight: 600;
    color: #5c4033;
    margin-bottom: 18px;
}

.description {
    font-family: 'Libre Baskerville', serif;
    text-align: center;
    color: #6b4f4f;
    font-size: 15px;
    margin-bottom: 35px;
}

.vintage-card {
    background: rgba(255, 248, 235, 0.88);
    padding: 42px 36px;
    border-radius: 18px;
    border: 1px solid #c9a86a;
    box-shadow: 0 18px 45px rgba(79, 49, 35, 0.18);
    text-align: center;
    margin-top: 28px;
}

.vintage-card h3 {
    font-family: 'Cormorant Garamond', serif;
    font-size: 34px;
    font-weight: 600;
    color: #4b2e2e;
    line-height: 1.45;
}

.divider {
    text-align: center;
    color: #9b6b43;
    font-size: 22px;
    margin: 25px 0;
}

.stSelectbox label {
    font-family: 'Libre Baskerville', serif;
    color: #4b2e2e;
    font-size: 15px;
}

.stButton > button {
    background: linear-gradient(90deg, #7a3e3e, #b08968);
    color: #fffaf0;
    border: 1px solid #c9a86a;
    border-radius: 30px;
    padding: 12px 28px;
    font-family: 'Libre Baskerville', serif;
    font-weight: 700;
    font-size: 15px;
    width: 100%;
    transition: 0.3s;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #b08968, #7a3e3e);
    transform: scale(1.01);
}

.footer {
    font-family: 'Cormorant Garamond', serif;
    text-align: center;
    color: #6b4f4f;
    font-size: 16px;
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

st.markdown('<div class="title">Inner Notes</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">pequenas cartas para a alma</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Escolha uma categoria e receba uma frase como se fosse escrita em uma carta antiga.</div>', unsafe_allow_html=True)
st.markdown('<div class="divider">❦</div>', unsafe_allow_html=True)


categoria = st.selectbox(
  "Escolha uma categoria :",
  ["Foco", "Recomeço", "Autoestima", "Estudos"]
  
)

frase = ""

if st.button("Gerar frases"):
  if categoria == "Foco":
    frase = random.choice(frases_foco)
  elif categoria == "Recomeço":
    frase = random.choice(frases_recomeco)
  elif categoria == "Autoestima":
    frase = random.choice(frases_autoestima)
  elif categoria == "Estudos":
    frase = random.choice(frases_estudos)

st.markdown(f"""
<div class="vintage-card">
    <h3>“{frase}”</h3>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown('<div class="footer">Criado com Python e Streamlit · Inner Notes by Thais Raquel</div>', unsafe_allow_html=True)

)
