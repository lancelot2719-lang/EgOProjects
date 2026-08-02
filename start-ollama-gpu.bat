@echo off
chcp 65001 >nul
title Ollama (Vulkan - AMD GPU)

REM If VRAM error, uncomment next line:
REM set OLLAMA_VULKAN=0

set OLLAMA_MODELS=D:\AI_Project\ollama

echo Stopping Ollama service...
net stop ollama 2>nul
sc config ollama start=disabled 2>nul

echo Starting Ollama with AMD GPU...
start /min /b "" "C:\Users\x2\AppData\Local\Programs\Ollama\ollama.exe" serve
