# @TODO: Import the libraries for Pandas and Streamlit
# YOUR CODE HERE!
import streamlit as st
import pandas as pd

# @TODO: Create a title for your application using markdown syntax and the
# Streamlit `write` function.
# YOUR CODE HERE!

st.write("# Welcome to FJ CBDC Wallet App")
st.write("### This App will manage your FJDCoin")

# @TODO: Create an opening sentence for your application using regular text and
# the Streamlit `write` function.
# YOUR CODE HERE!
st.write("---")
st.write("Bula Vinaka")

# @TODO: Create a Pandas dataframe
# YOUR CODE HERE!
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
st.write(df)


# @TODO: Write the Pandas dataframe to the page
# YOUR CODE HERE!

# @TODO: Create a text input box using the Streamlit `text_input` function.
# @TODO: Save the input as a variable.
# YOUR CODE HERE!

input_value = st.text_input("Enter a Message")

# @TODO: Utilize the Streamlit `button` function to display the text input
# variable created in the prior step to the page.
# YOUR CODE HERE!

if st.button("Display Message"):
    st.write(input_value)

# Bonus
# YOUR CODE HERE!

