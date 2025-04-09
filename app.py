# app.py

import streamlit as st
import random

# Set page title and icon
st.set_page_config(page_title="🪨 Rock, Paper, Scissors ✂️", page_icon="🎮")

# Add a colorful title
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: white;
        background-color: #FF5733;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
    <div class="title">🪨 Rock, Paper, Scissors ✂️</div>
    """,
    unsafe_allow_html=True
)

# Add a colorful header
st.markdown(
    """
    <style>
    .header {
        font-size: 30px;
        font-weight: bold;
        color: #33FF57;
        text-align: center;
    }
    </style>
    <div class="header">✨ Let's Play! ✨</div>
    """,
    unsafe_allow_html=True
)

# Add instructions
st.markdown(
    """
    <style>
    .instructions {
        font-size: 20px;
        color: #33A8FF;
        text-align: center;
    }
    </style>
    <div class="instructions">🎯 Choose Rock, Paper, or Scissors to play against the computer.</div>
    """,
    unsafe_allow_html=True
)

# Initialize session state for game results
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# Define game choices
choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]

# Add buttons for user choice
user_choice = st.radio("👉 Your Choice:", choices)

# Add a button to play the game
if st.button("🚀 Play"):
    # Computer makes a random choice
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie! 😐"
    elif (user_choice == "🪨 Rock" and computer_choice == "✂️ Scissors") or \
         (user_choice == "📄 Paper" and computer_choice == "🪨 Rock") or \
         (user_choice == "✂️ Scissors" and computer_choice == "📄 Paper"):
        result = "You win! 🎉"
        st.session_state.user_score += 1
    else:
        result = "Computer wins! 😢"
        st.session_state.computer_score += 1

    # Display the results
    st.markdown(
        f"""
        <style>
        .result {{
            font-size: 25px;
            font-weight: bold;
            color: #FFA500;
            text-align: center;
        }}
        </style>
        <div class="result">🎮 You chose: {user_choice}</div>
        <div class="result">🤖 Computer chose: {computer_choice}</div>
        <div class="result">🏆 Result: {result}</div>
        """,
        unsafe_allow_html=True
    )

# Display scores
st.markdown(
    f"""
    <style>
    .score {{
        font-size: 25px;
        font-weight: bold;
        color: #33FF57;
        text-align: center;
    }}
    </style>
    <div class="score">📊 Your Score: {st.session_state.user_score}</div>
    <div class="score">📊 Computer Score: {st.session_state.computer_score}</div>
    """,
    unsafe_allow_html=True
)

# Add a colorful footer
st.markdown(
    """
    <style>
    .footer {
        font-size: 20px;
        color: #33C1FF;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    <div class="footer">🚀 Thanks for playing Rock, Paper, Scissors! 🚀</div>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <h5 style="color: red; font-weight: bold; text-align: center; margin-top: 20px; margin-left: 45px;">
        ✏️📚 Author: Azmat Ali 📚✏️
    </h5>
    """,
    unsafe_allow_html=True
)