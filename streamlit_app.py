import streamlit as st

# Correct SymbolHash cipher (Unicode-safe)
def get_cipher():
    return {
        'A': 'V',    'B': '>',    'C': '<',    'D': '∧',
        'E': '⅃',    'F': '⊔',    'G': 'L',    'H': ']',    'I': '□',
        'J': '[',    'K': '⎾',    'L': '⊓',    'M': '┌',
        'N': '•V',   'O': '•>',   'P': '•<',   'Q': '•∧',
        'R': '•⅃',   'S': '•⊔',   'T': '•L',   'U': '•]', 
        'V': '•□',   'W': '•[',   'X': '•⎾',   'Y': '•⊓',   'Z': '•┌'
    }

def encode_symbolhash(word):
    cipher = get_cipher()
    return ' '.join(cipher.get(char.upper(), '?') for char in word)

def decode_symbolhash(encoded_str):
    cipher = get_cipher()
    reverse_cipher = {v: k for k, v in cipher.items()}
    output = []

    for sym in encoded_str.split():
        if sym == '_':
            output.append(' ')
        else:
            output.append(reverse_cipher.get(sym, '?'))

    return ''.join(output)

st.set_page_config(page_title="SymbolHash", layout="centered")
st.title("SymbolHash Encoder/Decoder")

st.markdown("""
**SymbolHash** is a reversible symbolic encoding system using quadrant geometry and dot-state logic.  
Designed for symbolic language, mathematical resonance mapping, and perceptual compression.
""")

if "history" not in st.session_state:
    st.session_state.history = []

mode = st.radio("Choose mode:", ["Encode", "Decode"])

if mode == "Encode":
    text = st.text_input("Enter text to encode:")
    if text:
        encoded = encode_symbolhash(text)
        st.text_area("Encoded Output:", encoded, height=100)
        st.code(encoded, language="plaintext")
        st.download_button("Download as .txt", data=encoded, file_name="symbolhash.txt")
        st.session_state.history.insert(0, f"Encoded: {text} → {encoded}")

else:
    encoded_input = st.text_input("Paste symbols to decode (space-separated, use `_` for spaces):")
    if encoded_input:
        decoded = decode_symbolhash(encoded_input)
        st.text_area("Decoded Output:", decoded, height=100)
        st.code(decoded, language="plaintext")
        st.session_state.history.insert(0, f"Decoded: {encoded_input} → {decoded}")

# Show history
if st.session_state.history:
    st.markdown("### Recent Activity:")
    for item in st.session_state.history[:5]:
        st.write(item)