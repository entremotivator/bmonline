import streamlit as st
from utils.api_utils import fetch_models, generate_response
from utils.file_utils import download_csv

def main():
    st.title("Contact Generator")
    st.markdown("Generate detailed contact information for your needs.")

    # Fetch available models
    try:
        models = fetch_models()
    except RuntimeError as e:
        st.error(e)
        return

    # Select a model
    model_name = st.selectbox("Select Model", options=models, index=0)

    # Input for contact details
    st.subheader("Contact Generation Details")
    contact_type = st.selectbox("Contact Type", ["Business", "Personal", "Organization"])
    additional_info = st.text_area("Additional Information (optional)")

    # Generate contacts
    if st.button("Generate Contacts"):
        prompt = f"Generate {contact_type} contact details. {additional_info}"
        try:
            response = generate_response(model_name, prompt)
            contacts = response.get("data", [])
            if not contacts:
                st.warning("No contacts generated.")
                return
            
            st.success("Contacts Generated Successfully!")
            st.table(contacts)

            # Download options
            csv_file = download_csv(contacts, "contacts.csv")
            st.download_button(
                label="Download as CSV", 
                data=csv_file, 
                file_name="contacts.csv",
                mime="text/csv"
            )
        except RuntimeError as e:
            st.error(e)

if __name__ == "__main__":
    main()
