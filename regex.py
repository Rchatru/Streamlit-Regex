import re
import hashlib
import streamlit as st

# output_file_path = "C:/Users/rrcht/OneDrive/Documentos/Personal/Python/out.txt"
# input_file_path = "C:/Users/rrcht/OneDrive/Documentos/Personal/Python/new.txt"





completed_lines_hash = set()
# output_file = open(output_file_path, "w")

# input = open(input_file_path, "r", encoding='utf-8')

# for line in input:
#     line = str(line)
#     line = re.sub(r'(<[^>]+>)|(0[^%]+%)',"", line)
#     # line = line.rstrip()
#     line = line.replace("\\n", "")

#     hashValue = hashlib.md5(line.encode('utf-8')).hexdigest()
#     if hashValue not in completed_lines_hash:
#         output_file.write(line)
#         output_file.write("\n")
#         completed_lines_hash.add(hashValue)
#         print(line)

        
# Web App Title
st.markdown('''
# **The Regex wizard!**

Esta aplicación permite importar archivos de texto extraídos de subtítulos de videos de YouTube y realizar una limpieza para obtener finalmente un txt limpio y legible.
Se eliminan frases repedidas, saltos de línea y timestamps y caracteres especiales de separación.

**Credit:** App built in `Python` + `Streamlit` by [Roberto](https://github.com/rchatru)

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your txt file'):
    input = st.sidebar.file_uploader("Upload your input txt file", type=["txt"])


# Pandas Profiling Report
if input is not None:

    for line in input:
        line = str(line)
        line = re.sub(r'(<[^>]+>)|(0[^%]+%)',"", line)
        line = line.replace("\\n", "")

        hashValue = hashlib.md5(line.encode('utf-8')).hexdigest()
        if hashValue not in completed_lines_hash:
            # out.write(line)
            # out.write("\n")
            completed_lines_hash.add(hashValue)
            st.write(line)
            # st.download_button('Download file', out)




