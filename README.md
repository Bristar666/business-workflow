# Week 2 - Build and Evaluate a Simple GenAI Workflow

## Business Workflow
This project focuses on turning meeting notes into a short meeting summary and a list of action items.

## User
The target user is a project manager or team lead who needs to quickly review meeting outcomes and assign follow-up work.

## Input
The system receives raw meeting notes. These notes may be messy, incomplete, or written in bullet-point form.

## Output
The system produces:
1. a short summary of the meeting
2. a structured list of action items
3. owners and deadlines when they are clearly mentioned in the notes

## Why this task is valuable
This task is repetitive and time-consuming. A GenAI workflow can help create a first draft quickly, improve consistency, and make follow-up easier after meetings.

## Setup

From the project root, create a virtual environment (optional but recommended) and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root (do not commit it). Add your API key:

```
GEMINI_API_KEY=your_key_here
```

Get a key from Google AI Studio. The app loads this value with `python-dotenv`.

## Run

Provide a path to a text file with meeting notes. Example:

```bash
python app.py sample_notes.txt
```

The script prints the model response to the terminal and saves the same text to `output.txt` in the current working directory.

## Walkthrough video

- **Video:** [Week 2 walkthrough (YouTube)](https://youtu.be/dvJhs8XPJZg)