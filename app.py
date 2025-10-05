import io
from pydub import AudioSegment
import streamlit as st

st.title("Audio Converter")

uploaded_files = st.file_uploader(
    "Upload an audio file you want to convert", accept_multiple_files=True, type=".m4a"
)

for uploaded_file in uploaded_files:
    if uploaded_file is not None:
        try:
            filename = uploaded_file.name
            print('filename', filename)
            sound = AudioSegment.from_file(uploaded_file, format="m4a")
            buffer = io.BytesIO()
            sound.export(buffer, format="wav")
            exported_audio = buffer.getvalue()
            st.download_button(
	            label="Download converted audio",
	            data=exported_audio,
	            file_name=f"{filename.split(".")[0]}.wav")

        except Exception as e:
            print(f"Error converting '{filename}': {e}")
