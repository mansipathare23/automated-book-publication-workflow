from ai_modules.writer import spin_text

# Use full relative path to outputs folder
input_path = "outputs/chapter1.txt"
output_path = "outputs/chapter1_rewritten.txt"

# Load input
with open(input_path, "r", encoding="utf-8") as f:
    input_text = f.read()

# Rewrite using Gemini
rewritten_text = spin_text(input_text)

# Save output
with open(output_path, "w", encoding="utf-8") as f:
    f.write(rewritten_text)

print("✅ Rewritten chapter saved as 'outputs/chapter1_rewritten.txt'")
