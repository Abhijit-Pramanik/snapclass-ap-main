import streamlit as st


def footer_home():
    logo_url = "https://img.magnific.com/premium-vector/ap-logo-design-symbol-initial-letter_772785-32440.jpg?semt=ais_hybrid&w=740&q=80"
    #Slogo_url = "https://www.shutterstock.com/shutterstock/photos/341032196/display_1500/stock-vector-ap-initial-monogram-logo-341032196.jpg"
    # logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://img.magnific.com/premium-vector/ap-logo-design-symbol-initial-letter_772785-32440.jpg?semt=ais_hybrid&w=740&q=80"
    #logo_url = "https://www.shutterstock.com/shutterstock/photos/341032196/display_1500/stock-vector-ap-initial-monogram-logo-341032196.jpg"
    # logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)