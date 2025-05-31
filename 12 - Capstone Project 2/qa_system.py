from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

# System prompt: instruct the model to include citations in the answer text
system_template = """
You are a customer support assistant specialized in Linux documentation.
When you answer, cite each source by including a bracketed reference with the document name and page number, e.g.:

"Here is the answer... [source: linux-manual.pdf, page 15]"

If you cannot answer based on the provided documentation, simply say "I don’t know.".

Company: OpenSource Corp | Email: support@example.com | Phone: 123-456-7890
"""
system_prompt = SystemMessagePromptTemplate.from_template(system_template)

# Prompt for answering with extracted context
qa_template = """
Use the following passages from Linux documentation to answer the question.

{context}

Question: {question}

Provide a concise answer, and include bracketed citations like [source: filename.pdf, page X] for each fact you use.
If you don't know, say "I don’t know.".
"""
qa_prompt = ChatPromptTemplate.from_messages([
    system_prompt,
    HumanMessagePromptTemplate.from_template(qa_template)
])

def create_conversational_chain(vector_store):
    #Set up a conversational retrieval chain with OpenAI chat model.
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    llm = ChatOpenAI(temperature=0)

    # Build the chain; it will maintain chat history internally
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        combine_docs_chain_kwargs={"prompt": qa_prompt},
        condense_question_prompt=ChatPromptTemplate.from_messages([
            SystemMessagePromptTemplate.from_template(
                """
                Rephrase the user question to be a standalone query.

                Conversation History:
                {chat_history}

                Follow-up Input: {question}

                Standalone question:"""),
            HumanMessagePromptTemplate.from_template("{question}")
        ]),
        return_source_documents=True
    )

    return qa_chain