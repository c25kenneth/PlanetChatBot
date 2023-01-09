import streamlit as st
from bot import chatbot

st.title("PlanetBot")

st.write("PlanetBot is a chatbot that can answer questions about the planets of our solar system!")
st.write("PlanetBot can return JSON data on a variety of planets and their moons.")
st.write("To get started, simply enter in your question in the text field, and PlanetBot will give you an answer back in seconds.")

st.image("SolarSystemDiagram.jpg")

question = st.text_input("Enter in your question")
button = st.button("Get response from PlanetBot")

if button and question:
    response = chatbot.get_response(question)
    st.write(response)
