import streamlit as st
from utils.api_utils import fetch_models, generate_response
from utils.file_utils import download_pdf

def main():
    st.title("Credit Letter Generator")
    st.markdown("Create professional credit dispute letters tailored to your needs.")

    # Fetch available models
    try:
        models = fetch_models()
    except RuntimeError as e:
        st.error(e)
        return

    # Select a model
    model_name = st.selectbox("Select Model", options=models, index=0)

    # Input for letter details
    st.subheader("Letter Details")
    recipient_name = st.text_input("Recipient Name")
    account_details = st.text_area("Account Details")
    dispute_reason = st.text_area("Dispute Reason")

    # Generate letter
    if st.button("Generate Letter"):
        if not all([recipient_name, account_details, dispute_reason]):
            st.warning("Please fill in all the fields before generating the letter.")
            return

        prompt = f"""
        Generate a credit dispute letter for {recipient_name}.
        Account Details: {account_details}.
        Dispute Reason: {dispute_reason}.
        """
        try:
            response = generate_response(model_name, prompt)
            letter_content = response.get("text", "No content generated.")
            st.success("Letter Generated Successfully!")
            st.text_area("Generated Letter", value=letter_content, height=300)

            # Download options
            pdf_file = download_pdf(letter_content, "credit_letter.pdf")
            st.download_button(
                label="Download as PDF", 
                data=pdf_file, 
                file_name="credit_letter.pdf",
                mime="application/pdf"
            )
        except RuntimeError as e:
            st.error(e)

if __name__ == "__main__":
    main()
