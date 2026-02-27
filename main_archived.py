import streamlit as st
from streamlit_option_menu import option_menu
from pathlib import Path
from descriptions import WORK_NAME, TC_NAME, DESCRIPTION_a, DESCRIPTION_b, EMAIL, SOCIAL_MEDIA, PROJECTS, EDU, CAREER, SKILLS
from print_txt import txt

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "assets" / "resume_leanlinmy.pdf"

# --- Load Assets ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- Top Header ---
st.set_page_config(layout = "centered")

st.title(f'''***{WORK_NAME}***''')
st.markdown(f'''##### ***{TC_NAME}***''')
st.warning(DESCRIPTION_a, icon = "💡")
st.success(DESCRIPTION_b, icon = "⚡")

st.download_button(
    label = "  ⏬ **Download Resume** (*.pdf*)  ",
    data = PDFbyte,
    file_name = resume_file.name,
    mime = "application/octet-stream",
    help = "Click to download the resume as a PDF file."
)

# --- Format Layout ---
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Skills', 'Projects', 'Contact'],
        icons = ['person-circle', 'tools', 'bar-chart-steps', 'telephone-plus-fill'],
        orientation = 'horizontal'
    )

if selected == 'About':
    tab_a1, tab_a2 = st.tabs(['Career Summary',
                              'Education'])
    with tab_a1:

        txt(f"{CAREER['coupang']['title']}, {CAREER['coupang']['corp_name']}", f"{CAREER['coupang']['period']}")
        st.markdown(CAREER['coupang']['info'])

        st.divider()

        txt(f"{CAREER['shopee']['title']}, {CAREER['shopee']['corp_name']}", f"{CAREER['shopee']['period']}")
        st.markdown(CAREER['shopee']['info'])

        st.divider()

        txt(f"{CAREER['ailabs']['title']}, {CAREER['ailabs']['corp_name']}", f"{CAREER['ailabs']['period']}")
        st.markdown(CAREER['ailabs']['info'])

        st.divider()

        txt(f"{CAREER['eland']['title']}, {CAREER['eland']['corp_name']}", f"{CAREER['eland']['period']}")
        st.markdown(CAREER['eland']['info'])

    with tab_a2:

        txt(f"{EDU['degree']}, {EDU['school']}", f"{EDU['period']}")
        st.markdown(EDU['info'])

if selected == 'Skills':
    tab_s1, tab_s2 = st.tabs(['Hard Skill', 
                              'Soft Skill'])
    with tab_s1:
        st.markdown(SKILLS['hard'])
        st.markdown('''
        #### Certificate 🪪
        ''')
        col1_cer, col2_cer = st.columns(2)
        
        with col1_cer:
            st.markdown(SKILLS['certificate_1'])
            st.image("assets/certificate_ml.png")
        
        with col2_cer:
            st.markdown(SKILLS['certificate_2'])
            st.image("assets/certificate_bi.png")
        
    with tab_s2:
        st.markdown(SKILLS['soft'])

if selected == 'Projects':
    tab_p1, tab_p2 = st.tabs(['Side Projects',
                              'Work Projects'])
    with tab_p1:
        st.markdown(PROJECTS['side']['ml']['name'])
        st.markdown(PROJECTS['side']['ml']['info'])
        st.markdown(
            f'''
            <div style="background-color: #292929; padding: 10px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <ul style="list-style: none; padding-left: 0; margin-top: 10px;">
                    <li style="margin-bottom: 5px;">
                        <a href="{PROJECTS['side']['ml']['access']}" target="_blank" style="color: #9FC5E8; text-decoration: none; font-weight: bold;">
                            🌐 Shared URL of this Project
                        </a>
                    </li>
                    <li>
                        <a href="{PROJECTS['side']['ml']['repo']}" target="_blank" style="color: #D9D2E9; text-decoration: none; font-weight: bold;">
                            👾 GitHub Repo
                        </a>
                    </li>
                </ul>
            </div>
            ''',
            unsafe_allow_html = True
        )

        st.divider()
        
        st.markdown(PROJECTS['side']['app']['name'])
        st.markdown(PROJECTS['side']['app']['info'])
        st.markdown(
            f'''
            <div style="background-color: #292929; padding: 10px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <ul style="list-style: none; padding-left: 0; margin-top: 10px;">
                    <li style="margin-bottom: 5px;">
                        <a href="{PROJECTS['side']['app']['access']}" target="_blank" style="color: #9FC5E8; text-decoration: none; font-weight: bold;">
                            🌐 Shared URL of this Project
                        </a>
                    </li>
                    <li>
                        <a href="{PROJECTS['side']['app']['repo']}" target="_blank" style="color: #D9D2E9; text-decoration: none; font-weight: bold;">
                            👾 GitHub Repo
                        </a>
                    </li>
                </ul>
            </div>
            ''',
            unsafe_allow_html = True
        )

        st.divider()

        st.markdown(PROJECTS['side']['wal']['name'])
        st.markdown(PROJECTS['side']['wal']['info'])
        st.markdown(
            f'''
            <div style="background-color: #292929; padding: 10px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <ul style="list-style: none; padding-left: 0; margin-top: 10px;">
                    <li style="margin-bottom: 5px;">
                        <a href="{PROJECTS['side']['wal']['access']}" target="_blank" style="color: #9FC5E8; text-decoration: none; font-weight: bold;">
                            🌐 Shared URL of this Project
                        </a>
                    </li>
                    <li>
                        <a href="{PROJECTS['side']['wal']['repo']}" target="_blank" style="color: #D9D2E9; text-decoration: none; font-weight: bold;">
                            👾 GitHub Repo
                        </a>
                    </li>
                </ul>
            </div>
            ''',
            unsafe_allow_html = True
        )

    with tab_p2:

        st.markdown(PROJECTS['work']['app']['name'])
        st.markdown(PROJECTS['work']['app']['info'])
        st.markdown(
            f'''
            <div style="background-color: #292929; padding: 10px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <ul style="list-style: none; padding-left: 0; margin-top: 10px;">
                    <li style="margin-bottom: 5px;">
                        <a href="{PROJECTS['work']['app']['access']}" target="_blank" style="color: #9FC5E8; text-decoration: none; font-weight: bold;">
                            🌐 Shared URL of this App
                        </a>
                    </li>
                </ul>
            </div>
            ''',
            unsafe_allow_html = True
        )

        st.divider()

        st.markdown(PROJECTS['work']['rfm']['name'])
        st.markdown(PROJECTS['work']['rfm']['info'])
        st.markdown(
            f'''
            <div style="background-color: #292929; padding: 10px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <ul style="list-style: none; padding-left: 0; margin-top: 10px;">
                    <li style="margin-bottom: 5px;">
                        <a href="{PROJECTS['work']['rfm']['access']}" target="_blank" style="color: #9FC5E8; text-decoration: none; font-weight: bold;">
                            🌐 Shared URL of this Project
                        </a>
                    </li>
                </ul>
            </div>
            ''',
            unsafe_allow_html = True
        )

        st.divider()

        st.markdown(PROJECTS['work']['topline']['name'])
        st.markdown(PROJECTS['work']['topline']['info'])
        st.markdown(
            f'''
            <div style="background-color: #292929; padding: 10px; border-radius: 12px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);">
                <ul style="list-style: none; padding-left: 0; margin-top: 10px;">
                    <li style="margin-bottom: 5px;">
                        <a href="{PROJECTS['work']['topline']['access_granger']}" target="_blank" style="color: #9FC5E8; text-decoration: none; font-weight: bold;">
                            1️⃣ Shared URL of the Working Note : Granger Causality Test
                        </a>
                    </li>
                    <li style="margin-bottom: 5px;">
                        <a href="{PROJECTS['work']['topline']['access_prophet']}" target="_blank" style="color: #9FC5E8; text-decoration: none; font-weight: bold;">
                            2️⃣ Shared URL of the Working Note : Prophet Modeling
                        </a>
                    </li>
                </ul>
            </div>
            ''',
            unsafe_allow_html = True
        )

        st.divider()

        st.markdown(PROJECTS['work']['dws']['name'])
        st.markdown(PROJECTS['work']['dws']['info'])
        
        st.divider()

        st.markdown(PROJECTS['work']['ls']['name'])
        st.markdown(PROJECTS['work']['ls']['info'])

if selected == 'Contact':
    col1, col2, col3= st.columns([1,0.1,1])
    with col1:
        st.image('assets/gmail.png', width = 60)
        st.markdown(
            f'''
            <div style="
                background-color: #eea2ad; 
                padding: 20px 25px; 
                border-radius: 8px; 
                color: #d51e3e; 
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
                <h5 style="margin: 0;"><b>Gmail</b></h5>
                <p style="margin: 5px 0 0 0;">
                    {EMAIL}
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    with col3:
        st.image('assets/line.png', width = 60)
        st.markdown(
            f'''
            <div style="
                background-color: #b7ded2; 
                padding: 20px 25px; 
                border-radius: 8px; 
                color: #209b38; 
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
                <h5 style="margin: 0;"><b>LINE id</b></h5>
                <p style="margin: 5px 0 0 0;">
                    {SOCIAL_MEDIA['Line ID']}
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    st.divider()
    col3, col4, col5 = st.columns([1,0.1,1])
    with col3:
        st.image('assets/linkedin.png', width = 60)
        st.markdown(
            f'''
            <div style="
                background-color: #b3cde0; 
                padding: 20px 25px; 
                border-radius: 8px; 
                color: #2972b6; 
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
                <h5 style="margin: 0;"><b>LinkedIn</b></h5>
                <p style="margin: 5px 0 0 0;">
                    <a href="{SOCIAL_MEDIA['LinkedIn']}" target="_blank" style="color: #0000EE; text-decoration: none;">
                        {SOCIAL_MEDIA['LinkedIn']}
                    </a>
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )
    with col5:
        st.image('assets/github.png', width = 60)
        st.markdown(
            f'''
            <div style="
                background-color: #dfdfde; 
                padding: 20px 25px; 
                border-radius: 8px; 
                color: #4d4d4d; 
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);">
                <h5 style="margin: 0;"><b>GitHub</b></h5>
                <p style="margin: 5px 0 0 0;">
                    <a href="{SOCIAL_MEDIA['GitHub']}" target="_blank" style="color: #0000EE; text-decoration: none;">
                        {SOCIAL_MEDIA['GitHub']}
                    </a>
                </p>
            </div>
            ''',
            unsafe_allow_html=True
        )
