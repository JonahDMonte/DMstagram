import tkinter as tk
import DMstagram as wi


window = tk.Tk()
window.title("DMstagram")
window.geometry("300x200")

# M1ll1ar4g3
# Create the button and attach the checkmsgs() function to its command
button = tk.Button(window, text="Check Messages", command=wi.checkmsgs)

button.pack(pady=20)

# Start the Tkinter event loop
window.mainloop()