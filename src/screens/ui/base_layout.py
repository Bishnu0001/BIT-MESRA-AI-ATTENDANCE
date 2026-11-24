from base64 import b64encode
from functools import lru_cache
from pathlib import Path

import streamlit as st


ASSETS = Path(__file__).resolve().parents[3] / "assets"
STYLESHEET = Path(__file__).with_name("attendance.css")


@lru_cache(maxsize=2)
def campus_photo(filename):
    photo = b64encode((ASSETS / filename).read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{photo}"


def style_portal_background():
    st.markdown(
        f'<style>.stApp {{ --campus-photo: url("{campus_photo("campus.jpg")}"); }}</style>',
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(f"<style>{STYLESHEET.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)
