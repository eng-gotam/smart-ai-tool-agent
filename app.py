
import streamlit as st

from agent import ask_agent_with_trace
from config import GEMINI_MODEL


# Page configuration
st.set_page_config(
    page_title="Smart AI Agent",
    page_icon="🤖",
    layout="wide"
)


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom styling

st.markdown("""
<style>

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

[data-testid="stChatMessage"] {
    background-color: #172033;
    border: 1px solid #263247;
    border-radius: 14px;
    padding: 12px;
    margin-bottom: 8px;
}

.hero {
    padding: 22px;
    background: linear-gradient(135deg, #172554, #312e81);
    border: 1px solid #3730a3;
    border-radius: 16px;
    margin-bottom: 18px;
}

.hero h1 {
    color: #FFFFFF;
    font-size: 32px;
    margin: 0;
    padding: 0;
}

.hero p {
    color: #CBD5E1;
    font-size: 15px;
    margin-top: 8px;
    margin-bottom: 0;
}

.tool-card {
    background-color: #172033;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 14px;
    min-height: 100px;
}

.tool-card h4 {
    color: #93C5FD;
    font-size: 18px;
    margin: 0;
    padding: 0;
}

.tool-card p {
    color: #CBD5E1;
    font-size: 13px;
    margin-top: 8px;
    margin-bottom: 0;
}

</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:

    st.title("🤖 Smart AI Agent")

    st.caption("Intelligent Tool Calling System")

    st.divider()

    st.subheader("Model Information")

    st.code(GEMINI_MODEL, language=None)

    st.caption("Provider: Google Gemini")

    st.divider()

    st.subheader("Available Tools")

    st.markdown("🧮 **Calculator**")
    st.caption("Perform mathematical operations.")

    st.markdown("🕒 **DateTime**")
    st.caption("Retrieve current date and time.")

    st.markdown("📝 **Text Analyzer**")
    st.caption("Analyze words and characters.")

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption("Developed by Gotam Kumar")
    st.caption("BS Artificial Intelligence")


# Header
st.markdown("""
<div class="hero">
    <h1>🤖 Smart AI Agent</h1>
    <p>
        An intelligent assistant that connects
        language models with real-world Python tools.
    </p>
</div>
""", unsafe_allow_html=True)


# Tool cards
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="tool-card">
        <h4>🧮 Calculator</h4>
        <p>Accurate mathematical calculations.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="tool-card">
        <h4>🕒 DateTime</h4>
        <p>Current date and timezone information.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="tool-card">
        <h4>📝 Text Analyzer</h4>
        <p>Word and character analysis.</p>
    </div>
    """, unsafe_allow_html=True)


st.divider()


# Display example prompts
if not st.session_state.messages:

    st.subheader("Try an example")

    st.markdown("""
    - What is 250 multiplied by 18?
    - What is the current time in Karachi?
    - Count the words in "Artificial Intelligence is powerful".
    - What is machine learning?
    """)


# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        if message.get("tools"):

            with st.expander("⚡ Tool Execution"):

                for tool in message["tools"]:
                    st.success(f"{tool} executed")

        st.markdown(message["content"])


# User input
if prompt := st.chat_input("Ask me anything..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Agent is processing your request..."):

            result = ask_agent_with_trace(prompt)

        if result["tools"]:

            with st.expander(
                "⚡ Tool Execution",
                expanded=True
            ):

                for tool in result["tools"]:
                    st.success(f"{tool} executed")

        st.markdown(result["answer"])

    st.session_state.messages.append({
        "role": "assistant",
        "content": result["answer"],
        "tools": result["tools"]
    })
