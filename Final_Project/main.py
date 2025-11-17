import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import os

from data import quiz_data
from functions import init_quiz, current_question, answer, reset


# -----Base config-----
root = tk.Tk()
root.title("Quiz game")
root.geometry("1200x800")

base_dir = os.path.dirname(os.path.abspath(__file__))

# Why? if you have a fish memory like me
bg_color = "#2A233B"
fg_color = "#DFCDDE"
title_font = ("Montserrat", 35, "bold")
body_font_lg =  ("Montserrat", 20)
body_font_mm = ("Montserrat", 15)
body_font_sm = ("Montserrat", 10)
button_font = ("System", 20, "bold")

# -----Background image-----
bg_path = os.path.join(base_dir, "images", "background2.png") # Loading background image for the program
bg_original = Image.open(bg_path) # Using a different library because PhotoImage wasnt able to resize the image
bg_photo = None

# Function to resize background image dynamically
def bg(event=None):
    global bg_photo
    w = root.winfo_width()
    h = root.winfo_height()
    resize = bg_original.resize((w,h), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(resize)
    bg_label.config(image=bg_photo)

bg_label = tk.Label(root)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
root.bind("<Configure>", bg)

# -----Helpers-------
# Creating this fuction allows to create "One window, many pages" approach instead of "One window per page"
def clear():
    for c in root.winfo_children():
        if c is bg_label:  # keeps the background
            continue
        c.destroy()

# Create a function for title, body text and buttons to minimize redundancy and pain in my poor fingers
def title(text):
    frame= tk.Frame(root, bg=bg_color, padx=20, pady=10)
    frame.place(relx=0.5, rely=0.08, anchor="center")
    tk.Label(frame,text=text,font=title_font, fg=fg_color,bg=bg_color).pack()
    return frame
    
def body(text, font):
    frame = tk.Frame(root, bg=bg_color, padx=80, pady=60)
    frame.place(relx=0.5, rely=0.45, anchor="center")
    tk.Label(frame, text=text, font=font, fg=fg_color,
             bg=bg_color, wraplength=820, justify="left").pack()
    return frame

def button(text, cmd=None, relx=0.5, rely=0.88):
    frame = tk.Frame(root, bg=bg_color, padx=20, pady=20)
    frame.place(relx=relx, rely=rely, anchor="center")
    
    # Enables to test every page
    if cmd is None: 
        btn = tk.Button(frame, text=text, font=button_font, fg=fg_color,
                                    bg=bg_color, padx=20, pady=20)
    else:
        btn = tk.Button(frame, text=text, command=cmd, font=button_font, 
             fg=fg_color, bg=bg_color,padx=20,pady=20)
    btn.pack()
    return frame

def button_center(text, cmd=None):
    return button(text, cmd, relx=0.5, rely=0.88)

def button_left(text, cmd=None):
    return button(text, cmd, relx=0.25, rely=0.88)

def button_right(text, cmd=None):
    return button(text, cmd, relx=0.75, rely=0.88)

# Preloading quiz images
for q in quiz_data:
    images = os.path.join(base_dir, "images", q["image_path"])
    q["image_obj"] = PhotoImage(file=images)
    
# Initiating quiz
quiz_state = init_quiz()

# -----Pages-------
def welcome_page():
    clear()
    title("To Be Phished or Not to Be Phished")
    
    welcome_text = (
        "Your inbox looks ordinary at first glance. A delivery update, a payment notice, "
        "a message from someone you trust. Then something feels off. This is where the game begins.\n\n"
        "This game puts you in realistic phishing situations that test how well you can spot small "
        "details under pressure. The goal is to train your instincts and help you recognize real "
        "attacks before they reach you."
    )
    
    body(welcome_text, body_font_lg)
    button_center("START", info_page)
    
def info_page():
    clear()
    title("What is phishing?")
    
    info_text = (
    "Phishing is a type of social engineering attack where someone tries to trick you into giving away "
    "personal information, such as passwords, credit card details, or other sensitive data. Instead of "
    "breaking into systems directly, the attacker pretends to be someone trustworthy, like your bank, a "
    "colleague, or a familiar service, and lures you into taking an action: clicking a link, downloading "
    "a file, or logging into a fake website.\n\n"
    "It works because it targets human attention, not technology. When you’re tired, distracted, or in a "
    "hurry, you’re more likely to miss small details, such as an off-looking email address, a slightly "
    "wrong URL, or a message that feels urgent. That moment of lowered focus is what phishing exploits."
)
    body(info_text, body_font_mm)
    
    button_left("RETURN", welcome_page)
    button_right("NEXT", types_page)
    
def types_page():
    clear()
    title("Different forms of phishing")
    
    types_text = (
    "1. Mass phishing\n"
    "Generic fake emails sent to many people. They often claim to be from a familiar service such as your "
    "bank or a delivery company and include a link to click or a file to open. These are the most common "
    "type and rely on volume rather than precision.\n\n"
    "2. Spear phishing\n"
    "Targeted messages written specifically for you or your organization. The attacker uses real details "
    "like your name, role, and company to sound convincing.\n\n"
    "3. Business Email Compromise (BEC)\n"
    "The attacker pretends to be a boss, colleague, or vendor to request money or sensitive data. It often "
    "looks completely legitimate because it uses a familiar tone and formatting. Financial loss is usually "
    "the goal.\n\n"
    "4. Credential phishing\n\n"
    "Emails that lead to fake login pages designed to steal usernames and passwords. The website looks "
    "identical to the real one but the URL is slightly wrong. This is how many account breaches start.\n\n\n"
    "5. Email spoofing\n"
    "Attackers forge or mimic legitimate addresses so the email appears to come from a trusted source. "
    "They can manipulate sender names or domain lookalikes. Technical protections such as SPF, DKIM, and "
    "DMARC help block this, but not all systems enforce them.\n\n"
)
    body(types_text, body_font_sm)
    
    button_left("RETURN", info_page)
    button_right("NEXT", how_to)
    
def how_to():
    clear()
    title("How to play?")
    
    how_to_text = ("You will see a series of email scenarios based on real phishing attempts. "
    "Each message contains clues that reveal whether it is legitimate or fake.\n\n"
    "Read each email carefully. Pay attention to sender details, links, tone, and urgency. "
    "Choose Safe if you believe it’s real or Phishing if you suspect it’s a trap.\n\n"
    "Your score increases with each correct answer. The goal is to sharpen your attention "
    "and train your eyes to spot the small signals that make all the difference.")
    body(how_to_text, body_font_lg)
    
    button_left("RETURN", types_page)
    button_right("NEXT", quiz )
    
# -----Quiz page-----
def quiz():
    clear()
    q = current_question(quiz_state)
    
    tk.Label(root, text=q["instruction"], font=title_font, fg=fg_color,
             bg=bg_color,).pack(pady=10)
    tk.Label(root, text=q["scenario"], font=body_font_lg, fg=fg_color,
             bg=bg_color, wraplength=820, justify="left",).pack(pady=10)
    tk.Label(root, image=q["image_obj"], bg=bg_color).pack(pady=10)
    
    choices_frame= tk.Frame(root, bg=bg_color)
    choices_frame.pack(pady=20)
    
    btn_phishy = tk.Button(choices_frame, text="PHISHY", font=button_font,
                           fg=fg_color, bg=bg_color, padx=40, pady=20,
                           command=lambda:handle_ans("Phishy"))
    btn_phishy.grid(row=0, column=0, padx=40)
    
    btn_safe = tk.Button(choices_frame, text="SAFE", font=button_font,
                         fg=fg_color, bg=bg_color, padx=40, pady=20,
                         command=lambda:handle_ans("Safe"))
    btn_safe.grid(row=0, column=1, padx=40)
    
def handle_ans(choice):
    correct, expl, done = answer(quiz_state, choice)
    clear()
    output = ("Correct!\n\n" if correct else "Incorrect.\n\n") + expl
    tk.Label(root, text=output, font=body_font_lg, fg=fg_color,
             bg=bg_color, wraplength=820, justify="left",).pack(pady=40)
    
    if done: 
        button_center("View results", results)
    else:
        button_center("Next question", quiz)
        
def results():
    clear()
    score = quiz_state["score"]
    total = quiz_state["total"]
    
    title("You result")
    
    body(f"You scored {score} out of {total}", body_font_lg)
    
    button_center("Security tips", tips.intro)
    
class SecurityTips:
    def __init__(self,root):
        self.root = root
        
    def intro(self):
        clear()
        title("Security mindset")
        
        text = ( "Good security is not about remembering hundreds of rules. "
            "It is about setting a few smart habits that protect you automatically.\n\n"
            "These pages cover the most important habits you can start using today." )
        body(text, body_font_lg)
        
        button_left("RETURN", results)
        button_right("NEXT", self.two_fa)
        
    def two_fa(self):
        clear()
        title("Use two factor authentication (2FA)")
            
        text = ("Even if someone steals your password, two-factor authentication (2FA) blocks them "
            "from logging in.\n\n"
            "Use an authenticator app or a physical security key rather than SMS when possible. "
            "Turn on 2FA on every important account: email, banking, social media, and work systems.")
        body(text, body_font_lg)
            
        button_left("RETURN", self.intro)
        button_right("NEXT", self.pswd_manager)
            
    def pswd_manager(self):
        clear()
        title("Use a password manager!")
            
        text= ("A password manager safely stores all your passwords and fills them in for you. "
            "This lets you use long, unique passwords without having to remember them.\n\n"
            "It removes the need to reuse passwords across different sites. Using a manager is "
            "one of the biggest upgrades you can make to your security.")
        body(text, body_font_lg)
            
        button_left("RETURN", self.two_fa)
        button_right("NEXT", self.pswd_system)
            
    def pswd_system(self):
        clear()
        title("Create a memorable password system")
            
        text = ("If you prefer not to use a manager, build your own repeatable system so each password "
            "is unique but still easy to recall.\n\n"
            "Pick a private base word that only you know, then add a small part that depends on the site.\n\n"
            "Example:\n"
            "  Base: GraniteRiver7!\n"
            "  Gmail  → GraniteRiver7!Mail\n"
            "  Spotify → GraniteRiver7!Music\n"
            "  LinkedIn → GraniteRiver7!Work\n\n"
            "The pattern is consistent, but each password is different.")
        body(text, body_font_mm)
            
        button_left("RETURN", self.pswd_manager)
        button_right("NEXT", self.data_breaches)
            
    def data_breaches(self):
        clear()
        title("Check if you data has been exposed")
            
        text = ("Data breaches happen when services lose control over user data such as emails and passwords. "
            "Attackers then try these leaked passwords on many other sites.\n\n"
            "Use a service like “Have I Been Pwned” to check if your email appears in known breaches. "
            "If it does, change those passwords immediately and never reuse them on other accounts.")
        body(text, body_font_lg)
            
        button_left("Restart", restart)
        button_right("Exit", root.destroy)
            
            
def restart():
    reset(quiz_state)
    welcome_page()
    
tips = SecurityTips(root)

welcome_page()
bg()

root.mainloop()

