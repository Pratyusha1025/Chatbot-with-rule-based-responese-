import tkinter as tk
from tkinter import scrolledtext

# Rule-based responses
def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in  user_input:
        return "Hello! I'm your College Assistant Chatbot. How can I help you today?"
    elif "college" in user_input:
        return "Our college is Management Institute of Durgapur. BCA, BBA, and MCA courses are available."
    elif "course" in user_input or "bca" in user_input:
        return "BCA is a 4-year undergraduate program with programming, c,c++,python,DBMS, Web Development and more."
    elif "contact" in user_input or "support" in user_input:
        return "You can reach us at support@college.com or call +91-9000000000."
    elif "hackathon" in user_input:
        return "You can check out Devfolio or HackerEarth for free student hackathons!"
    elif "internship" in user_input:
        return "Visit Internshala or LetsIntern for BCA-specific internships."
    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! 😊"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Please try asking something else."

# GUI setup
def send():
    user_input = entry.get()
    chat_area.insert(tk.END, "You: " + user_input + '\n')
    response = get_response(user_input)
    chat_area.insert(tk.END, "Bot: " + response + '\n\n')
    entry.delete(0, tk.END)
    chat_area.yview(tk.END)

root = tk.Tk()
root.title("Smart College Assistant Chatbot")
root.geometry("500x600")
root.config(bg="#e6f2ff")

title = tk.Label(root, text="🤖 College Chatbot", font=("Arial", 18, "bold"), bg="#e6f2ff", fg="#003366")
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="white", fg="black")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.insert(tk.END, "Bot: Hello! I'm here to help. Ask me anything related to college.\n\n")
chat_area.config(state=tk.NORMAL)

entry_frame = tk.Frame(root, bg="#e6f2ff")
entry_frame.pack(pady=5)

entry = tk.Entry(entry_frame, font=("Arial", 12), width=40)
entry.pack(side=tk.LEFT, padx=10)

send_button = tk.Button(entry_frame, text="Send", command=send, font=("Arial", 12), bg="#0059b3", fg="white")
send_button.pack(side=tk.LEFT)

root.mainloop()