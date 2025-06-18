import tkinter as tk
from game import start_game
from database import init_db

# Create initial login and level selection
def main():
    init_db()
    root = tk.Tk()
    root.title("Memory Match Game")
    root.geometry("400x300")
    root.config(bg="#222")

    def go_to_levels():
        username = entry.get()
        if not username.strip():
            return
        login_frame.destroy()
        show_level_selection(username)

    def show_level_selection(username):
        level_frame = tk.Frame(root, bg="#222")
        level_frame.pack(expand=True)

        tk.Label(level_frame, text=f"Welcome, {username}!", font=("Arial", 16), fg="white", bg="#222").pack(pady=10)
        tk.Label(level_frame, text="Choose a Level to Play:", font=("Arial", 12), fg="white", bg="#222").pack(pady=5)

        def level_button(level_text, size):
            return tk.Button(level_frame, text=level_text, width=25, height=2,
                             command=lambda: start_game(username, size, root),
                             bg="#444", fg="white", font=("Arial", 10))

        level_button("Level 1 – Easy 4x4", 4).pack(pady=5)
        level_button("Level 2 – Medium 6x6", 6).pack(pady=5)
        level_button("Level 3 – Hard 8x8", 8).pack(pady=5)

    login_frame = tk.Frame(root, bg="#222")
    login_frame.pack(expand=True)

    tk.Label(login_frame, text="Enter your name to start:", font=("Arial", 14), fg="white", bg="#222").pack(pady=10)
    entry = tk.Entry(login_frame, font=("Arial", 12))
    entry.pack(pady=5)

    start_btn = tk.Button(login_frame, text="Start", command=go_to_levels,
                          bg="#0a84ff", fg="white", font=("Arial", 12))
    start_btn.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
