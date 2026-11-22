import streamlit as st


def masthead():
    role = st.session_state.get("login_type")
    section = {"teacher": "Teacher Portal", "student": "Student Portal"}.get(role, "Home")
    st.markdown(f"""
<div class="masthead"><span class="brand-mark">BIT</span>
<strong>Mesra Attendance AI</strong><span class="location">{section}</span></div>
""", unsafe_allow_html=True)


def header_dashboard():
    role = st.session_state.login_type
    st.title("Student Portal" if role == "student" else "Teacher Portal")
