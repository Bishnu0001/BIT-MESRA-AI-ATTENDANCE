import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen 


from src.screens.components.header import LOGO, masthead
from src.screens.components.footer import creator_credit
from src.screens.ui.base_layout import style_base_layout


def main():
    st.set_page_config(
        page_title='Bit Mesra - Making Attendance faster using AI',
        page_icon=str(LOGO)
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    style_base_layout()
    masthead()
    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()
        
        case None:
            home_screen()

    creator_credit()


main()

