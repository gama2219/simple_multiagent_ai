# simple_multiagent_ai
 A simple multi-agent system designed to dynamically coordinate specialized AI agents and their tools to intelligently respond to user queries.
 
![simpleagent1](https://github.com/user-attachments/assets/51323808-59df-4e53-9271-4c0f1c50eb15)


# ✨ Key Features

* Hierarchical Agent Coordination:** A central Supervisor Agent manages workflow and task delegation.
  Specialized Agents:
    * Data Loader Agent: Responsible for efficiently accessing, parsing, and preparing data from various sources.
    * Research Agent: Capable of performing in-depth information gathering through web search
* Dynamic Tool Integration: Agents can utilize specific tools (e.g., web search) to perform their tasks effectively.
* Intelligent Query Resolution: Breaks down complex queries and assigns sub-tasks to the most suitable agent.
* Text-Only Responses: The project currently focuses on generating high-quality text-based answers.

# 🚀 How It Works

1.  User Query Received: A new query is submitted via the Gradio chatbot interface.
2.  Supervisor Initializes: The Supervisor Agent, powered by LangGraph, analyzes the query and determines the optimal path.
3.  Data Loading (if needed): If the query requires external data, the Supervisor delegates to the **Data Loader Agent**.
     The Data Loader fetches and processes necessary information.
4.  Research :The Supervisor then instructs the "Research Agent" to conduct in-depth analysis  or generate creative content based on the query .
     The Research Agent may use its own tools (e.g., web search, knowledge bases).
5.  **Final Response Generation:** The Supervisor synthesizes the outputs from both agents into a coherent, comprehensive, and user-friendly text response.
6.  **Response Delivered:** The final answer is presented back to the user within the Gradio chatbot.

# 🛠️ Installation


Before you begin, ensure you have the following installed:

* **Python 3.9+** 

# Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/gama2219/simple_multiagent_ai.git
    cd simple_multiagent_ai
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd simple_multiagent_ai
    ```
3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate   # On Windows
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up environment variables:**
    * Create a `.env` file in the `simple_multiagent_ai/` directory and add your keys:
        ```
        # GOOGLE_API_KEY="your_google_key_here"
        ```

## ⚙️ How to Use

Once installed and configured, you can launch the Gradio chatbot interface.

1.  **Ensure you are in the `simple_multiagent_ai` directory:**
    ```bash
    cd simple_multiagent_ai/simple_multiagent_ai
    ```
    (If you followed the installation steps, you should already be in this directory.)

2.  **Run the application:**
    ```bash
    python app.py
    ```

3.  **Access the Chatbot:**
    * This command will start a local Gradio server.
    * Open your web browser and navigate to: `http://127.0.0.1:7860`

4.  **Interact with the Chatbot:**
    * Type your query into the input box and press Enter.
    * Observe how the multi-agent system processes your request and provides a text-based response.
![agent2](https://github.com/user-attachments/assets/eedb6bd4-7ded-41b8-97ee-03a248c4fdc5)

---
