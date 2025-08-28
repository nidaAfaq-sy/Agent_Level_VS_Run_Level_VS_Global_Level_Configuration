📘 README.md
# Gemini + Agents Framework

This project demonstrates how to use **Google Gemini models** with the **Agents framework** via the **OpenAI-compatible endpoint**.

---

## ⚡ Requirements

- Python 3.10+
- Virtual environment recommended

Install dependencies:

```bash
pip install -r requirements.txt


requirements.txt should include at least:

openai
python-dotenv
agents

🔑 Setup API Key

Get a Gemini API Key from Google AI Studio
.

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

▶️ Run the Project

Activate your virtual environment and run:

python main.py

📂 Project Structure
.
├── main.py         # Main entry point
├── .env            # Contains GEMINI_API_KEY
├── requirements.txt
└── README.md

⚙️ Notes

Base URL must be:

https://generativelanguage.googleapis.com/v1beta/openai/


(⚠️ no extra dot after .com)

Use available models:

gemini-1.5-flash (fast, free quota available)

gemini-1.5-pro (higher quality, limited free quota)

Example in code:

model = OpenAIChatCompletionsModel(
    model="gemini-1.5-flash",
    openai_client=external_client,
)

✅ Example Output
English Teacher > how many tenses in grammar?
Final Output: There are 12 basic tenses in English grammar.
