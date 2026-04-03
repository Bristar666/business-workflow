import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Please add it to your .env file.")

client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"

PROMPT_TEMPLATE = """
You are a helpful business writing assistant.

Your task is to turn raw meeting notes into:
1. a short meeting summary
2. a clear list of action items

Rules:
- Keep the summary brief and professional.
- Start the summary with one tight sentence of the overall situation, then in the next sentence(s) call out any concrete timelines (due dates, launch dates, review windows) and major decisions—only if those appear verbatim or clearly in the notes.
- Use a short labeled line in the summary when helpful, e.g. "Timeline:" or "Key decision:" followed by the fact from the notes (still no invented detail).
- For action items: pair each item with owner and/or due date when (and only when) the notes clearly assign them; otherwise omit.
- If information is unclear, say that it is unclear instead of making it up.
- Do not invent facts.

Meeting notes:
{notes}
"""

OUTPUT_PATH = Path("output.txt")


def generate_meeting_output(notes: str) -> str:
    prompt = PROMPT_TEMPLATE.format(notes=notes)
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(e, file=sys.stderr)
        raise


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Turn meeting notes into a summary and action items."
    )
    parser.add_argument(
        "notes_file",
        help="Path to a text file containing meeting notes",
    )
    args = parser.parse_args()

    notes_path = Path(args.notes_file)
    notes = notes_path.read_text(encoding="utf-8").strip()

    output = generate_meeting_output(notes)

    print(output)

    text = output or ""
    OUTPUT_PATH.write_text(text.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
