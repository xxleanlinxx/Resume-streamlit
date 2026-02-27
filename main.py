import re
import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
from descriptions import (
    WORK_NAME, TC_NAME, DESCRIPTION_a, DESCRIPTION_b,
    EMAIL, SOCIAL_MEDIA, PROJECTS, EDU, CAREER, SKILLS
)

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "resume_leanlinmy.pdf"

# --- Load Assets ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# ============================================================
# Page Config & Global CSS
# ============================================================
st.set_page_config(
    page_title=f"{WORK_NAME} — Resume",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="collapsed",
)

GLOBAL_CSS = """
<style>
/* ---------- Import Google Font ---------- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ---------- Base ---------- */
html, body, [class*="st-"] {
    font-family: 'Inter', sans-serif;
}

/* ---------- Hide sidebar completely for mobile-first ---------- */
section[data-testid="stSidebar"] {
    display: none;
}
button[data-testid="stSidebarCollapsedControl"] {
    display: none;
}

/* ---------- Metric Cards ---------- */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #667eea22, #764ba222);
    border: 1px solid rgba(118, 75, 162, 0.25);
    border-radius: 12px;
    padding: 16px 20px;
    transition: transform 0.2s, box-shadow 0.2s;
}
div[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(102, 126, 234, 0.2);
}
div[data-testid="stMetric"] label {
    color: #a0a0b0 !important;
    font-size: 0.8rem !important;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
div[data-testid="stMetric"] [data-testid="stMetricValue"] {
    font-weight: 700 !important;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* ---------- Expander Card ---------- */
div[data-testid="stExpander"] {
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    margin-bottom: 8px;
    transition: border-color 0.2s;
}
div[data-testid="stExpander"]:hover {
    border-color: rgba(102, 126, 234, 0.4);
}

/* ---------- Container (bordered) Card ---------- */
div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 14px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.15);
}

/* ---------- Tabs ---------- */
button[data-baseweb="tab"] {
    font-weight: 600 !important;
    letter-spacing: 0.3px;
}

/* ---------- Dialog ---------- */
div[data-testid="stDialog"] > div {
    border-radius: 16px;
}

/* ---------- Link-Button Style ---------- */
a[data-testid="baseLinkButton-secondary"] {
    border-radius: 8px !important;
    transition: transform 0.15s !important;
}
a[data-testid="baseLinkButton-secondary"]:hover {
    transform: scale(1.03);
}

/* ---------- Fade-in Animation ---------- */
@keyframes fadeSlideIn {
    from { opacity: 0; transform: translateY(12px); }
    to   { opacity: 1; transform: translateY(0); }
}
.stMainBlockContainer {
    animation: fadeSlideIn 0.45s ease-out;
}

/* ---------- Highlighter for key terms ---------- */
.hl {
    background: linear-gradient(120deg, #a8e6cf55 0%, #dcedc155 100%);
    padding: 1px 6px;
    border-radius: 4px;
    font-weight: 600;
}

/* ---------- Dark mode highlighter ---------- */
@media (prefers-color-scheme: dark) {
    .hl {
        background: linear-gradient(120deg, #2d6a4f55 0%, #40916c44 100%);
        color: #b7e4c7;
    }
}
</style>
"""
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# ============================================================
# Helper — Convert backtick `text` to highlighted <span>
# ============================================================
_BACKTICK_RE = re.compile(r"`([^`]+)`")

def highlight_text(md_text: str) -> str:
    """Replace `backtick` terms with <span class='hl'>bold</span> highlights."""
    return _BACKTICK_RE.sub(r"<span class='hl'>\1</span>", md_text)

def st_highlighted(md_text: str):
    """Render markdown with backtick terms converted to highlighted spans."""
    st.markdown(highlight_text(md_text), unsafe_allow_html=True)


# ============================================================
# Dialogs (defined before pages so they can be called)
# ============================================================
@st.dialog("🖼️ Certificate Viewer", width="large")
def show_certificate(title: str, image_path: str):
    """Display a certificate in a modal dialog."""
    st.markdown(f"#### {title}")
    st.image(image_path, use_container_width=True)
    if st.button("Close", use_container_width=True):
        st.rerun()


@st.dialog("📋 Project Details", width="large")
def show_project_detail(project: dict, has_repo: bool = False):
    """Display full project info inside a dialog."""
    st.markdown(project.get("name", ""))
    st_highlighted(project.get("info", ""))
    st.markdown("---")

    # Render access links
    if "access" in project:
        st.link_button(
            "🌐  Open Project URL",
            url=project["access"].strip(),
            use_container_width=True,
        )
    if "access_granger" in project:
        st.link_button(
            "1️⃣  Working Note: Granger Causality",
            url=project["access_granger"].strip(),
            use_container_width=True,
        )
    if "access_prophet" in project:
        st.link_button(
            "2️⃣  Working Note: Prophet Modeling",
            url=project["access_prophet"].strip(),
            use_container_width=True,
        )
    if has_repo and "repo" in project:
        st.link_button(
            "👾  GitHub Repository",
            url=project["repo"].strip(),
            use_container_width=True,
        )


# ============================================================
# Helper — Project Card
# ============================================================
def render_project_card(project: dict, has_repo: bool = False):
    """Render a bordered project card with a detail button."""
    with st.container(border=True):
        st.markdown(project.get("name", ""))
        # Show a short preview of info with highlights
        info_text = project.get("info", "")
        preview_lines = [l for l in info_text.strip().split("\n") if l.strip()][:2]
        st_highlighted("\n".join(preview_lines))

        col_l, col_r = st.columns([3, 1])
        with col_r:
            if st.button("📋 Details", key=f"btn_{id(project)}", use_container_width=True):
                show_project_detail(project, has_repo=has_repo)


# ============================================================
# Helper — Career Entry
# ============================================================
def render_career_entry(key: str, career: dict):
    """Render a single career entry as an expander."""
    title = career["title"].replace("#### ", "").replace("**", "")
    corp = career["corp_name"].replace("*", "")
    period = career["period"].replace("*", "")
    is_current = "Present" in period

    badge = " 🟢" if is_current else ""
    expander_label = f"**{title}**  —  {corp}{badge}  ·  {period}"

    with st.expander(expander_label, expanded=is_current):
        st_highlighted(career["info"])


# ============================================================
# Header — Name, Description & Download
# ============================================================
st.markdown(f"# {WORK_NAME}")
st.markdown(f"##### *{TC_NAME}*")

st.info(DESCRIPTION_a.strip(), icon="💡")

# --- Key Metrics ---
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Experience", "7+ Years")
with m2:
    st.metric("Analytics Initiatives", "10+")
with m3:
    st.metric("AI Training Attendees", "250+")

st.markdown("")

# --- Core Strengths ---
with st.container(border=True):
    st.markdown("#### ⚡ Core Strengths")
    st.markdown(DESCRIPTION_b)

# --- Download Button ---
st.download_button(
    label="⏬  Download Resume (.pdf)",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
    help="Click to download the resume as a PDF file.",
    use_container_width=True,
)

st.markdown("")

# ============================================================
# Main Navigation — option_menu (horizontal)
# ============================================================
with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About", "Skills", "Projects", "Contact"],
        icons=["person-circle", "tools", "bar-chart-steps", "telephone-plus-fill"],
        orientation="horizontal",
    )

# ------ About ------
if selected == "About":
    tab_career, tab_edu = st.tabs(["💼  Career Summary", "🎓  Education"])

    with tab_career:
        for key in ["coupang", "shopee", "ailabs", "eland"]:
            render_career_entry(key, CAREER[key])

    with tab_edu:
        with st.container(border=True):
            col_e1, col_e2 = st.columns([3, 1])
            with col_e1:
                st.markdown(f"{EDU['degree']}, {EDU['school']}")
            with col_e2:
                st.markdown(f"*{EDU['period']}*")
            st.markdown(EDU["info"])

# ------ Skills ------
elif selected == "Skills":
    tab_hard, tab_soft = st.tabs(["⚙️  Hard Skills", "🤝  Soft Skills"])

    with tab_hard:
        st_highlighted(SKILLS["hard"])

        st.markdown("---")
        st.markdown("#### 🪪 Certificates")
        col1_cer, col2_cer = st.columns(2)

        with col1_cer:
            with st.container(border=True):
                st.markdown(SKILLS["certificate_1"])
                st.image("assets/certificate_ml.png", use_container_width=True)
                if st.button("🔍 View Full Size", key="cert_ml", use_container_width=True):
                    show_certificate(
                        "Stanford Machine Learning Specialization",
                        "assets/certificate_ml.png",
                    )

        with col2_cer:
            with st.container(border=True):
                st.markdown(SKILLS["certificate_2"])
                st.image("assets/certificate_bi.png", use_container_width=True)
                if st.button("🔍 View Full Size", key="cert_bi", use_container_width=True):
                    show_certificate(
                        "Google Business Intelligence Specialization",
                        "assets/certificate_bi.png",
                    )

    with tab_soft:
        st.markdown(SKILLS["soft"])

# ------ Projects ------
elif selected == "Projects":
    tab_side, tab_work = st.tabs(["🚀  Side Projects", "🏢  Work Projects"])

    with tab_side:
        render_project_card(PROJECTS["side"]["ml"], has_repo=True)
        render_project_card(PROJECTS["side"]["app"], has_repo=True)
        render_project_card(PROJECTS["side"]["wal"], has_repo=True)

    with tab_work:
        render_project_card(PROJECTS["work"]["app"])
        render_project_card(PROJECTS["work"]["rfm"])
        render_project_card(PROJECTS["work"]["topline"])
        render_project_card(PROJECTS["work"]["dws"])
        render_project_card(PROJECTS["work"]["ls"])

# ------ Contact ------
elif selected == "Contact":
    st.markdown("Feel free to reach out through any of the channels below.")
    st.markdown("")

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.image("assets/gmail.png", width=48)
            st.markdown("##### Gmail")
            st.code(EMAIL, language=None)

    with col2:
        with st.container(border=True):
            st.image("assets/line.png", width=48)
            st.markdown("##### LINE ID")
            st.code(SOCIAL_MEDIA["Line ID"], language=None)

    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.image("assets/linkedin.png", width=48)
            st.markdown("##### LinkedIn")
            st.link_button(
                "🔗  Open LinkedIn Profile",
                url=SOCIAL_MEDIA["LinkedIn"],
                use_container_width=True,
            )

    with col4:
        with st.container(border=True):
            st.image("assets/github.png", width=48)
            st.markdown("##### GitHub")
            st.link_button(
                "🔗  Open GitHub Profile",
                url=SOCIAL_MEDIA["GitHub"],
                use_container_width=True,
            )
