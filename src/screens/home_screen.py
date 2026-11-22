import streamlit as st


def home_screen():
    st.markdown("""
<section class="landing">
    <p>Birla Institute of Technology, Mesra</p>
    <h1>BIT Mesra Attendance AI</h1>
    <div>Classroom attendance using face and voice recognition, reviewed by teachers before saving.</div>
</section>
""", unsafe_allow_html=True)
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
