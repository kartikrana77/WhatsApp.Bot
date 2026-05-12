# WhatsApp AI Auto Reply Bot

A Python-based WhatsApp auto-reply bot using:

* PyAutoGUI
* Pyperclip
* Ollama
* Qwen 2.5 7B

The bot:

* Selects WhatsApp chat text
* Copies chat messages
* Detects if the latest message is from a target person
* Sends the chat to a local AI model
* Generates a human-like reply
* Automatically pastes and sends the reply

---

# Features

* Fully local AI (No API cost)
* Human-like Hinglish replies
* Automatic message detection
* Auto copy/paste/send
* Uses Ollama locally
* WhatsApp Desktop compatible
* Custom personality prompt

---

# Requirements

Install Python packages:

```bash
pip install pyautogui pyperclip ollama
```

Install Ollama:

https://ollama.com

---

# Download AI Model

Run:

```bash
ollama pull qwen2.5:7b
```

Start Ollama server:

```bash
ollama serve
```

---

# How It Works

1. Script opens WhatsApp chat
2. Selects messages using mouse drag
3. Copies chat text
4. Checks who sent the latest message
5. Sends conversation to AI
6. AI generates reply
7. Script pastes reply
8. Script sends message automatically

---

# Important Coordinates

You MUST adjust screen coordinates for your PC.

Current coordinates:

```python
pyautogui.click(1006, 1058)
```

Used for:

* opening chat
* selecting messages
* message input
* send button

Use this to find coordinates:

```python
import pyautogui

while True:
    print(pyautogui.position())
```

Move your mouse to see live X/Y coordinates.

---

# AI Personality

The AI personality is controlled using:

```python
SYSTEM_PROMPT
```

You can customize:

* speaking style
* slang
* emojis
* tone
* personality
* roast mode
* flirting
* formal/informal

---

# Important Warning

This project uses GUI automation.

Do NOT:

* move mouse during execution
* resize WhatsApp window
* change display scaling
* switch tabs while running

Recommended:

* Keep WhatsApp maximized
* Use 100% display scaling

---

# Current Workflow

```text
WhatsApp Chat
      ↓
Copy Chat
      ↓
Detect Last Sender
      ↓
Send To Ollama
      ↓
Generate Reply
      ↓
Paste Reply
      ↓
Send Message
```

---

# Project Structure

```text
project/
│
├── main.py
├── README.md
```

---

# Future Improvements

Possible upgrades:

* OCR-based reading
* Multi-contact support
* Memory per person
* Voice note transcription
* Screenshot parsing
* Auto unread detection
* Typing delay simulation
* AI emotional memory

---

# Disclaimer

This project is for educational purposes only.

Use responsibly and avoid violating WhatsApp policies.
