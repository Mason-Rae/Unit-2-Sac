from PIL import Image, ImageTk # "Pillow" Library to allow images be inserted
import random # Library for the randomiser
import tkinter as tk # The library for the application
from tkinter import messagebox, ttk # Certain things required from the library
import math # Math library
import time as timeImp # Allows for a countdown
import winsound # Imports sound for the countdown to emit once finished


img = Image.open("Thumbs_Up.png") # Open image with Pillow

keyword_list = ['essay', 'project', 'study',
'presentation', 'coding', 'revision', 'experiment',
'reading', 'art', 'groupwork', 'exam', 'research', 'math',
'language', 'media', 'music', 'sport', 'cooking', 'planning',
'household'] #List of answers for if the user enters random

#Keyword Map
keyword_map = {
    "essay": ["essay", "writing", "english", "document", "documenting", "paper", "report writing"],
    "project": ["project", "assignment", "build", "building", "building a project", "completing assignment", "prototype", "model"],
    "study": ["study", "prepare", "review", "learn", "tutor", "teach", "studying", "homework", "flashcards", "memorise"],
    "presentation": ["presentation", "speech", "slides", "presenting", "powerpoint", "pitch"],
    "coding": ["code", "program", "python", "develop", "java", "c++", "c#", "c sharp", "coding", "programming", "script", "debug" "debugging"],
    "revision": ["revision", "revise", "test prep", "revising", "relearn", "relearning"],
    "experiment": ["experiment", "lab", "science", "science project", "science experiment"],
    "reading": ["read", "book", "chapter", "novel", "literature", "reading", "read a book", "article"],
    "art": ["art", "draw", "paint", "poster", "design", "painting", "drawing", "designing", "sketching","canva", "collaboration", "collab"],
    "groupwork": ["group", "team", "collaborate", "shared", "group project", "groupwork", "group work"],
    "exam": ["exam", "final", "test", "prepare exam", "prepare for the exam", "exam practice", "exam prac", "exam preparation", "exam prep"],
    "research": ["research", "sources", "report", "investigate", "figure out", "search", "case study"],
    "math": ["math", "algebra", "homework", "problems", "calculations", "trigonometry"],
    "language": ["language", "duolingo", "vocab", "french", "japanese", "spanish", "italian", "grammar"],
    "media": ["media", "recording", "video recording", "editing", "video editing", "publishing", "video publishing", "uploading", "video designing", "film", "content creation"],
    "music": ["music", "compose", "lyrics", "sing", "singing", "instrument", "composing"],
    "sport": ["exercise", "training", "train", "practice", "workout", "fitness"],
    "cooking": ["cooking", "cook", "baking", "recipe", "meal prep"],
    "planning": ["schedule", "planning", "plan", "calender", "time management"],
    "household": ["household", "chores", "laundry", "cleaning", "tidying"]
    } #Originated from A.I (Improved)
      #Changed to add more of my ideas - Needs more stuff

#Task Responses
def generate_task_responses(time):
    return {
        "essay": [
            ("Research topic", round(time*0.19357, 1)),
            ("Create outline", round(time*0.12903, 1)),
            ("Write first draft", round(time*0.38710, 1)),
            ("Revise and edit", round(time*0.19357, 1)),
            ("Final proofread", round(time*0.09677, 1))
        ],
        "project": [
            ("Define project scope", round(time*0.0741, 1)),
            ("Do background research", round(time*0.1482, 1)),
            ("Design or plan solution", round(time*0.1111, 1)),
            ("Build or create solution", round(time*0.3333, 1)),
            ("Test and fix issues", round(time*0.2222, 1)),
            ("Create final presentation", round(time*0.1111, 1))
        ],
        "study": [
            ("Review notes", round(time*0.14815, 1)),
            ("Highlight key concepts", round(time*0.11111, 1)),
            ("Summarize material", round(time*0.22222, 1)),
            ("Practice questions", round(time*0.29630, 1)),
            ("Self-test or quiz", round(time*0.22222, 1))
        ],
        "presentation": [
            ("Research topic", round(time*0.25, 1)),
            ("Write bullet points", round(time*0.125, 1)),
            ("Design slides", round(time*0.25, 1)),
            ("Rehearse presentation", round(time*0.2083, 1)),
            ("Final edits and polish", round(time*0.1666, 1))
        ],
        "coding": [
            ("Understand problem requirements", round(time*0.10715, 1)),
            ("Design logic/flowchart", round(time*0.14286, 1)),
            ("Write initial code", round(time*0.32144, 1)),
            ("Test and debug", round(time*0.28571, 1)),
            ("Write comments and documentation", round(time*0.14286, 1))
        ],
        "revision": [
            ("List topics to review", round(time*0.0825, 1)),
            ("Create a revision schedule", round(time*0.12375, 1)),
            ("Study key concepts", round(time*0.33, 1)),
            ("Do practice problems", round(time*0.2475, 1)),
            ("Take mini mock test", round(time*0.20625, 1))
        ],
        "experiment": [
            ("Plan experiment steps", round(time*0.13793, 1)),
            ("Gather materials", round(time*0.10346, 1)),
            ("Run the experiment", round(time*0.31037, 1)),
            ("Record and analyze results", round(time*0.20691, 1)),
            ("Write conclusion/report", round(time*0.24138, 1))
        ],
        "reading": [
            ("Skim the chapter", round(time*0.133, 1)),
            ("Read carefully", round(time*0.4, 1)),
            ("Highlight key points", round(time*0.2,1 )),
            ("Write a short summary", round(time*0.266, 1))
        ],
        "language": [
            ("Revise vocabulary", round(time*0.15, 1)),
            ("Practice speaking", round(time*0.2, 1)),
            ("Do grammar exercises", round(time*0.25, 1)),
            ("Listen to audio or video", round(time*0.2, 1)),
            ("Quiz yourself", round(time*0.2, 1))
        ],
        "art": [
            ("Brainstorm concept", round(time*0.1, 1)),
            ("Sketch rough draft", round(time*0.2, 1)),
            ("Create final piece", round(time*0.4, 1)),
            ("Add details and color", round(time*0.2, 1)),
            ("Label or explain artwork", round(time*0.1, 1))
        ],
        "groupwork": [
            ("Divide responsibilities", round(time*0.1, 1)),
            ("Do your part", round(time*0.4, 1)),
            ("Share updates", round(time*0.1, 1)),
            ("Review each other's work", round(time*0.2, 1)),
            ("Combine and finalise", round(time*0.2, 1))
        ],
        "exam": [
            ("List exam topics", round(time*0.06896, 1)),
            ("Review key notes", round(time*0.20691, 1)),
            ("Practice old exams", round(time*0.27586, 1)),
            ("Identify weak areas", round(time*0.13793, 1)),
            ("Do timed mock test", round(time*0.31037, 1))
        ],
        "research": [
            ("Choose a research question", round(time*0.13793, 1)),
            ("Find reliable sources", round(time*0.20691, 1)),
            ("Take notes and quotes", round(time*0.20691, 1)),
            ("Organise findings", round(time*0.13793, 1)),
            ("Write report or summary", round(time*0.31037, 1))
        ],
        "language": [
            ("Revise vocabulary", round(time*0.15, 1)),
            ("Practice speaking", round(time*0.2, 1)),
            ("Do grammar exercises", round(time*0.25, 1)),
            ("Listen to audio or video", round(time*0.2, 1)),
            ("Quiz yourself", round(time*0.2, 1))
        ],
        "media": [
            ("Plan Your Content", round(time*0.075, 1)),
            ("Prepare your setup", round(time*0.075, 1)),
            ("Record Your Footage", round(time*0.35, 1)),
            ("Edit Your Video", round(time*0.45, 1)),
            ("Publish and share", round(time*0.05, 1))
        ],
        "music": [
            ("Choose your focus(genre)", round(time*0.075, 1)),
            ("Prepare your tools", round(time*0.075, 1)),
            ("Warm up", round(time*0.15, 1)),
            ("Practice or create", round(time*0.45, 1)),
            ("Review and improve", round(time*0.35, 1)),
        ],
        "sport": [
            ("Set a goal", round(time*0.075, 1)),
            ("Gather equipment", round(time*0.025, 1)),
            ("Warm up", round(time*0.2, 1)),
            ("Perform desired activity", round(time*0.5, 1)),
            ("Cool down and recover", round(time*0.2, 1)),
        ],
        "cooking": [
            ("Choose any recipe", round(time*0.05, 1)),
            ("Gather ingredients", round(time*0.1, 1)),
            ("Prepare ingredients", round(time*0.2, 1)),
            ("Cook or bake", round(time*0.6, 1)),
            ("Serve and enjoy", round(time*0.05, 1)),
        ],
        "planning": [
            ("Identify the purpose", round(time*0.05, 1)),
            ("List all tasks", round(time*0.1, 1)),
            ("Priotise and schedule", round(time*0.15, 1)),
            ("Assign resources", round(time*0.25, 1)),
            ("Review and adjust", round(time*0.45, 1)),
        ],
        "household": [
            ("Determine how many there are", round(time*0.05, 1)),
            ("List on urgency", round(time*0.05, 1)),
            ("Complete all chores", round(time*0.65, 1)),
            ("Check the house for any uncompleted tasks", round(time*0.1, 1)),
            ("Complete the final chores", round(time*0.15, 1)),
        ]
    } #Originated from A.I (Improved)
      #Changed to be changing times instead of being set

def pokemon_game():
    win = tk.Toplevel()
    win.title("Pokémon Battle") # Window Title

    # Simple Pokémon setup
    enemy_name = random.randint(1, 3) # Number generator
    if enemy_name == 1:
        enemy_name = "Keshav"
    elif enemy_name == 2:
        enemy_name = "Daniel"
    elif enemy_name == 4:
        enemy_name = "Mason"
    else:
        enemy_name = "Brandon"
    
    player_hp = tk.IntVar(value=50) # Player's health
    enemy_hp = tk.IntVar(value=50) # Enemy health
    if enemy_name == "Daniel":
        enemy_hp = tk.IntVar(value=30)
    elif enemy_name in ('Brandon', 'Mason'):
        enemy_hp = tk.IntVar(value=75)

    status = tk.Label(win, text=f"A wild {enemy_name} appeared!", font=("Arial", 12))
    status.pack(pady=10)

    player_label = tk.Label(win, textvariable=player_hp, font=("Arial", 14)) # Player Title
    player_label.pack()
    tk.Label(win, text="Your HP").pack()

    enemy_label = tk.Label(win, textvariable=enemy_hp, font=("Arial", 14)) # Enemy Title
    enemy_label.pack()
    tk.Label(win, text=f"{enemy_name} HP").pack()

    def player_attack():
        dmg = random.randint(5, 15) # Player damage
        enemy_hp.set(max(0, enemy_hp.get() - dmg)) # Dealing damage to enemy
        status.config(text=f"You dealt {dmg} damage!") # Text informing player how much damage was dealt

        if enemy_hp.get() <= 0:
            status.config(text="You won the battle!")
            winsound.Beep(1000, 200)
            return

        win.after(1000, enemy_attack)

    def enemy_attack():
        dmg = random.randint(5, 12) # Enemy damage
        if enemy_name == "Daniel":
            dmg = random.randint(4, 10)
        player_hp.set(max(0, player_hp.get() - dmg)) # Dealing damage to player
        status.config(text=f"{enemy_name} dealt {dmg} damage!")  # Text informing player how much damage was dealt

        if player_hp.get() <= 0:
            status.config(text="You fainted...")
            winsound.Beep(400, 600)

    attack_btn = tk.Button(win, text="Attack", command=player_attack) # The button for the user to attack the enemy
    attack_btn.pack(pady=10)

def split_task(task):
    task = task.lower() #Makes the task lowercase to deal with easily
    task_responses = generate_task_responses(time)
    for category, keywords in keyword_map.items(): #Looks through the keyword map
        for word in keywords: #Takes the list of words from the map
            if word in task: #Tries to match them with the task
                return category, task_responses.get(category, [("Break task into 5 equal steps", round(time*0.15, 1)), ("Set everything up", round(time*0.05, 1)), ("Complete the tasks assigned", round(time*0.8, 1))]) #Response if the task matches
    return "custom", [("Break task into 3-5 equal steps", round(time*0.15, 1)), ("Set everything up", round(time*0.05, 1)), ("Complete the tasks assigned", round(time*0.8, 1))] #The print for if the task doesn't match

def run_split():
    global big_task, time #Sets 'big_task' and 'time' as global variables for other parts of the code
    big_task = entry_task.get() #Transfers the data
    time_id = entry_time.get() #Transfers the data
    
    time = int(time_id) #Uses 'time' for a confirmed int variable
    
    if not time_id.isdigit(): #Checks for if the time entered is a digit
        if time_id == "": #If nothing is entered
            messagebox.showerror("Error", "Time must be entered.")
        elif time < 0:
            messagebox.showerror("Error", "Time must be more than 0.")
        else: # If something that isn't a number is entered
            messagebox.showerror("Error", "Time must be a number. E.G: \"70\"")
        return # Confirms whether or not the "number" is a digit or not
    
    if big_task.lower() == "random": # Grabs a word from the keyword list to display as a task
        big_task = random.choice(keyword_list)
        
    category, subtasks = split_task(big_task) # Takes the task into the spilt task function

    output.delete(1.0, tk.END) # Resets the text
    output.insert(tk.END, f"Breakdown of: {big_task.capitalize()}\n\n")
    
    def print_step(i=0):
        if i < len(subtasks):
            step, t = subtasks[i]
            secs, mins = math.modf(t)
            secs = secs * 60

            if mins == 1 and secs == 1:
                output.insert(tk.END, f"{i+1}. {step} – {int(mins)} minute, {int(secs)} second\n")
            elif mins == 1:
                output.insert(tk.END, f"{i+1}. {step} – {int(mins)} minute, {int(secs)} seconds\n")
            elif secs == 1:
                output.insert(tk.END, f"{i+1}. {step} – {int(mins)} minutes, {int(secs)} second\n")
            else:
                output.insert(tk.END, f"{i+1}. {step} – {int(mins)} minutes, {int(secs)} seconds\n")

            # Schedule next step for after the step ends
            root.after(int(((mins*60)+secs)*1000), print_step, i+1) # Sets the wait time to allign with the task
            countdown(int((mins*60)+secs))
            root.after(1, winsound.Beep(1000, 500)) # Plays a sound after a task finishs
        else:
            output.insert(tk.END, "\nYou can do this!") # Words of encouragement
            winsound.PlaySound("Fnaf 1 Ending of each Shift Sound Effect.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    print_step()

keyword_dropdown_options = ["art", "assignment", "building", "coding", "composing", "cooking", "documenting", "english",
"essay", "exam prep", "experiment", "final", "groupwork", "homework", "household", "lab", "language", "learn", "literature",
"math", "media", "plan", "presentation", "problems", "project", "reading", "report", "revision", "studying", "test",
"test prep", "training", "vocab"]
#All options for the dropdown box to easliy select the task

secret = random.randint(1, 20) # Selects a number from 1-20
if secret == 1:
    hidden = "You rolled a 1 in 20 chance, well done!\nThe secret is you have good patience unless it was your first try."
elif secret in (2, 3):
    hidden = "The secret is still hidden, but you were half way there. \nIf you were lucky enough to get this, you'll be lucky enough to get the secret. \nGood Luck, you got this!"
else:
    hidden = "There is a secret hidden here, good luck finding it.\nIt's a 1 in 20 chance to spawn. \nReset the app to try again."
# Little joke to have the user try discover what the secret is

pages = [
    {"title": "Index", "message": "This is the index page. \nThank you for clicking the “Index Page”!",
     "subpages": [
         {"title": "List", "message": "Here is the list of all tasks currently available to be selected.\nSelect a task to learn about all the usable words.",
          "subpages": [
              {"title": "Art", "message": "Art, Draw, Paint, Poster, Design, Sketching"},
              {"title": "Chores", "message": "Household, Chores, Laundry, Cleaning, Tidying"},
              {"title": "Coding", "message": "Code, Program, Develop, Script, Debug"},
              {"title": "Cooking", "message": "Cooking, Baking, Recipe, Meal Prep"},
              {"title": "Exam", "message": "Exam, Final, Test"},
              {"title": "Essay", "message" : "Essay, Writing, English, Document, Documenting, Paper"},
              {"title": "Experiment", "message": "Experiment, Lab, Science"},
              {"title": "Groupwork", "message": "Group, Team, Collaborate, Shared"},
              {"title": "Language", "message": "Language, Duolingo, Vocab, Grammar"},
              {"title": "Math", "message": "Math, Algebra, Homework, Problems, Calculations, Trigonometry"},
              {"title": "Media", "message": "Media, Recording, Editing, Publishing, Uploading, Video Designing, Film, Content Creation"},
              {"title": "Music", "message": "Music, Compose, Lyrics, Sing, Instrument"},
              {"title": "Planning", "message": "Schedule, Planning, Calender, Time Management"},
              {"title": "Presentation", "message": "Presentation, Speech, Slides, Presenting, Powerpoint, Pitch"},              
              {"title": "Project", "message": "Project, Assignment, Build, Prototype, Model"},
              {"title": "Revision", "message": "Revision, Test prep, Relearning"},
              {"title": "Reading", "message": "Read, Book, Chapter, Novel, Literature, Article"},
              {"title": "Research", "message": "Research, Sources, Report, Investigate, Search, Case Study"},
              {"title": "Sport", "message": "Exercise, Train, Practice, Workout, Fitness"},
              {"title": "Study", "message": "Study, Prepare, Review, Learn, Tutor, Teach, Homework, Flashcards, Memorise"}
              ]},
         {"title": "Placeholder", "message": "This is the placeholder page."},
         {"title": "About", "message": "This is the core of the S.T.S (AKA Smart Task Splitter). This page would allow users such as yourself to find various subtasks in tasks. \nThis could allow people to gather information upon a selection of tasks to gain an idea of what their specific tasks could be about. \nHowever some of the tasks subtasks  won't have the direct information for the users so we apologise for that…\n\nThank you for visiting \"The Index\"...",
          "subpages": [
              {"title": "  ", "message": f"{hidden}"}]}
     ]}
]

def open_page(title, message, subpages=None):
    if title == "Placeholder":
        pokemon_game()
        return

    win = tk.Toplevel()
    win.title(title)

    tk.Label(win, text=message, font=("Arial", 14)).pack(padx=20, pady=20)

    if subpages:
        frame = tk.Frame(win)
        frame.pack(pady=10)
        for i, sub in enumerate(subpages):
            btn = tk.Button(frame, text=sub["title"],
                            command=lambda s=sub: open_page(s["title"], s["message"], s.get("subpages")))
            btn.grid(row=i // 4, column=i % 4, padx=5, pady=5)

root = tk.Tk()#Starts the app
root.title("🧠 Smart Task Splitter")#Title for the app

tk.Label(root, text="Select your task (or type 'random')", font=("Gill Sans Ultra Bold", 11)).pack()#Text above telling the user what to do
entry_task = ttk.Combobox(root, values=keyword_dropdown_options, width = 35, font=("Franklin Gothic Medium", 11))#What is stored inside the box
entry_task.pack()#Enables the box

tk.Label(root, text="Time available (minutes)", font=("Gill Sans Ultra Bold", 11)).pack()#Tells user whats happening
entry_time = tk.Entry(root, width = 20, font=("Franklin Gothic Medium", 11))#Stored inside box
entry_time.pack()#Enables box

tk.Button(root, text="Split Task", command=run_split).pack(pady=5)#Button that will give a response once hit, that is favoured towards the user's options

thumbs_up = ImageTk.PhotoImage(img) # Convert to Tkinter-compatible image

tk.Label(root, text="Timer").pack()
output2 = tk.Text(root, height = 1, width = 5, font=("Franklin Gothic Medium", 12))#Customisation of the textbox
output2.pack()#Allows custom size to be used

output = tk.Text(root, height = 20, width = 80, font=("Franklin Gothic Medium", 12))#Customisation of the textbox
output.pack()#Allows custom size to be used

label = tk.Label(root, image=thumbs_up) # Create a label with the image
label.pack(padx=10, pady=10) #Customising 

def countdown(t):
    if t >= 1:
        output2.delete(1.0, tk.END) # Resets the timer
        output2.insert(tk.END, f"{t}")
        root.after(1000, countdown, t-1)  # Run again after 1s
    else:
        output2.delete(1.0, tk.END) # Resets the timer again
for page in pages:
    btn = tk.Button(root, text=page["title"], command=lambda p=page: open_page(p["title"], p["message"], p.get("subpages")))
    btn.pack(pady=5) # Creates all the numbers inside the index
    

root.mainloop()#Loops app to keep it constantly running
