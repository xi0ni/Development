import asyncio
import tkinter as tk
from threading import Thread
from datetime import datetime
from io import BytesIO
import requests
from PIL import Image, ImageTk
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import torch

# ========== SETUP ==========
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[INFO] Using device: {DEVICE}")

# Load a pre-trained Stable Diffusion model
print("[INFO] Loading AI model...")
sd_pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32
).to(DEVICE)

# Load a summarization model for trending topics
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ========== ASYNC UTILS ==========
async def get_trending_topic():
    """Fetches trending topic from a public API."""
    try:
        res = requests.get("https://api.currentsapi.services/v1/latest-news",
                           params={"apiKey": "demo"}).json()
        headline = res["news"][0]["title"]
        summary = summarizer(headline, max_length=12, min_length=5, do_sample=False)[0]["summary_text"]
        return summary
    except Exception as e:
        return f"AI Abstract Concept {datetime.now().strftime('%H:%M:%S')}"

async def generate_image(prompt, style="Van Gogh"):
    """Generates an AI image based on prompt and style."""
    full_prompt = f"{prompt}, in the style of {style}, surreal and cinematic"
    print(f"[GEN] {full_prompt}")
    image = sd_pipe(full_prompt).images[0]
    return image

# ========== GUI ==========
class AIArtApp:
    def __init__(self, master):
        self.master = master
        master.title("AI Art Generator - Live")
        
        self.prompt_label = tk.Label(master, text="Enter your creative prompt:")
        self.prompt_label.pack()

        self.prompt_entry = tk.Entry(master, width=50)
        self.prompt_entry.pack()

        self.style_label = tk.Label(master, text="Choose style:")
        self.style_label.pack()

        self.style_entry = tk.Entry(master, width=50)
        self.style_entry.insert(0, "Van Gogh")
        self.style_entry.pack()

        self.generate_button = tk.Button(master, text="Generate!", command=self.start_generation)
        self.generate_button.pack()

        self.image_label = tk.Label(master)
        self.image_label.pack()

    def start_generation(self):
        Thread(target=self.run_generation).start()

    def run_generation(self):
        prompt = self.prompt_entry.get()
        style = self.style_entry.get()
        if not prompt:
            prompt = asyncio.run(get_trending_topic())
        image = asyncio.run(generate_image(prompt, style))
        self.show_image(image)

    def show_image(self, img):
        img = img.resize((512, 512))
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk

# ========== MAIN ==========
if __name__ == "__main__":
    root = tk.Tk()
    app = AIArtApp(root)
    root.mainloop()
