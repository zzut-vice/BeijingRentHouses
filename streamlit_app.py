import streamlit as st
import base64

# 显示PDF文件的函数
def st_display_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="800" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

def main():
    st.title("在Streamlit中嵌入PDF文件")
    st.subheader("Learn Streamlit")

#     st_display_pdf("https://github.com/zzut-vice/BeijingRentHouses/blob/main/%E5%8C%97%E4%BA%AC%E4%BD%8F%E6%88%BF.pdf")
    st_display_pdf("北京住房.pdf")

if __name__ == '__main__':
    main()

