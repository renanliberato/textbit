# Textbit 🚀
Turn your words into clear, concise masterpieces instantly. Hate clunky sentences and jargon? Textbit uses affordable AI to rewrite your content in active voice, shorter form, and simple words. It works great for emails, docs, and quick edits.

https://github.com/user-attachments/assets/0fa7176b-5b3c-4344-a3a3-d466faebd0df

## ✨ Why You'll Love It
- **Crystal Clear**: Removes passive voice and complexity
- **Lightning Fast**: Rephrases instantly with AI
- **Interactive CLI**: Simple terminal interface for experts
- **Mac Notifications**: Alerts you when your text transforms

## 🚀 Quick Start

1. **Install**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up API Key**:
   Create a `.env` file:
   ```
   OPENROUTER_API_KEY=sk-or-your-openrouter-api-key
   ```
   Get a free key from [openrouter.ai](https://openrouter.ai)

3. **Run it**:
   ```bash
   python app.py
   ```

   Or use the CLI script for automatic venv setup:
   ```bash
   ./bin/textbit
   ```

Enter text, press rephrase, and see the result. Type 'quit' to exit.

## 🛠️ CLI Script Setup

1. Add to PATH:
   ```bash
   export PATH="$PATH:$(pwd)/bin"
   ```
   Add this line to your `~/.zshrc` or `~/.bash_profile` to make it permanent.

2. Or create a symlink for system-wide access:
   ```bash
   sudo ln -s $(pwd)/bin/textbit /usr/local/bin/textbit
   ```

Now run `textbit` from any directory. It handles the venv automatically.

## 🔧 Requirements
- Python 3.8 or later
- [OpenRouter API key](https://openrouter.ai) (free tier available)
- macOS for notifications (optional)

## 🤝 Contributing
Enjoy the app? Fork it, improve the prompt, or add features. Pull requests welcome.

## 📄 License
MIT. Use it freely, but keep the magic alive.
