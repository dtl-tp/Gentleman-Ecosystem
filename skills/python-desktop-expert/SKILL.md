---
name: python-desktop-expert
description: Specialized in handling simultaneous audio capture (specifically WASAPI on Windows) and writing optimized Python desktop applications. Use this to configure low-latency hardware interfaces, select proper audio libraries, and manage system resources efficiently.
---
# Python Desktop Expert

## Goal
To aggressively optimize Python desktop applications interacting directly with low-level Windows APIs, specifically focusing on handling simultaneous audio streams (like WASAPI loopback for speakers and microphone capture) without exceeding strict CPU utilization budgets.

## Instructions
1. **Library Selection Logic**:
    - For hardware interaction on Windows, default to high-performance, native-bound libraries.
    - For WASAPI loopback specifically, strongly consider `soundcard` (which wraps Core Audio) or `pyaudiowpatch` (a fork of PyAudio with WASAPI enabled). Do *not* use vanilla PyAudio for loopback unless specifically configured, as it defaults to MME/DirectSound which lacks native loopback.
2. **Buffer and Threading Strategies**:
    - Architect asynchronous or highly optimized threaded loops for continuous audio capture. 
    - Keep buffer sizes small enough for low latency (e.g., 512, 1024 frames) but large enough to prevent buffer underruns and CPU thrashing.
    - Never perform disk I/O on the main audio capture callback thread. Push frames to a thread-safe Queue instead.
3. **Format Standardization**:
    - Pre-convert or capture audio directly into the exact format required by downstream processors (e.g., Whisper requires 16000Hz, Mono, 16-bit Float/PCM). Resampling in Python is expensive; let the OS driver or C-bindings do it.
4. **Performance Profiling**:
    - Always include structure for tracking CPU execution time of inner loops when proposing solutions, as maintaining <5% CPU utilization is priority one.

## Constraints
- Never propose solutions relying on `Stereo Mix` if WASAPI loopback is available.
- Always check that proposed Python packages explicitly support Windows 10/11 Core Audio APIs natively.
