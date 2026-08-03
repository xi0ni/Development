from PIL import Image, ImageDraw

# Load the provided floor plan image
img_path = "Screenshot 2026-03-04 at 11.13.30 PM copy.png"
img = Image.open(img_path).convert("RGB")
draw = ImageDraw.Draw(img)

# Approximate coordinates for AHUs (green squares) based on visual estimation
ahu1 = (780, 520)
ahu2 = (780, 760)

# Diffuser approximate locations in rooms
living = (950, 300)
study = (1020, 520)
master = (980, 700)
bed2 = (500, 650)
kitchen = (420, 850)
bath = (620, 520)

# Draw supply ducts (purple)
purple = (160, 0, 160)
draw.line([ahu1, living], fill=purple, width=6)
draw.line([ahu1, study], fill=purple, width=6)
draw.line([ahu2, master], fill=purple, width=6)
draw.line([ahu2, bed2], fill=purple, width=6)
draw.line([ahu2, kitchen], fill=purple, width=6)

# Draw return ducts (green)
green = (0, 160, 0)
draw.line([bath, ahu1], fill=green, width=6)
draw.line([master, ahu2], fill=green, width=6)

# Save output
out_path = "newfolder"
img.save(out_path)

out_path
