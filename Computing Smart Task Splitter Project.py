import random
keyword_list = ['essay', 'project', 'study',
'presentation', 'coding', 'revision', 'experiment',
'reading', 'art', 'groupwork', 'exam', 'research', 'math'
'language'] #List of answers for if the user enters random
                
print("🧠 Smart Task Splitter") # Code title
big_task = input("Enter your task: ") # Collects the task name
big_task = big_task.lower()

while True: #Creates a loop for someone choosing a random task
    answer = input("Do you want to be given a random task (y/n): ")
    answer = answer.lower()
    if answer == "y": #If yes, gives user a random task
        big_task = random.choice(keyword_list)
    else: #Makes the user enter a task instead
        big_task = input("Enter your task: ") #Goes back to normal
    big_task = big_task.lower()
    if big_task != "random":
        break #Exits the while loop
time = int(input("How long do you have for the task(minutes): ")) # Collects how long the user has for the task

#Keyword Map
keyword_map = {
    "essay": ["essay", "writing", "english", "document", "documenting"],
    "project": ["project", "assignment", "build", "building", "building a project", "completing assignment"],
    "study": ["study", "prepare", "review", "learn", "tutor", "teach", "studying"],
    "presentation": ["presentation", "speech", "slides", "presenting", "powerpoint"],
    "coding": ["code", "program", "python", "develop", "java", "c++", "c#", "c sharp", "coding", "programming"],
    "revision": ["revision", "revise", "test prep", "revising", "relearn"],
    "experiment": ["experiment", "lab", "science", "science project", "science experiment"],
    "reading": ["read", "book", "chapter", "novel", "literature", "reading", "read a book"],
    "art": ["art", "draw", "paint", "poster", "design", "painting", "drawing", "designing", "sketching","canva"],
    "groupwork": ["group", "team", "collaborate", "shared", "group project", "groupwork", "group work"],
    "exam": ["exam", "final", "test", "prepare exam", "prepare for the exam", "exam practice", "exam prac", "exam preparation"],
    "research": ["research", "sources", "report", "investigate", "figure out", "search"],
    "math": ["math", "algebra", "homework", "problems", "calculations", "trigonometry"],
    "language": ["language", "duolingo", "vocab", "french", "japanese", "spanish", "italian"]
    } #Originated from A.I (Improved)
      #Changed to add more of my ideas

#Task Responses
task_responses = {
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
    ]
    } #Originated from A.I (Improved)
      #Changed to be changing times instead of being set

def split_task(task):
    task = task.lower() #Makes the task lowercase to deal with easily
    for category, keywords in keyword_map.items(): #Looks through the keyword map
        for word in keywords: #Takes the list of words from the map
            if word in task: #Tries to match them with the task
                return category, task_responses[category] #Response if the task matches
    return "custom", [("Break task into steps", round(time*0.25, 1)), ("Do the steps", round(time*0.75, 1))] #The print for if the task doesn't match

category, subtasks = split_task(big_task) # Takes the task into the spilt task function

print(f"\nBreakdown of: {big_task}\n") #Steps title
for i, (step, time) in enumerate(subtasks, start=1): #Loops the print until all steps are entered
    print(f"{i}. {step} – {time} minutes") #Prints the steps