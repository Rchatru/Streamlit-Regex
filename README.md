# Streamlit-Regex

## **The Regex wizard!**
Esta aplicación permite importar archivos de texto extraídos de subtítulos de videos de YouTube y realizar una limpieza para obtener finalmente un txt limpio y legible.
Se eliminan frases repedidas, saltos de línea, timestamps y caracteres especiales de separación.

Texto de ejemplo extraído directamente de los subtítulos de YouTube:
````
WEBVTT
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
pues agradecerte tanto a ti como a
````

Después de la limpieza: 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/rchatru/streamlit-regex/regex.py)
````
WEBVTT

Kind: captions

Language: es

muchas gracias y bueno antes de todo

pues agradecerte tanto a ti como a

silver en la oportunidad porque en
````


