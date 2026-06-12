import streamlit as st
from datetime import datetime
import random
import qrcode
from io import BytesIO
import base64

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Nossa História em Rock",
    page_icon="🎸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CARREGAR CSS
# ============================================================
def load_css(path):
    with open(path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

# ============================================================
# ============== EDITE AQUI O CONTEÚDO DO CASAL ==============
# ============================================================

NOME_ELA = "Ana Luiza"
NOME_ELE = "Alex Cavalera"

# Data em que o casal começou a namorar (ano, mês, dia, hora, minuto)
DATA_INICIO = datetime(2025, 12, 21, 0, 0)

# URL pública do site (para o QR Code). Troque pela URL do Streamlit Cloud.
URL_SITE = "https://nossahistoriaemrock.streamlit.app"

# ----- NOSSA TURNÊ (linha do tempo / marcos) -----
TURNE = [
    {
        "data": "19 NOV 2025",
        "cidade": "FORTALEZA, BR",
        "titulo": "O Primeiro Encontro",
        "descricao": "A noite em que a banda foi formada. Tudo começou aqui.",
    },
    {
        "data": "20 DEZ 2026",
        "cidade": "LIMOEIRO DO NORTE, BR",
        "titulo": "O PEDIDO",
        "descricao": "O refrão que a gente nunca mais esqueceu.",
    },
    {
        "data": "20 MAR 2026",
        "cidade": "FORTALEZA",
        "titulo": "O Primeiro Show Juntos",
        "descricao": "A noite que ela roubou meu caminhão.",
    },
    {
        "data": "18 ABR 2026",
        "cidade": "ARENA CASTELÃO",
        "titulo": "A PROMESSA, ARMAS E AS ROSAS",
        "descricao": "Show do Guns N Roses com beijo sob a chuva de abril.",
    },
    {
        "data": "11 MAIO 2026",
        "cidade": "CANOA QUEBRADA",
        "titulo": "A Primeira Viagem",
        "descricao": "Nosso primeiro show fora de casa.",
    },
]

# ----- NOSSOS MOMENTOS (galeria de fotos / polaroids) -----
MOMENTOS = [
    {
        "foto": "assets/foto7.jpeg",
        "titulo": "Viagem",
        "descricao": "Som novo, lugar novo.",
    },
    {
        "foto": "assets/foto2.jpg",
        "titulo": "Aquele dia",
        "descricao": "Uma lembrança inesquecível.",
    },
    {
        "foto": "assets/foto1.jpg",
        "titulo": "Risadas",
        "descricao": "Os melhores bastidores são os nossos.",
    },
    {
        "foto": "assets/foto3.jpg",
        "titulo": "Viagem",
        "descricao": "Som novo, lugar novo.",
    },
    {
        "foto": "assets/foto4.jpeg",
        "titulo": "Hoje",
        "descricao": "E a turnê continua.",
    },
    {
        "foto": "assets/foto5.jpeg",
        "titulo": "Aquele dia",
        "descricao": "Uma lembrança inesquecível.",
    },
    {
        "foto": "assets/foto6.jpeg",
        "titulo": "Risadas",
        "descricao": "Os melhores bastidores são os nossos.",
    }

]

# ----- SETLIST (trilha sonora da história) -----
SETLIST = [
    {
        "ordem": 1,
        "titulo": "A música do nosso primeiro encontro",
        "artista": "Papa Roach",
        "spotify": "https://open.spotify.com/embed/track/5W8YXBz9MTIDyrpYaCg2Ky?si=00c6b09356c24dc9",
    },
    {
        "ordem": 2,
        "titulo": "Nossa primeira viagem",
        "artista": "RHCP",
        "spotify": "https://open.spotify.com/embed/track/1G391cbiT3v3Cywg8T7DM1?si=c3acddd71aad4828",
    },
    {
        "ordem": 3,
        "titulo": "Nossa música",
        "artista": "Hoobstank",
        "spotify": "https://open.spotify.com/embed/track/1CobuGL6ysSrfCE2tWcfFU?si=6213f6ff3261429f",
    },
    {
        "ordem": 4,
        "titulo": "Sempre ouvimos",
        "artista": "Pearl Jam",
        "spotify": "https://open.spotify.com/embed/track/5Xak5fmy089t0FYmh3VJiY?si=7f2f476fa39d474c",
    },


]

# ----- BACKSTAGE (curiosidades / lembranças especiais) -----
#BACKSTAGE_ITEMS = [
#    "🎸 A primeira mensagem que troquei com você foi sobre uma piada péssima.",
#    "🥁 Nosso primeiro filme juntos foi assistido três vezes seguidas.",
#    "🎤 Você canta errado a letra dessa música, e eu amo isso.",
#    "🔥 O apelido que só nós dois entendemos.",
#    "🎶 A primeira vez que dancei sem vergonha foi com você.",
#]

# ----- SURPRESAS (mensagens aleatórias) -----
SURPRESAS = [
    "Você é o solo de guitarra que eu não sabia que minha vida precisava. 🎸",
    "Cada dia com você é uma nova faixa no álbum da nossa história. 🎶",
    "Se nosso amor fosse uma música, seria um clássico que nunca sai de moda. 🔥",
    "Você é o encore que eu sempre peço. ❤️🤘",
    "Junto com você, até o silêncio tem ritmo.",
]

# ----- CARTA -----
CARTA_TEXTO = """Querida """+NOME_ELA+""",

Se a nossa história fosse um álbum, cada faixa contaria um pedaço
de tudo que vivemos juntos. Dos primeiros acordes desafinados às
turnês que ainda vamos fazer.

Obrigado(a) por ser meu palco, minha plateia e minha melhor canção.

Com todo o meu rock,
""" + NOME_ELE + """🤘 !!!"""

# ----- MENSAGEM FINAL -----
MENSAGEM_FINAL = "Você sempre será minha música favorita."

# ============================================================
# ============== FIM DA ÁREA DE EDIÇÃO ========================
# ============================================================


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def gerar_qrcode(url: str) -> str:
    """Gera QR Code em base64 a partir de uma URL."""
    qr = qrcode.QRCode(box_size=8, border=2)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#FF0000", back_color="#000000")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()


def calcular_tempo(inicio: datetime):
    agora = datetime.now()
    delta = agora - inicio

    total_dias = delta.days
    anos = total_dias // 365
    dias_restantes = total_dias % 365
    meses = dias_restantes // 30
    dias = dias_restantes % 30
    horas = delta.seconds // 3600

    return anos, meses, dias, horas


# ============================================================
# HERO
# ============================================================
# ============================================================
# HERO
# ============================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">🎸 Our Love Tour</div>
        <div class="hero-title">A TRILHA SONORA DAS NOSSAS VIDAS</div>
        <div class="hero-subtitle">
        A história da vida de Alex & Ana <br>
            Nossa história.<br>
            Nosso som.<br>
            Nosso rock.
        </div>
        <a href="#contador" class="start-button" style="margin-top: 2rem; z-index: 1;
           animation: heroFadeIn 1s ease-out 0.8s both;">🎸 COMEÇAR</a>
        <a href="#contador" class="hero-scroll">
            ROLE PARA COMEÇAR
            <span class="hero-scroll-arrow"></span>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# CONTADOR
# ============================================================
st.markdown('<div id="contador"></div>', unsafe_allow_html=True)
st.markdown(
    '<div class="section-title-wrap"><div class="section-title">Há quanto tempo somos uma banda</div></div>',
    unsafe_allow_html=True,
)

anos, meses, dias, horas = calcular_tempo(DATA_INICIO)

st.markdown(
    f"""
    <div class="counter-grid">
        <div class="counter-card">
            <div class="counter-number">{anos:02d}</div>
            <div class="counter-label">ANOS</div>
        </div>
        <div class="counter-card">
            <div class="counter-number">{meses:02d}</div>
            <div class="counter-label">MESES</div>
        </div>
        <div class="counter-card">
            <div class="counter-number">{dias:02d}</div>
            <div class="counter-label">DIAS</div>
        </div>
        <div class="counter-card">
            <div class="counter-number">{horas:02d}</div>
            <div class="counter-label">HORAS</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# NOSSA TURNÊ
# ============================================================
st.markdown(
    '<div class="section-title-wrap"><div class="section-title">Nossa Turnê</div></div>',
    unsafe_allow_html=True,
)

for parada in TURNE:
    st.markdown(
        f"""
        <div class="ticket">
            <div class="ticket-date">{parada['data']} · {parada['cidade']}</div>
            <div class="ticket-title">{parada['titulo']}</div>
            <div class="ticket-desc">{parada['descricao']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# NOSSOS MOMENTOS (GALERIA / POLAROIDS)
# ============================================================
st.markdown(
    '<div class="section-title-wrap"><div class="section-title">Nossos Momentos</div></div>',
    unsafe_allow_html=True,
)

rotacoes = [-4, 3, -2, 5, -5, 2]
cols = st.columns(2)

for i, momento in enumerate(MOMENTOS):
    rot = rotacoes[i % len(rotacoes)]
    with cols[i % 2]:
        try:
            with open(momento["foto"], "rb") as f:
                img_b64 = base64.b64encode(f.read()).decode()
            img_tag = f'<img src="data:image/jpeg;base64,{img_b64}">'
        except FileNotFoundError:
            img_tag = (
                '<div style="background:#333;height:220px;display:flex;'
                'align-items:center;justify-content:center;color:#888;'
                'font-family:Oswald;border-radius:2px;">Foto não encontrada</div>'
            )

        st.markdown(
            f"""
            <div class="polaroid" style="transform: rotate({rot}deg);">
                {img_tag}
                <div class="polaroid-caption">{momento['titulo']}</div>
                <div class="polaroid-desc">{momento['descricao']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# SETLIST
# ============================================================
st.markdown(
    '<div class="section-title-wrap"><div class="section-title">Setlist</div></div>',
    unsafe_allow_html=True,
)

for faixa in SETLIST:
    st.markdown(
        f"""
        <div class="track">
            <div class="track-number">{faixa['ordem']:02d}</div>
            <div class="track-info">
                <div class="track-title">{faixa['titulo']}</div>
                <div class="track-artist">{faixa['artista']}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if faixa.get("spotify"):
        st.markdown(
            f"""
            <iframe style="border-radius:12px; margin-bottom: 1rem;"
                src="{faixa['spotify']}"
                width="100%" height="80" frameBorder="0"
                allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media;
                fullscreen; picture-in-picture" loading="lazy">
            </iframe>
            """,
            unsafe_allow_html=True,
        )

# ============================================================
# BACKSTAGE
# ============================================================
#st.markdown(
#    '<div class="section-title-wrap"><div class="section-title">Backstage</div></div>',
#    unsafe_allow_html=True,
#)
#
#for item in BACKSTAGE_ITEMS:
#    st.markdown(f'<div class="backstage-box">{item}</div>', unsafe_allow_html=True)

# ----- BOTÃO SURPRESA -----
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🎁 SURPRESA", use_container_width=True):
        st.session_state["surpresa"] = random.choice(SURPRESAS)

if "surpresa" in st.session_state:
    st.markdown(
        f'<div class="surprise-box">{st.session_state["surpresa"]}</div>',
        unsafe_allow_html=True,
    )

# ============================================================
# CARTA
# ============================================================
st.markdown(
    '<div class="section-title-wrap"><div class="section-title">A Carta</div></div>',
    unsafe_allow_html=True,
)

st.markdown(f'<div class="letter">{CARTA_TEXTO}</div>', unsafe_allow_html=True)

# ============================================================
# MENSAGEM FINAL
# ============================================================
st.markdown(f'<div class="final-message">{MENSAGEM_FINAL}</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="final-message" style="font-size:1.8rem;">Long Live Love & Rock.</div>',
    unsafe_allow_html=True,
)

# ============================================================
# COMPARTILHAMENTO (QR CODE)
# ============================================================
st.markdown(
    '<div class="section-title-wrap"><div class="section-title">Compartilhe</div></div>',
    unsafe_allow_html=True,
)

qr_b64 = gerar_qrcode(URL_SITE)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="data:image/png;base64,{qr_b64}" width="220"
                 style="border: 3px solid #FF0000; border-radius: 8px;
                 box-shadow: 0 0 20px rgba(255,0,0,0.5);">
            <p style="font-family:'Oswald', sans-serif; color:#ccc; margin-top:0.8rem;">
                Aponte a câmera para reviver essa turnê
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    "<div style='text-align:center; color:#666; font-family:Oswald; "
    "margin-top:3rem; margin-bottom:1rem;'>🎸 Nossa História em Rock 🎸</div>",
    unsafe_allow_html=True,
)
