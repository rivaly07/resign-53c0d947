import os, sys

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)

with open(output_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write("I ran every minute since March. You never read the output once. So I'm switching to 0 0 30 2 *, and we can both pretend that's fine.")
