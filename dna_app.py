# Import necessary libraries
import pandas as pd
import streamlit as st
import altair as alt

# Display the main title and description of the app
st.write("""
# DNA Nucleotide Counter

This app counts the nucleotide composition of query DNA

***
""")

# Prompt user for DNA sequence input
st.header('Enter DNA sequence')
sequence_input = ">DNA Query\ngatacccaggctttgcgtacatcagtctgaggttttcatgataacccagggccaaatcaaaggtggagttcggaattgaggcaaggactcatcggattcaccttctgtctgcgacatgct"
sequence = st.text_area("Sequence input (only A, T, G, C characters are allowed)", sequence_input, height=250)

# Process the DNA sequence input
sequence = sequence.splitlines()
sequence = sequence[1:]  # Skips the sequence name (first line)
sequence = ''.join(sequence)  # Concatenates list to string
sequence = sequence.upper()  # Convert to uppercase to handle case sensitivity

# Validate the sequence to contain only valid DNA nucleotides
valid_nucleotides = set("ATGC")
if set(sequence) - valid_nucleotides:
    st.error("The provided DNA sequence contains invalid characters. Please input a valid DNA sequence.")
    st.stop()

sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

# Display the processed DNA sequence
st.header('INPUT (DNA Query)')

# Display the DNA nucleotide count results
st.header('OUTPUT (DNA Nucleotide Count)')
st.subheader('1. Print dictionary')

from collections import Counter

def DNA_nucleotide_count(seq):
    nucleotide_counts = Counter(seq)
    return {
        'A': nucleotide_counts.get('A', 0),
        'T': nucleotide_counts.get('T', 0),
        'G': nucleotide_counts.get('G', 0),
        'C': nucleotide_counts.get('C', 0)
    }

# Call the nucleotide counting function
X = DNA_nucleotide_count(sequence)

# Display the nucleotide counts in textual format
st.subheader('2. Print text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

# Convert the nucleotide counts to a DataFrame and display it
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

# Visualize the nucleotide counts using a bar chart
st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80) # controls width of bar
)
st.write(p)
