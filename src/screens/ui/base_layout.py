import streamlit as st


def style_background_home():
    st.markdown("""
<style>
[data-testid="stMain"] [data-testid="stColumn"] {
    background: var(--secondary-background-color);
    color: var(--text-color);
    border-radius: 1.25rem;
    padding: clamp(1rem, 4vw, 2rem);
}
</style>
""", unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
<style>
.block-container { padding-top: 3rem; }
.creator-credit {
    margin: 2.5rem auto 0;
    padding: 1.1rem .75rem;
    border-top: 1px solid currentColor;
    max-width: 28rem;
    color: var(--text-color);
    font-size: .95rem;
    text-align: center;
}
.creator-credit strong { font-weight: 700; }
</style>
""", unsafe_allow_html=True)
