import streamlit as st


def header_home():

    logo_url = "https://upload.wikimedia.org/wikipedia/en/d/d2/Birla_Institute_of_Technology_Mesra.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:inherit'>BIT<br/>MESRA</h1>
        </div>   
                
                """, unsafe_allow_html=True)
    
def header_dashboard():

    logo_url = "https://upload.wikimedia.org/wikipedia/en/d/d2/Birla_Institute_of_Technology_Mesra.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:inherit'>BIT<br/>MESRA</h2>
        </div>""",unsafe_allow_html=True) 
    