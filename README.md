# ollama_chatbot_summarizerr
This is a simple summarizer chatbot built using the Ollama framework and powered by the llama3.2 model. The chatbot takes user input (e.g., long text, articles, or documents) and returns a concise summary in natural language.

Key Features
✨ Uses the powerful llama3.2 model for intelligent summarization.

⚙️ Built with LangChain and Python for modular prompt handling.

💬 Chat-like interface for intuitive user interaction.

📄 Supports summarizing long text blocks into shorter, meaningful content.

How It Works
The app defines a structured prompt using LangChain's ChatPromptTemplate.

When a user submits text, the chatbot invokes the template with the input.

The llama3.2 model processes the prompt and generates a summary response.

Requirements
Ollama installed and running with llama3.2 model pulled.

Python dependencies (LangChain,argparse)
