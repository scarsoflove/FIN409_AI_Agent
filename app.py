import streamlit as st
from agent import generate_industry_analysis


st.set_page_config(
    page_title="FIN409 Industry Analyst AI Agent",
    page_icon="📊"
)


st.title("📊 FIN409 Industry Analyst AI Agent")

st.write(
    "AI-powered Porter’s Five Forces Industry Analysis Assistant"
)


industry = st.text_input(
    "Enter an industry to analyse:",
    "China Electric Vehicle Industry"
)


if st.button("Generate Analysis"):

    with st.spinner("Analysing industry..."):

        try:
            result = generate_industry_analysis(industry)

            st.subheader("Industry Analysis Result")

            st.write(result)

        except Exception as e:

            st.error(
                f"Error: {e}"
            )