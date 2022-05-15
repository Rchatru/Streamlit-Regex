from io import StringIO
import re
import hashlib
import streamlit as st

completed_lines_hash = set()
out = ""
  
# Web App Title
st.markdown('''
# **The Regex wizard!**

Esta aplicación permite importar archivos de texto extraídos de subtítulos de videos de YouTube y realizar una limpieza para obtener finalmente un txt limpio y legible.
Se eliminan frases repedidas, saltos de línea, timestamps y caracteres especiales de separación.

**Credit:** App built in `Python` + `Streamlit` by [Roberto](https://github.com/rchatru)

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your txt file'):
    input = st.sidebar.file_uploader("Upload your input txt file", type=["txt"])


if input is not None:
    string_in = StringIO(input.read().decode('utf-8'))
    for line in string_in:
        line = str(line)
        line = re.sub(r'(<[^>]+>)|(0[^%]+%)|([0-9]+:[0-9]+)',"", line)
        line = line.replace("\\n", "")

        hashValue = hashlib.md5(line.encode('utf-8')).hexdigest()
        if hashValue not in completed_lines_hash:
            out += line
            out += "\n"
            completed_lines_hash.add(hashValue)
    st.write(out)
    with st.sidebar:
        st.header('2. Download processed txt file')
        st.download_button('Download file', out)
    

else:

    # Text Input
    
    # save the input text in the variable 'name'
    # first argument shows the title of the text input box
    # second argument displays a default text inside the text input area
    text = st.text_area("Enter text for processing")
    
    if(st.button('Submit')):
        st.write(len(text),text)
        st.success('Correcto')

        text = str(text)
        text = re.sub(r'(<[^>]+>)|(0[^%]+%)|([0-9]+:[0-9]+)',"", text)
        text = text.replace("\\n", "")

        for line in text.splitlines():
            hashValue = hashlib.md5(line.encode('utf-8')).hexdigest()
            if hashValue not in completed_lines_hash:
                out += line
                out += "\n"
                completed_lines_hash.add(hashValue)
        st.write(out)
        with st.sidebar:
            st.header('2. Download processed txt file')
            st.download_button('Download file', out)



