import streamlit as st

from src.screens.ui.base_layout import campus_photo


def home_screen():
    st.html(f"""
        <section class="campus-hero" aria-labelledby="campus-title">
            <img src="{campus_photo("campus-evening.jpg")}" alt="BIT Mesra campus at dusk">
            <h1 class="campus-title" id="campus-title">BIT Mesra<br>Attendance AI</h1>
        </section>
    """)

    students, teachers = st.columns(2, gap="medium")
    for column, role, icon, description in (
        (students, "Student", "school", "Sign in, enroll in subjects and check your attendance."),
        (teachers, "Teacher", "co_present", "Manage subjects, take attendance and review class records."),
    ):
        with column, st.container(border=True, key=f"entry_{role.lower()}"):
            st.subheader(f"{role} Portal")
            st.write(description)
            if st.button(
                f"Open {role} Portal",
                icon=f":material/{icon}:",
                type="primary",
                width="stretch",
            ):
                st.session_state.login_type = role.lower()
                st.rerun()
