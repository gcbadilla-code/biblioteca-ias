import streamlit as st
import os
import base64

# --- 1. CONFIGURACIÓN ---
st.set_page_config(
    page_title="Portal IA - Pontificia Universidad Católica de Chile",
    layout="wide",
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# --- 2. FUNCIONES TÉCNICAS ---

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def get_img_tag(nombre_archivo, ancho=80):
    if os.path.exists(f"{nombre_archivo}.png"):
        ruta = f"{nombre_archivo}.png"
        ext = "png"
    elif os.path.exists(f"{nombre_archivo}.jpg"):
        ruta = f"{nombre_archivo}.jpg"
        ext = "jpg"
    else:
        return "" 
    
    base64_img = get_base64_of_bin_file(ruta)
    return f'<img src="data:image/{ext};base64,{base64_img}" width="{ancho}" style="margin-bottom:10px;">'

def tarjeta_html(imagen_nombre, titulo, descripcion, link_url, link_texto):
    img_html = get_img_tag(imagen_nombre, ancho=80)
    
    return f"""
    <div class="tarjeta-blanca hvr-grow">
        <div style="display: flex; align-items: flex-start; gap: 15px;">
            <div style="flex-shrink: 0;">{img_html}</div>
            <div>
                <h3 style="margin: 0 0 10px 0; color: #002469; font-size: 1.2rem;">{titulo}</h3>
                <p style="color: #444; font-size: 0.95rem; margin-bottom: 15px; line-height: 1.4;">{descripcion}</p>
                <a href="{link_url}" target="_blank" class="boton-link">{link_texto} ➝</a>
            </div>
        </div>
    </div>
    """

# --- 3. CSS (FIRMA MOVIMIENTO A ARRIBA A LA DERECHA) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Roboto', sans-serif; }

    /* OCULTAR MARCA DE STREAMLIT */
    footer {visibility: hidden;} 

    /* TARJETA BLANCA */
    .tarjeta-blanca {
        background-color: #ffffff !important;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
    }

    /* EFECTO HOVER */
    .hvr-grow { transition: all .2s ease-in-out; }
    .hvr-grow:hover { transform: scale(1.01); box-shadow: 0 8px 20px rgba(0,0,0,0.15); }

    /* BOTONES */
    .boton-link {
        display: inline-block;
        text-decoration: none;
        color: #009FE3;
        font-weight: 700;
        font-size: 14px;
    }
    .boton-link:hover { text-decoration: underline; }

    /* BARRA LATERAL */
    section[data-testid="stSidebar"] { background-color: #002469 !important; }
    section[data-testid="stSidebar"] * { color: white !important; }
    
    /* TITULOS */
    .titulo-seccion {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 10px 20px;
        border-radius: 8px;
        display: inline-block;
        color: #002469;
        font-weight: 700;
        margin-top: 30px;
        margin-bottom: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        border-left: 5px solid #002469;
    }

    /* --- TU MARCA DE AGUA (FIRMA) MOVIDA ARRIBA A LA DERECHA (POSICIÓN SEGURA) --- */
    .watermark {
        position: fixed;
        top: 15px; /* <--- ARRIBA */
        right: 15px; /* <--- DERECHA */
        background-color: rgba(255, 255, 255, 0.9);
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 12px;
        color: #555;
        border: 1px solid #ccc;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        z-index: 999999; 
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. FONDO ---
if os.path.exists("fondo.jpg") or os.path.exists("fondo.png"):
    nombre_fondo = "fondo.png" if os.path.exists("fondo.png") else "fondo.jpg"
    bg_b64 = get_base64_of_bin_file(nombre_fondo)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_b64}");
            background-size: cover;
            background-attachment: fixed;
        }}
        .main .block-container {{ background: transparent !important; }}
        </style>
        """,
        unsafe_allow_html=True
    )

# --- 5. NAVEGACIÓN ---
with st.sidebar:
    st.markdown(get_img_tag("logo", ancho=200), unsafe_allow_html=True)
    st.write("---")
    opcion = st.radio("Ir a:", ["Inicio", "Catálogo de Soluciones", "Soporte"])
    st.write("---")
    st.markdown("**Contacto:** Alonso Meneses\n\n📧 armenesesz@uc.cl")

# --- 6. CONTENIDO ---

if opcion == "Inicio":
    st.markdown(f"<div style='text-align:center;'>{get_img_tag('banner', ancho='100%')}</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tarjeta-blanca">
        <h2 style="color: #002469; margin-top:0;">Bienvenido/a a tu Centro de Comando Digital</h2>
        <p style="font-size: 16px; color: #333;">
            Esta plataforma centraliza y facilita el acceso a las herramientas de Inteligencia Artificial permitidas para la comunidad universitaria.
        </p>
        <hr style="margin: 20px 0; border-top: 1px solid #eee;">
        <p style="color: #002469; font-weight: bold;">👉 Para comenzar:</p>
        <ol style="color: #444;">
            <li>Dirígete al menú azul de la izquierda.</li>
            <li>Selecciona <strong>"Catálogo de Soluciones"</strong>.</li>
            <li>Elige la herramienta que necesites.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="tarjeta-blanca" style="text-align: center;">
            <div class="metrica-label">Herramientas</div>
            <div class="metrica-num">7 IAs</div>
            <div class="metrica-sub">Disponibles</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="tarjeta-blanca" style="text-align: center;">
            <div class="metrica-label">Acceso</div>
            <div class="metrica-num">Comunidad UC</div>
            <div class="metrica-sub">Gratuito</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="tarjeta-blanca" style="text-align: center;">
            <div class="metrica-label">Categorías</div>
            <div class="metrica-num">3 Áreas</div>
            <div class="metrica-sub">Texto, Visual, Datos</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tarjeta-blanca" style="border-left: 5px solid #ffc107;">
        <h4 style="color: #856404; margin-top:0;">⚠️ Seguridad de la Información</h4>
        <ul style="color: #856404; margin-bottom:0;">
            <li><strong>No ingreses datos confidenciales</strong> (RUT, fichas clínicas, datos bancarios).</li>
            <li><strong>Verifica siempre la información:</strong> Las IAs pueden cometer errores. Tú eres el responsable final.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif opcion == "Catálogo de Soluciones":
    
    st.markdown('<div class="tarjeta-blanca"><h1 style="margin:0; color:#002469;">Catálogo de Soluciones</h1><p>Explora las herramientas disponibles.</p></div>', unsafe_allow_html=True)

    st.markdown('<div class="titulo-seccion">Redacción y Oficina</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(tarjeta_html(
            "copilot", "Copilot", 
            "Experto en Office. Analiza Excel, crea fórmulas y redacta en Word de forma segura.", 
            "https://copilot.microsoft.com", "Abrir Copilot"
        ), unsafe_allow_html=True)
    with c2:
        st.markdown(tarjeta_html(
            "chatgpt", "ChatGPT", 
            "Motor de creatividad. Ideal para lluvias de ideas, borradores y traducciones rápidas.", 
            "https://chat.openai.com", "Abrir ChatGPT"
        ), unsafe_allow_html=True)
    with c3:
        st.markdown(tarjeta_html(
            "gemini", "Gemini", 
            "Lógica avanzada. Úsalo para razonamiento complejo y análisis de imágenes.", 
            "https://gemini.google.com", "Abrir Gemini"
        ), unsafe_allow_html=True)

    st.markdown('<div class="titulo-seccion">Diseño y Video</div>', unsafe_allow_html=True)
    c4, c5, c6 = st.columns(3)
    
    with c4:
        st.markdown(tarjeta_html(
            "remini", "Remini", 
            "Restauración fotográfica. Recupera la calidad de fotos antiguas o borrosas a HD.", 
            "https://remini.ai", "Abrir Remini"
        ), unsafe_allow_html=True)
    with c5:
        st.markdown(tarjeta_html(
            "gamma", "Gamma", 
            "Presentaciones automáticas. Crea PPTs completos solo escribiendo el título.", 
            "https://gamma.app", "Abrir Gamma"
        ), unsafe_allow_html=True)
    with c6:
        st.markdown(tarjeta_html(
            "heygen", "HeyGen", 
            "Videos con avatares. Crea comunicados con personajes virtuales que hablan tu texto.", 
            "https://www.heygen.com", "Abrir HeyGen"
        ), unsafe_allow_html=True)

    st.markdown('<div class="titulo-seccion">Datos</div>', unsafe_allow_html=True)
    c7, c8 = st.columns([1, 2])
    
    with c7:
        st.markdown(tarjeta_html(
            "julius", "Julius AI", 
            "Analista de datos. Sube tu Excel y pídele gráficos y tendencias sin usar fórmulas.", 
            "https://julius.ai", "Abrir Julius"
        ), unsafe_allow_html=True)

elif opcion == "Soporte":
    st.markdown('<div class="titulo-seccion">Centro de Ayuda</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tarjeta-blanca">
        <h4 style="color:#002469; margin-top:0;">👤 Contacto Oficial</h4>
        <p><strong>Alonso Meneses</strong><br>Coordinador del Proyecto</p>
        <p>📧 <a href="mailto:armenesesz@uc.cl" style="color:#009FE3; font-weight:bold;">armenesesz@uc.cl</a></p>
    </div>
    """, unsafe_allow_html=True)

# --- TU FIRMA (PROTEGIDA Y VISIBLE) ---
st.markdown("""
    <div class="watermark">
        Desarrollado por <strong>Genesis Badilla</strong>
    </div>
""", unsafe_allow_html=True)