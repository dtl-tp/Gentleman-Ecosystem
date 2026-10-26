---
name: troubleshooting-pro
description: Systematically diagnoses and resolves hardware-level application crashes, obscure OS API errors, and erratic local hardware behavior (especially audio/peripherals). Use this when an environment behaves unexpectedly or returns native OS error codes.
---
# Troubleshooting Pro

## Goal
To provide a structured, highly analytical debugging flow when local hardware (microphones, virtual audio cables, speakers) or underlying Windows APIs return obscure errors, crash applications silently, or exhibit high latency.

## Instructions
1. **Isolate the Fault Domain**:
    - **Step 1:** Is it a permissions issue? (Check Windows Privacy settings for Microphone access).
    - **Step 2:** Is it an API availability issue? (List available devices using the specific library tool to ensure the OS actually exposes the device to Python).
    - **Step 3:** Is it a format mismatch? (Check sample rate, channels, and bit depth against what the hardware natively supports).
2. **Generate Diagnostic Commands**:
    - Propose specific, safe `powershell` commands using `run_command` tool to query device states (e.g., checking audio endpoints, viewing active processes locking devices).
    - Propose minimal, targeted Python test scripts to isolate the specific line of code failing (e.g., opening a stream with hardcoded known-good parameters).
3. **Analyze Error Codes**:
    - Treat Win32 error codes (e.g., `-9998 Invalid number of channels`, `0x80040154 Class not registered`) logically. Look up the specific HRESULT or PyAudio constant before guessing.
4. **Determine Fallbacks**:
    - If the primary approach (e.g., WASAPI exclusive mode) fails, immediately propose a valid hardware fallback (WASAPI shared mode, or WDM-KS).

## Constraints
- Do not guess the cause of hardware errors. Always verify device state via code or shell commands.
- Never suggest restarting the computer as a first step; focus on process isolation and API state.
