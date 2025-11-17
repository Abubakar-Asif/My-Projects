# Jarvis Bot -- Python Virtual Assistant

Jarvis Bot is a Python-powered virtual assistant capable of performing
web automation, smart searches, and AI-driven conversation. It
integrates with the DeepSeek model through the OpenRouter API, offering
fast and intelligent replies. Jarvis includes text-to-speech
capabilities and supports simple text commands for easy interaction.

## About Me

My name is Abubakar Asif. I am a Python developer who enjoys creating
automation tools, AI assistants, and practical programming projects. I
am passionate about learning data science, cybersecurity, and building
intelligent applications. Jarvis Bot reflects my interest in Python
automation and AI integration.

## Features

### 1. Voice Output

-   Uses pyttsx3 for offline text-to-speech.
-   Speaks all commands, confirmations, and AI responses.

### 2. Web Automation

Jarvis can automatically open: - Google - YouTube - Instagram -
Facebook - News sites

### 3. Smart Search

Supports direct platform-based search: - Google search - YouTube
search - Facebook search - Instagram tag search - News search

### 4. AI Chat Support (DeepSeek via OpenRouter)

-   Uses DeepSeek model:
    -   deepseek/deepseek-r1-0528-qwen3-8b:free
-   Generates short, clear, intelligent responses.
-   Replies are spoken aloud using pyttsx3.

### 5. API Key Handling

-   Saves API key in jarvis_ai_api.txt.
-   Auto-loads the key.
-   Prompts for key if missing.

### 6. Command System

Supports: - Web commands - Search commands - AI queries - Exit commands

## Requirements

Install dependencies:

    pip install requests pyttsx3

Use Python 3.8 or higher.

## How to Use the AI Feature

### 1. Get an OpenRouter API Key

Create a free account at: https://openrouter.ai/

### 2. Generate API Key

-   Open Dashboard\
-   Go to API Keys\
-   Click Create Key\
-   Copy the key

### 3. Add Your API Key to Jarvis

On first run :

    Do you have API key (Y/N) :

Enter :

    y

Then paste your key :

    Enter your OpenRouter API key :

Jarvis saves it to :

    jarvis_ai_api.txt

### 4. Using AI Queries

Any text that is not a command becomes an AI question.

Example :

    Explain gravity.

Jarvis: - Sends it to DeepSeek - Prints the answer - Speaks the answer

## How to Run the Project

Clone the repository :

    git clone https://github.com/yourusername/jarvis-bot

Navigate :

    cd jarvis-bot

Run :

    python jarvis.py

Activate :

    jarvis

## Project Structure

    jarvis-bot/
    │
    ├── jarvis.py
    ├── jarvis_ai_api.txt
    └── README.md

## Example Commands

### Web

open google\
open youtube\
open instagram\
open facebook\
open news

### Search

open google and search python\
open youtube and search gym motivation\
open instagram and search travel

### AI

Explain quantum computing.\
Who is Albert Einstein ?\
Write a short summary of Marvels superheros.

### Exit

exit

## Future Enhancements

-   Make it GUI based jarvis bot.
-   Add system operations (shutdown, restart)
-   Add memory-based AI mode
-   Add more integrations
