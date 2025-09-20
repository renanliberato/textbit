#!/usr/bin/env python3

import sys
import os
import json
from subprocess import run, PIPE
import requests
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

load_dotenv()

OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")  # Set this env var

if not OPENROUTER_API_KEY:
    print("Error: OPENROUTER_API_KEY environment variable not set.", file=sys.stderr)
    sys.exit(1)

MODEL = "google/gemini-flash-1.5-8b"

PROMPT_TEMPLATE = """You are a highly skilled technical writer tasked with rephrasing the following text to make it clear, concise, and easy to read, following these four rules:

1. **Avoid passive voice**: Use active voice. Identify clear subjects and actions, avoiding forms of the verb "to be" (e.g., is, was, are) where possible.
2. **Be concise**: Eliminate unnecessary words to compress the text while retaining its full meaning. Aim for brevity and clarity, maximizing information density.
3. **Avoid technical jargon**: Replace complex or technical terms with simple, accessible language that a general audience can understand on the first read.
4. **Rewrite for clarity**: Refine the text to ensure it is straightforward, removing ambiguity and simplifying complex ideas without losing substance.

**Input Text**:  
{input_text}

**Instructions**:  
- Rephrase the input text to adhere to the four rules above.  
- Ensure the rephrased text is clear, direct, and easy to understand for a broad audience.  
- Maintain the original meaning and intent of the text.  
- If the input contains technical terms, replace them with simpler alternatives or brief explanations.  
- Output only the rephrased text, without additional commentary or explanations."""

def send_to_llm(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "",  # Optional: your app's website
        "X-Title": "Textbit",  # Optional: your app's name
    }
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,  # Low for consistency
    }
    try:
        response = requests.post(OPENROUTER_API_URL, headers=headers, json=data, timeout=30)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            print(f"Error: {response.status_code} - {response.text}", file=sys.stderr)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}", file=sys.stderr)
        return None

def clear_screen():
    os.system('clear')

def copy_to_clipboard(text):
    if sys.platform == 'darwin':
        run(['pbcopy'], input=text, text=True)
    elif sys.platform == 'win32':
        run(['clip'], input=text, text=True)
    else:
        print("Clipboard copy not supported on this platform.")

def main():
    console = Console()
    console.print("[bold magenta]Welcome to Textbit - Text Rephraser![/bold magenta]\n")
    while True:
        console.print("[bold blue]Enter text to rephrase (or 'quit' to exit):[/bold blue]")
        input_text = input().strip()
        if input_text.lower() == 'quit':
            break
        if not input_text:
            continue
        with Progress(SpinnerColumn(), TextColumn("[bold green]Rephrasing...[/bold green]"), console=console) as progress:
            task = progress.add_task("", total=None)
            prompt = PROMPT_TEMPLATE.format(input_text=input_text)
            rephrased = send_to_llm(prompt)
            progress.update(task, completed=True)
        if rephrased:
            panel = Panel(rephrased, title="[bold green]Rephrased Text[/bold green]", border_style="green")
            console.print(panel)
            input("\nPress Enter to copy to clipboard and continue...")
            copy_to_clipboard(rephrased)
            console.clear()
        else:
            console.print("[bold red]Error rephrasing.[/bold red]")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
