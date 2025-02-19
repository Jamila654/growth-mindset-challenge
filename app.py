# type: ignore
import streamlit as st

# App Title and Header
st.title("🚀 Growth Mindset Challenge!")
st.header("Code Seekho, Seekh ke Maidaan Maaro!")


# Main Content Area
st.subheader("What's Your Biggest Coding Challenge?")

# User Input for Coding Challenge
user_input = st.text_input("✍ Aapki sabse badi coding challenge kya hai?", key="challenge_input")

if user_input:
    st.success(f"Great! {user_input} solve kerna apke growth ka part hai! Keep going! 💪")
    # Additional interaction after input
    if st.button("Need Advice?"):
        st.info("Remember, every challenge is a step towards mastery! Try breaking it down into smaller parts.")

# Motivational Message and Additional Content
st.subheader("Motivation Station")
st.write("Jo try nahi karta, wo kabhi nahi jeetta! 💯")

# Adding more motivational content or resources
st.markdown("""
- **Consistency**: Practice coding daily, even if it's just for 15 minutes.
- **Community**: Join coding groups or forums. Learning together can be fun and productive.
- **Resources**: 
  - [FreeCodeCamp](https://www.freecodecamp.org/)
  - [LeetCode](https://leetcode.com/)
""")

# Footer
st.write("---")
st.write("**Happy Coding!**")