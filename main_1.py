import streamlit as st
import os
st.title("**Super Hero**")
st.header("**Super Hero Name Generator**")
st.write("Welcome to the Super Hero Name Generator! This app will help you create a unique and powerful super hero name based on your preferences. Just answer a few questions, and we'll generate a name that suits your super hero persona!")
st.subheader("**Step 1: Choose Your Super Power**")
super_powers = ["Flight", "Super Strength", "Invisibility", "Telepathy", "Time Manipulation", "Shape Shifting"]
selected_power = st.selectbox("Select your super power:", super_powers)
st.subheader("**Step 2: Choose Your Super Hero Type**")
hero_types = ["Hero", "Villain", "Anti-Hero", "Sidekick"]
selected_type = st.selectbox("Select your super hero type:", hero_types)
st.subheader("**Step 3: Choose Your Super Hero Color**")    
colors = ["Red", "Blue", "Green", "Black", "White", "Yellow"]
selected_color = st.selectbox("Select your super hero color:", colors)
st.subheader("**Your Super Hero Name**")
if st.button("Generate Super Hero Name"):
    super_hero_name = f"{selected_color} {selected_power} {selected_type}"
    st.success(f"Your Super Hero Name is: {super_hero_name}")

st.image(os.path.join(os.getcwd(),"static","Screenshot (1).png"), caption=selected_power)

