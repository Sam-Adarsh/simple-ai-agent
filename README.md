# Simple AI Agent with LangGraph and Groq

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)


A simple intelligent agentic workflow built with **LangChain** and **LangGraph**, powered by **Groq's LLaMA 3** models. This project demonstrates how to build a stateful processing pipeline that classifies, extracts entities, and summarizes text in a coordinated manner.

## 🚀 Project Overview

The agent processes input text through a directed graph of operations:
1.  **Classification Node**: Categorizes text into News, Blog, Research, or Other.
2.  **Entity Extraction Node**: Identifies key entities (People, Organizations, Locations).
3.  **Summarization Node**: Generates a concise summary.

This architecture allows for modular, observable, and easier-to-debug AI applications compared to single-prompt chains.

## 🛠️ Tech Stack

-   **LangGraph**: For orchestrating the stateful workflow.
-   **LangChain**: For prompt management and model interaction.
-   **Groq API**: For ultra-fast inference using LLaMA 3 models.
-   **Python 3.11+**: Core programming language.

## 📦 Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ai-agent-langgraph.git
    cd ai-agent-langgraph
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python3 -m venv agent_env
    source agent_env/bin/activate  # On macOS/Linux
    # agent_env\Scripts\activate   # On Windows
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration

1.  **Get a Groq API Key**:
    Sign up at [Groq Console](https://console.groq.com/keys).

2.  **Set up Environment Variables**:
    Create a `.env` file in the root directory:
    ```bash
    touch .env
    ```
    Add your API key:
    ```env
    GROQ_API_KEY=your_actual_api_key_here
    ```

## 🏃 Usage

Run the main agent script:

```bash
python main.py
```

### Example Verification Output
You should see output similar to:
```text
Classification: News

Entities: ['OpenAI', 'GPT-4', 'GPT-3']

Summary: OpenAI has announced the GPT-4 model...
```
