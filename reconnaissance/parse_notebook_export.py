import os
import json

directory = "/mnt/d/Hermes_context_inbox/Saved-Context/"
files = os.listdir(directory)
print(f"Scanning {len(files)} files in Saved-Context for Orbit Wars or NotebookLM reasoning...")

matches = []
for f in files:
    if "orbit" in f.lower() or "gemini-chat" in f.lower() or "emergent" in f.lower():
        matches.append(f)
        
print("Found matches:", matches[:10])
