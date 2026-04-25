# AI Research Assistant

A simple Flask web app that generates structured academic research reports using the OpenAI API, LangChain, and Pydantic structured output.

The app asks for:

- A research topic
- Key research questions
- An optional paper timeframe

It then generates a structured report containing:

- 5–10 relevant academic papers
- Key mathematical formulas related to the topic
- Recent research trends
- Raw JSON output for further use

---

## What This Project Is Used For

This project is designed to help with early-stage academic research, thesis planning, literature review preparation, and research topic exploration.

It can be used to quickly generate a structured overview of a technical or academic subject before doing deeper manual research.

Example topics:

- Reinforcement learning for autonomous drones
- Machine learning for medical imaging
- Digital twins in smart manufacturing
- Computer vision for agricultural robotics
- Cybersecurity in IoT networks

---

## Tech Stack

- Python
- Flask
- LangChain
- OpenAI API
- Pydantic
- HTML / CSS
- MathJax for displaying formulas

---

## Project Structure

ai-research-assistant/
│
├── main.py
├── .env
│
├── templates/
│   └── index.html
│
└── static/
    └── styles.css

---

## Requirements

You need Python installed on your machine.

This project uses the OpenAI API, so you also need an OpenAI API key.

Important: ChatGPT Plus and the OpenAI API are billed separately. Having ChatGPT Plus does not automatically give API credits.

---

## Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/ai-research-assistant.git

Move into the project folder:

cd ai-research-assistant

Create a virtual environment:

python -m venv venv

Activate the virtual environment.

On Windows:

venv\Scripts\activate

On Mac/Linux:

source venv/bin/activate

Install the required Python libraries:

python -m pip install flask python-dotenv pydantic langchain langchain-openai

---

## Environment Variables

Create a `.env` file in the root of the project:

OPENAI_API_KEY=your_openai_api_key_here

Replace `your_openai_api_key_here` with your real OpenAI API key.

Do not upload your `.env` file to GitHub.

---

## Running the App

Start the Flask app:

python main.py

Then open your browser and go to:

http://127.0.0.1:5000

---

## How To Use

1. Enter the topic of your paper, thesis, or research project.
2. Enter your key research questions.
3. Optionally enter a timeframe for the papers, such as `2020-2025`.
4. Click **Generate Report**.
5. Review the generated papers, formulas, trends, and raw JSON output.

---

## API Route

The app also includes a JSON API endpoint:

POST /api/report

Example JSON body:

{
  "topic": "Reinforcement learning for autonomous drones",
  "questions": "How can reinforcement learning improve navigation in GPS-denied environments?",
  "timeframe": "2020-2025"
}

The API returns a structured JSON report.

---

## Notes

This app is intended as a research assistant, not a replacement for manual academic research.

The generated paper list, formulas, and trends should be checked against real academic databases such as:

- Google Scholar
- IEEE Xplore
- ACM Digital Library
- ScienceDirect
- SpringerLink
- arXiv

Always verify citations, paper details, formulas, and sources before using the output in academic work.

---

## Common Errors

### ModuleNotFoundError: No module named 'dotenv'

Install the missing package:

python -m pip install python-dotenv

### 429 insufficient_quota

This means the OpenAI API account does not currently have available billing quota or credits.

Fix it by checking your OpenAI API billing settings and making sure the API key belongs to a funded project.

---

## Future Improvements

Possible future additions:

- Export report to PDF
- Export report to Word document
- Save generated reports
- Add real academic database search
- Add citation formatting such as APA, IEEE, or Harvard
- Add user authentication
- Deploy online using Render, Railway, or Vercel

---

## License

This project is for educational and research-assistance purposes.
