import base64
from pathlib import Path

import streamlit as st

LOGO = Path(__file__).resolve().parents[3] / 'assets' / 'bit-mesra.jpg'


def masthead():
    role = st.session_state.get("login_type")
    section = {"teacher": "Teacher Portal", "student": "Student Portal"}.get(role, "Home")
    st.markdown(f"""
<div class="masthead"><img src="data:image/jpeg;base64,{base64.b64encode(LOGO.read_bytes()).decode()}" alt="Birla Institute of Technology, Mesra" width="52" height="52">
<strong>BIT Mesra Attendance AI</strong><span class="location">{section}</span></div>
""", unsafe_allow_html=True)


def header_dashboard():
    role = st.session_state.login_type
    st.title("Student Portal" if role == "student" else "Teacher Portal")
