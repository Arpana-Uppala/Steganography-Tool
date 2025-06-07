import tkinter as tk
from tkinter import filedialog, ttk
from stegano import (
    encode_lsb, decode_lsb,
    encode_image_in_image, decode_image_from_image,
    encode_audio, decode_audio
)

root = tk.Tk()
root.title("Steganography Tool")
root.geometry("600x500")

# Dynamic input area
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", wraplength=500, justify="left")
result_label.pack(pady=10)

# Dropdowns
stego_type_var = tk.StringVar()
action_var = tk.StringVar()

stego_options = [
    "Image to Text",
    "Image to Image",
    "Audio to Text"
]

action_options = ["Encode", "Decode"]

def clear_input_frame():
    for widget in input_frame.winfo_children():
        widget.destroy()

def browse_file(entry_widget, filetypes):
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, file_path)

def perform_operation():
    result_label.config(text="")
    stego_type = stego_type_var.get()
    action = action_var.get()

    if stego_type == "Image to Text" and action == "Encode":
        image = entries['image'].get()
        message = entries['message'].get()
        password = entries['password'].get()
        if not image or not message:
            result_label.config(text="Image and Message required.")
            return
        encode_lsb(image, message, password or '', "secure_output.png")
        result_label.config(text="Message encoded in 'secure_output.png'.")

    elif stego_type == "Image to Text" and action == "Decode":
        image = entries['image'].get()
        password = entries['password'].get()
        if not image:
            result_label.config(text="Image required.")
            return
        result = decode_lsb(image, password or '')
        result_label.config(text=f"Decoded Message:\n\n**{result}**", font=("Arial", 10, "bold"))

    elif stego_type == "Image to Image" and action == "Encode":
        cover = entries['cover_image'].get()
        secret = entries['secret_image'].get()
        if not cover or not secret:
            result_label.config(text="Both images required.")
            return
        encode_image_in_image(cover, secret, "image_stego_output.png")
        result_label.config(text="Secret image hidden in 'image_stego_output.png'")

    elif stego_type == "Image to Image" and action == "Decode":
        cover = entries['cover_image'].get()
        try:
            decode_image_from_image(cover, (100, 100), "extracted_secret.png")
            result_label.config(text="Secret image extracted to 'extracted_secret.png'")
        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

    elif stego_type == "Audio to Text" and action == "Encode":
        audio = entries['audio'].get()
        message = entries['message'].get()
        if not audio or not message:
            result_label.config(text="Audio and Message required.")
            return
        encode_audio(audio, message, "audio_output.wav")
        result_label.config(text="Message hidden in 'audio_output.wav'")

    elif stego_type == "Audio to Text" and action == "Decode":
        audio = entries['audio'].get()
        if not audio:
            result_label.config(text="Audio file required.")
            return
        result = decode_audio(audio)
        result_label.config(text=f"Decoded Message:\n\n**{result}**", font=("Arial", 10, "bold"))

entries = {}

def update_inputs(*args):
    clear_input_frame()
    entries.clear()

    stype = stego_type_var.get()
    act = action_var.get()

    if stype == "Image to Text":
        tk.Label(input_frame, text="Image Path:").pack()
        entries['image'] = tk.Entry(input_frame, width=50)
        entries['image'].pack()
        tk.Button(input_frame, text="Browse", command=lambda: browse_file(entries['image'], [("Images", "*.png *.bmp")])).pack()

        if act == "Encode":
            tk.Label(input_frame, text="Secret Message:").pack()
            entries['message'] = tk.Entry(input_frame, width=50)
            entries['message'].pack()

        tk.Label(input_frame, text="Password (optional):").pack()
        entries['password'] = tk.Entry(input_frame, width=50, show="*")
        entries['password'].pack()

    elif stype == "Image to Image":
        tk.Label(input_frame, text="Cover Image Path:").pack()
        entries['cover_image'] = tk.Entry(input_frame, width=50)
        entries['cover_image'].pack()
        tk.Button(input_frame, text="Browse Cover", command=lambda: browse_file(entries['cover_image'], [("Images", "*.png *.bmp")])).pack()

        if act == "Encode":
            tk.Label(input_frame, text="Secret Image Path:").pack()
            entries['secret_image'] = tk.Entry(input_frame, width=50)
            entries['secret_image'].pack()
            tk.Button(input_frame, text="Browse Secret", command=lambda: browse_file(entries['secret_image'], [("Images", "*.png *.bmp")])).pack()

    elif stype == "Audio to Text":
        tk.Label(input_frame, text="Audio File Path:").pack()
        entries['audio'] = tk.Entry(input_frame, width=50)
        entries['audio'].pack()
        tk.Button(input_frame, text="Browse", command=lambda: browse_file(entries['audio'], [("WAV Audio", "*.wav")])).pack()

        if act == "Encode":
            tk.Label(input_frame, text="Secret Message:").pack()
            entries['message'] = tk.Entry(input_frame, width=50)
            entries['message'].pack()

stego_type_menu = ttk.Combobox(root, textvariable=stego_type_var, values=stego_options, state='readonly')
stego_type_menu.set("Select Steganography Type")
stego_type_menu.pack(pady=5)

action_menu = ttk.Combobox(root, textvariable=action_var, values=action_options, state='readonly')
action_menu.set("Select Action")
action_menu.pack(pady=5)

stego_type_var.trace("w", update_inputs)
action_var.trace("w", update_inputs)

tk.Button(root, text="Perform Operation", command=perform_operation).pack(pady=10)

root.mainloop()