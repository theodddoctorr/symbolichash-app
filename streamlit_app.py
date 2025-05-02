import streamlit as st

# Final SymbolHash mapping

def get_cipher(): return { 'A': 'V', 'B': '>', 'C': '<', 'D': '∧', 'E': '⅃', 'F': '⊔', 'G': 'L', 'H': ']', 'I': '□', 'J': '[', 'K': '⎾', 'L': '⊓', 'M': '┌', 'N': '•V', 'O': '•>', 'P': '•<', 'Q': '•∧', 'R': '•⅃', 'S': '•⊔', 'T': '•L', 'U': '•]', 'V': '•□', 'W': '•[', 'X': '•⎾', 'Y': '•⊓', 'Z': '•┌' }

def encode_symbolhash(word): cipher = get_cipher() return ' '.join(cipher.get(char.upper(), '?') for char in word)

def decode_symbolhash(encoded_str): cipher = get_cipher() reverse_cipher = {v: k for k, v in cipher.items()} return ''.join(reverse_cipher.get(sym, '?') for sym in encoded_str.split())

Streamlit UI

st.set_page_config(page_title="SymbolHash Encoder/Decoder", layout="centered") st.title("SymbolHash Encoder/Decoder") st.markdown(""" SymbolHash is a symbolic, reversible cipher created by Jason. It transforms each letter into a geometric or symbolic representation with support for binary logic and dot-state recursion.

Type any word to encode it using SymbolHash, or paste a space-separated symbol string to decode. """)

option = st.radio("Choose mode:", ("Encode", "Decode"))

if option == "Encode": input_text = st.text_input("Enter text to encode:") if input_text: encoded = encode_symbolhash(input_text) st.text_area("Encoded Output:", encoded, height=100) else: encoded_input = st.text_input("Enter space-separated symbols to decode:") if encoded_input: decoded = decode_symbolhash(encoded_input) st.text_area("Decoded Output:", decoded, height=100)

