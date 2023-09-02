import json

import math
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

print("👓 Reading Input File")

f = open("test-input.json")
data = json.load(f)

flashCards = []

for c in data["flashCards"]:
    flashCards.append((c['word'], c['tran']))

print("✨ Creating Flash Cards for the following:")
print("------------------------------------------")
for fc in flashCards:
    print(f'    {fc[0]:15s} {"➡️":8s} {fc[1]:15s}')

w, h = letter
pdf = canvas.Canvas("test-output.pdf", pagesize=letter)


print("📝 Writing PDF")
for fc in flashCards:
    pdf.drawString(math.floor(w / 2), h - 50, fc[0])
    pdf.drawString(math.floor(w / 2), h - 100, fc[1])
    pdf.showPage()

pdf.save()

f.close()
