import tkinter as tk
import random
import time
from PIL import Image, ImageTk
import os
import pygame
from database import save_score

pygame.mixer.init()

GRID_PADDING = 5

def play_sound(filename):
    pygame.mixer.Sound(os.path.join("sounds", filename)).play()

def start_game(username, grid_size, root):
    for widget in root.winfo_children():
        widget.destroy()

    canvas = tk.Canvas(root, bg="#111")
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#111")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    num_pairs = (grid_size * grid_size) // 2
    level_map = {4: 1, 6: 2, 8: 3}
    level = level_map.get(grid_size, 1)

    images = load_images(num_pairs, level)
    images *= 2
    random.shuffle(images)

    revealed = []
    matched = []
    buttons = []
    clicks = [0]
    start_time = [time.time()]

    back_raw = Image.open("images/back.png").resize((70, 70))
    back_img = ImageTk.PhotoImage(back_raw)

    powerups_used = {"reveal": False, "shuffle": False}

    def on_click(i):
        if i in matched or i in revealed or len(revealed) == 2:
            return
        play_sound("click.wav")
        clicks[0] += 1
        buttons[i].config(image=images[i])
        revealed.append(i)
        if len(revealed) == 2:
            root.after(500, check_match)

    def check_match():
        i1, i2 = revealed
        if images[i1] == images[i2]:
            matched.extend([i1, i2])
            play_sound("match.wav")
        else:
            play_sound("fail.wav")
            buttons[i1].config(image=back_img)
            buttons[i2].config(image=back_img)
        revealed.clear()
        if len(matched) == grid_size * grid_size:
            finish_game()

    def finish_game():
        play_sound("win.wav")
        end_time = int(time.time() - start_time[0])
        canvas.destroy()
        scrollbar.destroy()
        save_score(username, grid_size, end_time, clicks[0])
        show_end_screen(username, grid_size, end_time, clicks[0], root)

    def use_reveal_all():
        if powerups_used["reveal"]:
            return
        powerups_used["reveal"] = True
        for i in range(len(images)):
            if i not in matched:
                buttons[i].config(image=images[i])
        root.after(2000, hide_unmatched)
        btn_reveal.config(state="disabled")

    def hide_unmatched():
        for i in range(len(images)):
            if i not in matched and i not in revealed:
                buttons[i].config(image=back_img)

    def use_shuffle():
        if powerups_used["shuffle"]:
            return
        powerups_used["shuffle"] = True
        unmatched_indices = [i for i in range(len(images)) if i not in matched]
        unmatched_images = [images[i] for i in unmatched_indices]
        random.shuffle(unmatched_images)
        for idx, i in enumerate(unmatched_indices):
            images[i] = unmatched_images[idx]
            buttons[i].config(image=back_img)
        revealed.clear()
        btn_shuffle.config(state="disabled")

    for idx in range(grid_size * grid_size):
        btn = tk.Button(scrollable_frame, image=back_img, width=70, height=70,
                        command=lambda i=idx: on_click(i))
        buttons.append(btn)

    for r in range(grid_size):
        for c in range(grid_size):
            idx = r * grid_size + c
            buttons[idx].grid(row=r, column=c, padx=GRID_PADDING, pady=GRID_PADDING)

    powerup_frame = tk.Frame(scrollable_frame, bg="#111")
    powerup_frame.grid(row=grid_size, column=0, columnspan=grid_size)

    global btn_reveal, btn_shuffle
    btn_reveal = tk.Button(powerup_frame, text=" Reveal All", font=("Arial", 10), width=12,
                           command=use_reveal_all, bg="#ffaa00", fg="black")
    btn_reveal.pack(side="left", padx=10, pady=10)

    btn_shuffle = tk.Button(powerup_frame, text=" Shuffle", font=("Arial", 10), width=12,
                            command=use_shuffle, bg="#00ccff", fg="black")
    btn_shuffle.pack(side="left", padx=10, pady=10)

    btn_end = tk.Button(powerup_frame, text="End Game", font=("Arial", 10), width=12,
                        command=root.quit, bg="#ff4444", fg="white")
    btn_end.pack(side="left", padx=10, pady=10)

def load_images(num_pairs, level):
    image_folder = f"images/level{level}"

    if not os.path.exists(image_folder):
        raise FileNotFoundError(f"Folder '{image_folder}' does not exist. Please check your levels.")

    files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.avif'))]

    if len(files) < num_pairs:
        raise ValueError(f"Not enough images in {image_folder}. Need {num_pairs} images.")

    images = []
    for f in files[:num_pairs]:
        img = Image.open(os.path.join(image_folder, f)).resize((70, 70))
        images.append(ImageTk.PhotoImage(img))
    return images

def show_end_screen(username, level, time_taken, clicks, root):
    end_frame = tk.Frame(root, bg="#000")
    end_frame.pack(expand=True, fill="both")

    tk.Label(end_frame, text=f"Well done, {username}!", font=("Arial", 18), fg="white", bg="#000").pack(pady=10)
    tk.Label(end_frame, text=f"Time Taken: {time_taken} sec", font=("Arial", 14), fg="white", bg="#000").pack(pady=5)
    tk.Label(end_frame, text=f"Clicks Used: {clicks}", font=("Arial", 14), fg="white", bg="#000").pack(pady=5)

    def play_again():
        end_frame.destroy()
        from main import main
        main()

    tk.Button(end_frame, text="Play Again", font=("Arial", 12), command=play_again,
              bg="#0f0", fg="black").pack(pady=15)
    tk.Button(end_frame, text="Exit", font=("Arial", 12), command=root.quit,
              bg="#f00", fg="white").pack()