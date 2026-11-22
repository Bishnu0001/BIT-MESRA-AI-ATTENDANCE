import streamlit as st


def style_base_layout():
    st.markdown("""
<style>
.block-container {max-width:68rem; padding:3.5rem clamp(1rem,4vw,3rem) 2rem;}
.masthead {display:flex;align-items:center;gap:.75rem;border-bottom:1px solid #cbd4e4;padding:.8rem 0 1.25rem;margin-bottom:1rem;}
.brand-mark {background:#00236f;color:white;font: bold 1.05rem Georgia,serif;letter-spacing:.03em;padding:.65rem .55rem;border-radius:.5rem;}
.masthead strong {font-size:1.12rem;}
.location {margin-left:auto;font-weight:600;font-size:.9rem;border-bottom:2px solid #5277cd;padding:.35rem 0;}
.st-key-campus_hero {
    position: relative;
    overflow: hidden;
    border-radius: 1rem;
    margin-bottom: 1rem;
}
.st-key-campus_hero [data-testid="stImage"] img {
    width: 100%;
    height: clamp(18rem, 38vw, 29rem);
    object-fit: cover;
    object-position: center 48%;
    display: block;
}
.st-key-campus_hero [data-testid="stVerticalBlock"] { gap: 0; }
.st-key-campus_hero h1.campus-title {
    position: absolute;
    inset: auto 0 0;
    padding: 3.5rem clamp(1rem, 5vw, 3rem) 1.5rem;
    margin: 0;
    background: linear-gradient(transparent, rgba(8, 23, 40, .94));
    color: #fff;
    font-size: clamp(2rem, 5vw, 4rem);
    line-height: 1.08;
    letter-spacing: -.035em;
    text-shadow: 0 2px 10px rgba(8, 23, 40, .7);
}
.st-key-entry_teacher,.st-key-entry_student,.st-key-access_panel {background:var(--background-color);border:1px solid #cbd4e4!important;border-radius:1rem!important;padding:clamp(1.1rem,3vw,2rem)!important;box-shadow:0 6px 22px #172f5810;}
.st-key-access_panel {max-width:48rem;margin-inline:auto;}
[data-testid="stMain"] h2,[data-testid="stMain"] h3 {letter-spacing:-.025em;}
.creator-credit {margin:3rem auto 0;border-top:1px solid #cbd4e4;padding:1.15rem;text-align:center;font-size:.95rem;max-width:32rem;}
@media(max-width:600px){.masthead{gap:.5rem}.masthead strong{font-size:1rem}.location{font-size:.78rem}}
</style>
""", unsafe_allow_html=True)
