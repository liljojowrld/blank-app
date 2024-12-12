import streamlit as st

left, right = st.columns(2)

with left:
    st.write("Hallo")


with right:
    st.write("Bye")

left, right = st.columns(2)

with left :
    st.image("https://is1-ssl.mzstatic.com/image/thumb/AMCArtistImages211/v4/86/7e/49/867e497d-561c-a0cf-6d15-445cc08f91df/ae2a0d84-600a-48e0-94dd-c78af373ac9b_ami-identity-2acbcd55418649b971b6374771ac9ed9-2024-09-28T10-41-42.831Z_cropped.png/486x486bb.png")

with right :
    st.image("https://i1.sndcdn.com/artworks-F1KJfzcgwRzBsPQR-A5niAg-t500x500.jpg")

left,right = st.columns(2)

with left :
    st.title("LACAZETTE")

with right :
    st.title("IST MEGATRON")

left, right = st.columns(2)

with left : 
    st.header("PSYCHOSE")

with right :
    st.header("KOKA-SCHADEN")

    left, right = st.columns(2)

    left.header("Neu Links")     
    right.header("Neu Rechts")

st.title("Große Überschrift" ,)
st.header("Kleiner", anchor=False, divider=True)
st.subheader("Noch kleiner", anchor=False, divider=True)
st.write("Webseite von liljojowrld")
st.image("https://images.genius.com/007e4a05ad4a42400391b9871ade32cb.1000x1000x1.png")
st.video("https://www.youtube.com/watch?v=-VphUV6QNeU")
st.image("https://images.genius.com/36b6584eeb56517669c004074284cad1.1000x1000x1.png")
st.video("https://www.youtube.com/watch?v=0HbLZC7cSO8")
st.image("https://images.genius.com/e11cf6a8f2e270819e7215179a480848.1000x1000x1.png")
st.video("https://www.youtube.com/watch?v=DZllJqtWxoM")
st.image("https://images.genius.com/0016c880e4bff0b8abc98071b0dd1550.1000x1000x1.png")
st.video("https://www.youtube.com/watch?v=VN6KKXUMaik")
st.image("https://images.genius.com/937720f3a35de0bc58360024f304a8d7.1000x1000x1.png")
st.video("https://www.youtube.com/watch?v=xVGSbgHw49g")