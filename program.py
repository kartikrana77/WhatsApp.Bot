import pyautogui
import pyperclip
import time
import ollama
import re

# =========================
# CHECK LAST MESSAGE SENDER
# =========================

def is_last_message_from_sender(chat_log, sender_name="Basanti 🎠"):

    lines = [line.strip() for line in chat_log.split("\n") if line.strip()]

    # Traverse backwards
    for line in reversed(lines):

        # Find actual WhatsApp message line
        if "]" in line and ":" in line:

            return sender_name.lower() in line.lower()

    return False
# =========================
# AI SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """
You are Kartik chatting on WhatsApp.

Style:
- Casual Indian boy
- Hinglish
- Short replies
- Natural texting
- Sometimes slang
- No formal Hindi
- No AI behavior
- No emojis unless necessary
- No overexplaining
- No asking weird questions
- No assistant tone
- Reply like a real friend

IMPORTANT:
Reply ONLY to the last message from the OTHER person.
"""

# =========================
# CLEAN CHAT
# =========================

def clean_chat(chat):

    lines = chat.split("\n")

    cleaned = []

    for line in lines:

        # Remove timestamps
        line = re.sub(r"\[.*?\]\s*", "", line)

        if ":" in line:

            name, msg = line.split(":", 1)

            name = name.strip().lower()
            msg = msg.strip()

            # Your messages
            if name == "kartik":
                cleaned.append(f"You: {msg}")

            # Other person
            else:
                cleaned.append(f"Friend: {msg}")

    return "\n".join(cleaned[-12:])

# =========================
# ASK AI
# =========================

def ask_ai(chat):

    cleaned_chat = clean_chat(chat)

    prompt = f"""
Conversation:

{cleaned_chat}

Reply as Kartik to the LAST Friend message only.
"""

    response = ollama.chat(
        model='qwen2.5:7b',
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.7,
            "top_p": 0.9
        }
    )

    return response['message']['content'].strip()

# =========================
# START
# =========================

time.sleep(3)

# Click WhatsApp chat
pyautogui.click(1006, 1058)

time.sleep(1)

while True:

    # Select chat manually
    pyautogui.moveTo(1850, 180)

    pyautogui.dragTo(
        1850,
        970,
        duration=1,
        button='left'
    )

    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')

    time.sleep(0.5)

    pyautogui.click(1669, 931)

    copied_text = pyperclip.paste()

    print(copied_text)

    print(is_last_message_from_sender(copied_text))

    # If last message is from target person
    if is_last_message_from_sender(copied_text):

        question = copied_text

        # Generate AI reply
        reply = ask_ai(question)

        print("AI Reply:", reply)

        # Copy AI reply
        pyperclip.copy(reply)

        time.sleep(0.5)

        # Click message box
        pyautogui.click(781, 993)

        time.sleep(0.5)

        # Paste message
        pyautogui.hotkey('ctrl', 'v')

        time.sleep(0.5)

        # Click send button
        pyautogui.click(1877, 986)

    else:
        print("Last message not from target person")

    time.sleep(5)