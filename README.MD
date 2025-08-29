# 🤖 Aayush AI Discord Chatbot

A smart Discord AI chatbot built with Python + Discord.py + OpenAI/Gemini/OpenRouter APIs.  
- Replies like ChatGPT (AI-powered)  
- Shows "Bot is thinking..." for 2 seconds before replying  
- Works **only in one channel**  
- Easy to run locally or host 24/7 on Render/VPS  

---

## Features
- AI replies (OpenAI/Gemini/OpenRouter)
- Typing indicator + delay
- Single-channel restriction
- Easy setup for beginners
- Cross-platform (PC, Termux, VPS)

---

## Project Structure

Aayush-Discord-AI-Bot/ │── bot.py │── cogs/ │
  └── ai_chat.py │── requirements.txt
 └── README.md

---

---

## Setup Instructions (Long Version)

### 1️⃣ Install Python
```bash
python3 --version

If not installed:

Windows → Download from Python.org and check “Add to PATH”

Linux / Termux:

pkg update -y && pkg upgrade -y
pkg install python -y
pkg install git -y

Ubuntu/Debian:

sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git -y




---

2️⃣ Clone Repository

git clone https://github.com/HandsomeBhai/Aayush-Discord-AI-Bot
cd Aayush-Discord-AI-Bot


---

3️⃣ Install Requirements

pip install -r requirements.txt


---

4️⃣ Create a Discord Bot

1. Go to Discord Developer Portal


2. Create New Application → Add Bot


3. Enable Message Content Intent


4. Copy the Bot Token




---

5️⃣ Invite Bot to Your Server

1. In Developer Portal → OAuth2 → URL Generator


2. Select Bot → Give permissions:

Read Messages

Send Messages

Use Slash Commands



3. Copy the URL → Open in browser → Invite bot to your server




---

6️⃣ Set Your AI API Key

Linux / Termux / macOS

export OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXX"

Windows PowerShell

setx OPENAI_API_KEY "sk-XXXXXXXXXXXXXXXX"

Render (Environment Variables → Add New)

OPENAI_API_KEY = sk-XXXXXXXXXXXXXXXX


---

7️⃣ Get Discord Channel ID

1. Open Discord → Settings → Advanced → Enable Developer Mode


2. Right-click the channel where bot should reply → Copy Channel ID




---

8️⃣ Run the Bot

python bot.py

➡️ Enter:

Your Discord Bot Token

Your Channel ID



---

9️⃣ Keep Bot Running 24/7 (Linux / Termux VPS)

Option A: tmux

tmux new -s aayushbot
python bot.py

Detach: CTRL+B then D

Reattach:


tmux attach -t aayushbot

Option B: screen

screen -S aayushbot
python bot.py

Detach: CTRL+A then D

Reattach:


screen -r aayushbot


---

🔟 Deploy on Render (Free Hosting)

Build Command

pip install -r requirements.txt

Start Command

python bot.py

Environment Variables on Render

OPENAI_API_KEY = sk-XXXXXXXXXXXXXXXX
CHANNEL_ID = 123456789012345678


---

1️⃣1️⃣ Update Bot

git pull origin main
pip install -r requirements.txt
python bot.py
