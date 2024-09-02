import streamlit as st
import json

def generate_json(kol_id, eng_code, ja_code, ko_code):
    result = []
    result.append({
        "kol_id": kol_id,
        "promotion_code": eng_code
    })
    result.append({
        "kol_id": kol_id,
        "promotion_code": ja_code,
        "language": "ja"
    })
    result.append({
        "kol_id": kol_id,
        "promotion_code": ko_code,
        "language": "ko"
    })
    return json.dumps(result, indent=4)

# Streamlit 应用界面
st.title("JSON Generator for KOL Promotions")

kol_id = st.text_input("KOL ID")
eng_code = st.text_input("英语 Promotion Code")
ja_code = st.text_input("日语 Promotion Code")
ko_code = st.text_input("韩语 Promotion Code")

if st.button("生成 JSON"):
    if kol_id and eng_code and ja_code and ko_code:
        json_output = generate_json(kol_id, eng_code, ja_code, ko_code)
        st.text_area("生成的 JSON", json_output, height=200)
    else:
        st.error("请确保所有输入框都已填写。")
