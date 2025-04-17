import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2, col3= st.columns([0.3, 0.5, 1])

with col1:
    st.title("SER2")
    st.subheader("Quantity: 22")
    st.subheader("Size: 6 ft")
    st.link_button(label="Google sheets",
                   url="https://docs.google.com/spreadsheets/d/1Roe8IzbNcUi4rwRpYZQb4Zvmpqvi-iDTvRbwZSTRnkY/edit?usp=sharing")

with col2:
    st.image("2.jpg", width=300)

with col3:
    sheet_id = "1Roe8IzbNcUi4rwRpYZQb4Zvmpqvi-iDTvRbwZSTRnkY"
    gid = "737078015"

    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

    df1 = pd.read_csv(csv_url, usecols=[1,2,3,4,5])
    df1_clean = df1.dropna()
    
    st.dataframe(df1_clean, width= 515, hide_index=True, use_container_width=False)

    sheet_id = "1Roe8IzbNcUi4rwRpYZQb4Zvmpqvi-iDTvRbwZSTRnkY"
    gid = "687391187"

    csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

    df2 = pd.read_csv(csv_url, usecols=[7])
    df2_clean = df2.dropna()
    
    st.dataframe(df2_clean, width= 200, hide_index=True, use_container_width=False)
    
    

    
