import streamlit as st
import pandas as pd

# Load or create sample data
try:
    data = pd.read_csv("club_participation.csv")
except FileNotFoundError:
    data = pd.DataFrame({
        "Student": ["Aditi", "Rahul", "Mohan"],
        "Club": ["Coding", "Robotics", "Literature"],
        "Events Attended": [5, 10, 2],
        "Active Member": [True, True, False]
    })

st.title("Project Pragati - Club Participation Dashboard")
st.subheader("Participation Data")
st.dataframe(data)

st.metric("Total Participants", len(data))
st.metric("Active Clubs", data['Club'].nunique())
st.bar_chart(data.set_index("Club")["Events Attended"])

st.subheader("Add Your Participation")
with st.form("add_participation"):
    name = st.text_input("Student Name")
    club = st.text_input("Club Name")
    events = st.number_input("Number of Events Attended", min_value=0)
    active = st.checkbox("Active Member")
    submitted = st.form_submit_button("Submit")
    if submitted:
        new_entry = {"Student": name, "Club": club, "Events Attended": events, "Active Member": active}
        data = data.append(new_entry, ignore_index=True)
        data.to_csv("club_participation.csv", index=False)
        st.success(f"Participation recorded for {name} in {club}!")

st.info("Dashboard demo – customize and enhance for your requirements.")
