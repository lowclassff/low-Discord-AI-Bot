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

## 📌 1. Install Python

Check if Python is installed:

bash

```python3 --version```

🖥️ Windows
Download from Python.org

During installation, check “Add to PATH”

📱 Termux (Android)
bash
Copy code

```pkg update -y && pkg upgrade -y
pkg install python -y
pkg install git -y```

🐧 Linux (Debian/Ubuntu)
bash
Copy code

```sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-distutils -y```

👉 If you need Python upgrade (for Google GenAI support):

bash
Copy code

```sudo apt install python3.11 python3.11-venv python3.11-distutils -y```

📌 2. Clone Repository
bash
Copy code

```git clone https://github.com/HandsomeBhai/Aayush-Discord-AI-Bot
cd Aayush-Discord-AI-Bot```

📌 3. Install Requirements
Upgrade pip (important!):

bash
Copy code

```pip install --upgrade pip setuptools wheel```

Install dependencies:

bash
Copy code

```python -m pip install --upgrade pip```

```python3.11 --version
python3.11 -m venv venv
source venv/bin/activate
python --version  # should now show 3.11 inside the venv
pip install --upgrade pip```

```pip install -r requirements.txt```

📌 4. Create a Discord Bot
Go to Discord Developer Portal

Create New Application → Add Bot

Enable Message Content Intent

Copy the Bot Token

📌 5. Invite Bot to Your Server
In Developer Portal → OAuth2 → URL Generator

Select Bot and permissions:

✅ Read Messages

✅ Send Messages

✅ Use Slash Commands

Copy the URL → Open in browser → Invite bot to your server

📌 6. Set Your API Key
Get your OpenAI API key from platform.openai.com/api-keys.

Linux / macOS / Termux

```https://platform.openai.com/api-keys```

bash
Copy code

```export OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXX"```

Windows PowerShell
powershell
Copy code

```setx OPENAI_API_KEY "sk-XXXXXXXXXXXXXXXX"```

Render (Hosting)
Environment Variables → Add:

```OPENAI_API_KEY = sk-XXXXXXXXXXXXXXXX```

📌 7. Get Discord Channel ID
Discord → Settings → Advanced → Enable Developer Mode

Right-click channel → Copy Channel ID

📌 8. Run the Bot
bash
Copy code

```python bot.py```
Enter when prompted:

Your Discord Bot Token

Your Channel ID

📌 9. Keep Bot Running 24/7 (Linux / VPS / Termux)
Option A: tmux
bash
Copy code
tmux new -s aayushbot
python bot.py
Detach: CTRL + B then D

Reattach: tmux attach -t aayushbot

Option B: screen
bash
Copy code
screen -S aayushbot
python bot.py
Detach: CTRL + A then D

Reattach: screen -r aayushbot

📌 🔟 Deploy on Render (Free Hosting)
Build Command

bash
Copy code
pip install -r requirements.txt
Start Command

bash
Copy code
python bot.py
Environment Variables

ini
Copy code
OPENAI_API_KEY = sk-XXXXXXXXXXXXXXXX
CHANNEL_ID = 123456789012345678
📌 1️⃣1️⃣ Update Bot
bash
Copy code
git pull origin main
pip install -r requirements.txt --upgrade
python bot.py
🛠️ Useful Commands & Tips
Upgrade pip

bash
Copy code
pip install --upgrade pip
Upgrade all packages

bash
Copy code
pip list --outdated
pip install -U $(pip list --outdated | awk 'NR>2 {print $1}')
Upgrade Python on Debian/Ubuntu

bash
Copy code
sudo apt update
sudo apt install python3.11 python3.11-venv python3.11-distutils -y
Run inside virtual environment (recommended)

bash
Copy code
python3.11 -m venv venv
source venv/bin/activate
Deactivate venv:

bash
Copy code
deactivate
✅ Done!
Your bot should now be online 🎉
