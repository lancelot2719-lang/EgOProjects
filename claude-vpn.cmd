@echo off
chcp 65001 >nul
cd /d D:\AI_Project
powershell -ExecutionPolicy Bypass -NoProfile -File "D:\AI_Project\tech\claude-vpn-launcher.ps1"
