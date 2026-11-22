from pathlib import Path

import streamlit as st


CAMPUS_PHOTO = Path(__file__).resolve().parents[2] / "assets" / "campus.jpg"


def home_screen():
    with st.container(key="campus_hero"):
        st.image(str(CAMPUS_PHOTO), width="stretch")
        st.markdown('<h1 class="campus-title">BIT Mesra Attendance AI</h1>', unsafe_allow_html=True)

    students, teachers = st.columns(2, gap="medium")
    for column, role, icon, description in (
        (students, "Student", "face", "Sign in with a photo, enroll in subjects and track your attendance."),
        (teachers, "Teacher", "co_present", "Manage subjects, capture classroom attendance and review each session."),
    ):
        with column, st.container(border=True, key=f"entry_{role.lower()}"):
            st.badge(f"{role} access", icon=f":material/{icon}:", color="blue")
            st.subheader(f"{role} Portal")
            st.write(description)
            st.divider()
            if st.button(f"Open {role} Portal", icon=":material/arrow_forward:", icon_position="right", type="primary"):
                st.session_state.login_type = role.lower()
                st.rerun()
