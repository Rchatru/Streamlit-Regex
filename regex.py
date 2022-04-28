import re
import hashlib
import streamlit as st

output_file_path = "C:/Users/rrcht/OneDrive/Documentos/Personal/Python/out.txt"
input_file_path = "C:/Users/rrcht/OneDrive/Documentos/Personal/Python/new.txt"





completed_lines_hash = set()
output_file = open(output_file_path, "w")

input = open(input_file_path, "r", encoding='utf-8')

for line in input:
    line = str(line)
    line = re.sub(r'(<[^>]+>)|(0[^%]+%)',"", line)
    # line = line.rstrip()
    line = line.replace("\\n", "")

    hashValue = hashlib.md5(line.encode('utf-8')).hexdigest()
    if hashValue not in completed_lines_hash:
        output_file.write(line)
        output_file.write("\n")
        completed_lines_hash.add(hashValue)
        print(line)

        
# Web App Title
st.markdown('''
# **The EDA App**

This is the **EDA App** created in Streamlit using the **pandas-profiling** library.

**Credit:** App built in `Python` + `Streamlit` by [Chanin Nantasenamat](https://medium.com/@chanin.nantasenamat) (aka [Data Professor](http://youtube.com/dataprofessor))

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your txt file'):
    uploaded_file = st.sidebar.file_uploader("Upload your input txt file", type=["txt"])

# Pandas Profiling Report
if uploaded_file is not None:
    @st.cache
    def load_txt():
        txt = open(input_file_path, "r", encoding='utf-8')
        return txt
    df = load_txt()
    
    st.header('**Input DataFrame**')
    st.write(txt)
    st.write('---')


input.close()
output_file.close()
