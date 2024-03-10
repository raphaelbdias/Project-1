# web app
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

tab1,tab2,tab3,tab4 = st.tabs(['Welcome', 'Professional', 'Projects', 'Contact'])

with tab1:
    col1, col2 = st.columns([1,2])
    with col1:
        st.title('Welcome')
        st.write("Hello, and welcome to my profile!")

        st.markdown("""<div style="text-align: justify;">I'm currently serving as a Compliance Analyst, 
    where I navigate the intricacies of company compliance and business law in India.</div>""", unsafe_allow_html=True)
        st.write('')
        st.markdown("""<div style="text-align: justify;">My specialisation lies in incorporating companies for individuals from across the globe, 
    a role that grants me the privilege to engage with clients from diverse cultures and backgrounds.</div>""", unsafe_allow_html=True)
        st.write('')
        st.markdown("""<div style="text-align: justify;">With a keen eye for detail and a dedication to staying updated on regulatory changes,
    I ensure that all compliance requirements are met efficiently and effectively.</div>""", unsafe_allow_html=True)
        st.write('')
        st.write("Let's connect!")

with tab2:
    st.title('My Experience')
    st.write('Experirence 1')