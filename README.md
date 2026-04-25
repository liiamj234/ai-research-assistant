# AI Research Assistant

AI Research Assistant is a Flask web application that generates structured academic research reports using the OpenAI API, LangChain, and Pydantic.

The application takes a research topic, key research questions, and an optional timeframe, then returns a structured report containing relevant academic papers, mathematical formulas, research trends, and raw JSON output.

---

## Purpose

This project is designed to support early-stage academic research, thesis planning, literature review preparation, and technical topic exploration.

It helps turn a broad research idea into a structured starting point by generating:

- Relevant papers
- Key formulas
- Research trends
- Source links where available
- Structured JSON output for reuse

This is useful for quickly exploring a subject before moving into deeper manual research using academic databases.

---

## Features

- Web-based research report generator
- Flask backend
- Clean HTML and CSS interface
- OpenAI-powered structured output
- Pydantic schema validation
- MathJax support for displaying LaTeX formulas
- JSON API endpoint
- Raw JSON output for further processing

---

## Tech Stack

- Python
- Flask
- LangChain
- OpenAI API
- Pydantic
- HTML
- CSS
- MathJax

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

Python must be installed on the machine running the project.

This project also requires an OpenAI API key.

OpenAI API usage is billed separately from a ChatGPT subscription. A ChatGPT Plus subscription does not automatically provide OpenAI API credits.

---

## Installation

Move into the project directory:

    cd ai-research-assistant

Create a virtual environment:

    python -m venv venv

Activate the virtual environment on Windows:

    venv\Scripts\activate

Activate the virtual environment on macOS or Linux:

    source venv/bin/activate

Install the required Python packages:

    python -m pip install flask python-dotenv pydantic langchain langchain-openai

---

## Environment Variables

Create a `.env` file in the root directory of the project.

The application expects the following environment variable:

    OPENAI_API_KEY

The `.env` file should not be committed to GitHub.

A `.gitignore` file should include:

    .env
    venv/
    __pycache__/

---

## Running the Application

Start the Flask app:

    python main.py

Open the local development server in a browser:

    http://127.0.0.1:5000

---

## How to Use

1. Enter a research topic.
2. Enter one or more key research questions.
3. Optionally enter a timeframe for the papers.
4. Click Generate Report.
5. Review the generated report.
6. Use the raw JSON output for further processing, exporting, or integration.

---

## Example Topics

- Reinforcement learning for autonomous drones
- Machine learning for medical imaging
- Computer vision for agricultural robotics
- Digital twins in smart manufacturing
- Cybersecurity in IoT networks
- AI-assisted engineering design
- Robotics for precision agriculture

---

## API Endpoint

The application includes a JSON API endpoint:

    POST /api/report

Expected JSON fields:

    {
      "topic": "Reinforcement learning for autonomous drones",
      "questions": "How can reinforcement learning improve navigation in GPS-denied environments?",
      "timeframe": "2020-2025"
    }

The endpoint returns a structured JSON research report.

---

## Output Structure

The generated report includes:

- Topic
- Research questions
- Timeframe
- Relevant papers
- Important formulas
- Recent trends

Each paper includes:

- Title
- Authors
- Year
- Venue
- URL where available
- Relevance to the research topic

Each formula includes:

- Name
- LaTeX source
- Description
- Reference where available

Each trend includes:

- Title
- Description
- Supporting references

---

## Important Notes

This application is a research assistant, not a replacement for proper academic verification.

Generated results should be checked against trusted academic sources before being used in formal work.

Recommended sources for verification include:

- Google Scholar
- IEEE Xplore
- ACM Digital Library
- ScienceDirect
- SpringerLink
- arXiv

Citations, formulas, paper metadata, and source links should always be manually verified before use in academic writing.

---

## Common Errors

### ModuleNotFoundError: No module named 'dotenv'

Install the missing package:

    python -m pip install python-dotenv

### 429 insufficient_quota

This means the OpenAI API account does not currently have available billing quota or credits.

To resolve this, check the OpenAI API billing settings and confirm that the API key belongs to a project with available usage.

---

## Future Improvements

Planned or possible future improvements include:

- Export reports to PDF
- Export reports to Word documents
- Save generated reports
- Add citation formatting
- Add APA, IEEE, and Harvard reference styles
- Add real academic database search
- Add user authentication
- Add report history
- Deploy the application online

---

## License

This project is for educational, research-assistance, and portfolio demonstration purposes.
