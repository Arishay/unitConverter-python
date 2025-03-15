import streamlit as st

def convertUnit(value , unitFrom, unitTo):
    conversions = {
        "meters_kilometers":0.001,
        "kilometers_meters": 1000,
        "grams_kilograms":0.001,
        "kilograms_grams": 1000,
        "foots_centimeters": 30.48,
        "centimeters_foots": 0.0328,
        "foots_inches": 12,
        "inches_foots": 0.086
    }

    key = f"{unitFrom}_{unitTo}"

    if key in conversions:
        conversion = conversions[key]
        return value*conversion
    
    else:
        return "❌ Conversion not found"
    

st.title("🙂‍↔️ Unit Converter")

value = st.number_input("↪ Enter the value:" , min_value=1.0 , step=1.0)

unitFrom = st.selectbox("🔄Convert From:" , ["meters","kilometers","grams","kilograms","foots","centimeters","inches"])

unitTo =st.selectbox("🔁 Convert To:", ["meters","kilometers","grams","kilograms","centimeters","foots","inches"])


if st.button("📌 Convert"):
    result = convertUnit(value,unitFrom,unitTo)
    st.write(f"✅ Converted Value is :{result}")

st.markdown("-_- 🔗Unit Converter By Arisha -_-")