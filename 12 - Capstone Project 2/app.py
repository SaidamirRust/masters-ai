import streamlit as st
from doc_loader import load_and_index_documents
from qa_system import create_conversational_chain
from ticket_system import create_github_issue

# Hardcoded company info for answer signature
COMPANY_NAME = "OpenSource Corp"
COMPANY_EMAIL = "support@example.com"
COMPANY_PHONE = "123-456-7890"

st.set_page_config(page_title="Linux Docs Support Bot")
st.title("🐧 Linux Documentation Support Chatbot")

# Initialize vector store and QA chain once
if "qa_chain" not in st.session_state:
    with st.spinner("Loading and indexing documents..."):
        vector_store = load_and_index_documents(data_dir="data")
        st.session_state.qa_chain = create_conversational_chain(vector_store)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []  # will hold past messages

# Chat input
if user_input := st.chat_input("Ask a question about Linux docs:"):
    # Display user message
    st.chat_message("user").write(user_input)

    # Get answer from QA chain
    result = st.session_state.qa_chain(
        {
            "question": user_input,
            "chat_history": st.session_state.chat_history
        }
    )
    answer = result["answer"]
    source_docs = result.get("source_documents", [])

    # Display assistant answer
    st.chat_message("assistant").write(answer)
    st.write(f"**{COMPANY_NAME}** • {COMPANY_PHONE} • {COMPANY_EMAIL}")

    # Show citations under the message
    if source_docs:
        st.markdown("**Citations:**")
        for doc in source_docs:
            src = doc.metadata.get("source", "unknown")
            page = doc.metadata.get("page", "?")
            st.markdown(f"- [source: {src}, page {page}]")

    # Append the turn to chat history
    st.session_state.chat_history.append((user_input, answer))

    # If answer indicates no relevant info, offer ticket creation
    if any(phrase in answer.lower() for phrase in ["i don’t know", "i don't know", "can't find", "cannot find"]):
        st.warning("It seems this question was not answered from the documentation.")
        with st.expander("Submit a Support Ticket"):
            with st.form("ticket_form", clear_on_submit=True):
                st.write("Please fill out the following fields to create a support ticket:")
                ticket_title = st.text_input("Ticket Title", placeholder="Short summary of the issue")
                user_name = st.text_input("Your Name")
                user_email = st.text_input("Your Email")
                ticket_description = st.text_area("Detailed Description of the Issue")
                submitted = st.form_submit_button("Submit Ticket")

                if submitted:
                    if not ticket_title or not ticket_description:
                        st.error("Title and description are required to submit a ticket.")
                    else:
                        # Build GitHub issue body
                        issue_body = (
                            f"**Question:** {user_input}\n"
                            f"**Name:** {user_name or 'Anonymous'}\n"
                            f"**Email:** {user_email or 'Not provided'}\n"
                            f"**Description:**\n{ticket_description}"
                        )
                        try:
                            issue_url = create_github_issue(ticket_title, issue_body)
                            st.success(f"Ticket submitted successfully! [View Issue]({issue_url})")
                        except Exception as e:
                            st.error(f"Failed to create ticket: {e}")