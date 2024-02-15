#pip install streamlit
#Create hello.py and run it:
#streamlit run hello.py
#Open http://localhost:8501/
import streamlit as st


st.title("Hello World")

st.write("This is Rafi Ali")

st.markdown("# Markdown content")

st.code("""if post == "good":
        print("Hit Like")""")

