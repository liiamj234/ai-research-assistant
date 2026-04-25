import json

from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from pydantic import BaseModel, Field
from langchain.chat_models import init_chat_model

load_dotenv()

app = Flask(__name__)


class Paper(BaseModel):
    title: str
    authors: list[str]
    year: int
    venue: str | None = None
    url: str | None = None
    relevance: str = Field(
        description="Why this paper is relevant to the topic or research questions."
    )


class Formula(BaseModel):
    name: str
    latex: str = Field(
        description="LaTeX source for the formula, no surrounding delimiters."
    )
    description: str
    reference: str | None = Field(
        default=None,
        description="Paper, textbook or source where the formula comes from."
    )


class Trend(BaseModel):
    title: str
    description: str
    references: list[str] = Field(
        default_factory=list,
        description="Titles or URLs of papers backing this trend."
    )


class Report(BaseModel):
    topic: str
    research_questions: list[str]
    time_frame: str | None = None
    papers: list[Paper] = Field(description="5 to 10 most relevant papers.")
    formulas: list[Formula]
    trends: list[Trend]


def generate_report(topic: str, questions: str, timeframe: str | None) -> Report:
    task = f"""Topic: {topic}
Research questions: {questions}
Time frame: {timeframe or 'no specific focus'}

Gather 5-10 highly relevant papers.
Then identify the most important mathematical formulas for this subject and recent trends.
Populate the Report schema fully."""

    model = init_chat_model("openai:gpt-5").with_structured_output(Report)

    result = model.invoke(
        [
            {
                "role": "system",
                "content": "You are a thorough IT research assistant helping write academic papers and theses.",
            },
            {
                "role": "user",
                "content": task,
            },
        ]
    )

    return result


@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    error = None
    raw_json = None

    if request.method == "POST":
        topic = request.form.get("topic", "").strip()
        questions = request.form.get("questions", "").strip()
        timeframe = request.form.get("timeframe", "").strip()

        if not topic:
            error = "Please enter a topic."
        elif not questions:
            error = "Please enter at least one research question."
        else:
            try:
                report = generate_report(topic, questions, timeframe)
                raw_json = json.dumps(report.model_dump(), indent=2)
            except Exception as e:
                error = str(e)

    return render_template(
        "index.html",
        report=report,
        error=error,
        raw_json=raw_json,
    )


@app.route("/api/report", methods=["POST"])
def api_report():
    data = request.get_json(force=True)

    topic = data.get("topic", "").strip()
    questions = data.get("questions", "").strip()
    timeframe = data.get("timeframe", "").strip()

    if not topic or not questions:
        return jsonify({"error": "Topic and research questions are required."}), 400

    try:
        report = generate_report(topic, questions, timeframe)
        return jsonify(report.model_dump())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)