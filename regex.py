from io import StringIO
import re
import hashlib
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi


completed_lines_hash = set()
out = ""
  
def text_processing(string_in, completed_lines_hash):
    for line in string_in:
        line = str(line)
        line = re.sub(r'(<[^>]+>)|(0[^%]+%)|([0-9]+:[0-9]+)',"", line)
        line = line.replace("\\n", "")
        
        for line in text.splitlines():
            hashValue = hashlib.md5(line.encode('utf-8')).hexdigest()
            if hashValue not in completed_lines_hash:
                out += line
                out += "\n"
                completed_lines_hash.add(hashValue)
        st.write(out)
    return out
 
before='''WEBVTT
Kind: captions
Language: es

00:00:10.480 --> 00:00:13.680 align:start position:0%
 
muchas <00:00:10.964><c>gracias </c><00:00:11.448><c>y </c><00:00:11.932><c>bueno </c><00:00:12.416><c>antes </c><00:00:12.900><c>de </c><00:00:13.384><c>todo</c>

00:00:13.680 --> 00:00:13.690 align:start position:0%
muchas gracias y bueno antes de todo
 

00:00:13.690 --> 00:00:16.140 align:start position:0%
muchas gracias y bueno antes de todo
pues <00:00:14.079><c>agradecerte </c><00:00:14.468><c>tanto </c><00:00:14.857><c>a </c><00:00:15.246><c>ti </c><00:00:15.635><c>como </c><00:00:16.024><c>a</c>

00:00:16.140 --> 00:00:16.150 align:start position:0%
pues agradecerte tanto a ti como a'''

after= '''WEBVTT

Kind: captions

Language: es

muchas gracias y bueno antes de todo
pues agradecerte tanto a ti como a
silver en la oportunidad porque en'''


# Web App Title
st.markdown('''
# **The Regex wizard!**

Esta aplicación permite importar archivos de texto extraídos de subtítulos de videos de YouTube y realizar una limpieza para obtener finalmente un txt limpio y legible.
Se eliminan frases repedidas, saltos de línea, timestamps y caracteres especiales de separación.

Texto de ejemplo extraído directamente de los subtítulos de YouTube:
''')

st.code(before,language=None)

st.markdown(''' Después de la limpieza:
''')

st.code(after,language=None)


st.markdown('''

**Credit:** App built in `Python` + `Streamlit` by [Roberto](https://github.com/rchatru)

---
''')

# Upload CSV data
with st.sidebar.header('1. Upload your txt file'):
    input = st.sidebar.file_uploader("Upload your input txt file", type=["txt"])


if input is not None:
    string_in = StringIO(input.read().decode('utf-8'))
    
    out = text_processing(string_in)
    
    with st.sidebar:
        st.header('2. Download processed txt file')
        st.download_button('Download file', out)
    

else:

    # Text Input
    
    # save the input text in the variable 'name'
    # first argument shows the title of the text input box
    # second argument displays a default text inside the text input area
    text = st.text_area("Enter text for processing")
    
    with st.form("yt_url"):
        st.write("Or paste the video URL")
        url = st.text_input('Youtube video URL')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            text = YouTubeTranscriptApi.get_transcript("submitted")
            out = text_processing(text, completed_lines_hash)
            
            with st.sidebar:
                st.header('2. Download processed txt file')
                st.download_button('Download file', out)
    
    if(st.button('Submit')):
        st.success('Correcto')

        text_processing(text, completed_lines_hash)
        
        with st.sidebar:
            st.header('2. Download processed txt file')
            st.download_button('Download file', out)
