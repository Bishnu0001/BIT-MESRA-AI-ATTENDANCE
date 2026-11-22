from pathlib import Path

import streamlit as st

LOGO = Path(__file__).resolve().parents[3] / 'assets' / 'bit-mesra.jpg'


def masthead():
    role = st.session_state.get("login_type")
    section = {"teacher": "Teacher Portal", "student": "Student Portal"}.get(role, "Home")
    with st.container(horizontal=True, vertical_alignment="center", key="site_header"):
        st.image(str(LOGO), width=74)
        st.markdown(f"**BIT Mesra Attendance AI**  \n{section}")
    st.divider()


def header_dashboard():
    role = st.session_state.login_type
    st.title("Student Portal" if role == "student" else "Teacher Portal")
