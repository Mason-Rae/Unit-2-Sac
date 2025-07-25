#AI Preview for what they code would look like


# Task templates
task_templates = {
     "essay": [
        ("Research topic", 30),
        ("Create outline", 20),
        ("Write first draft", 60),
        ("Revise and edit", 30),
        ("Final proofread", 15)
    ],
    "project": [
        ("Define project scope", 20),
        ("Do background research", 40),
        ("Design or plan solution", 30),
        ("Build or create solution", 90),
        ("Test and fix issues", 60),
        ("Create final presentation", 30)
    ],
    "study": [
        ("Review notes", 20),
        ("Highlight key concepts", 15),
        ("Summarize material", 30),
        ("Practice questions", 40),
        ("Self-test or quiz", 30)
    ],
    "presentation": [
        ("Research topic", 30),
        ("Write bullet points", 15),
        ("Design slides", 30),
        ("Rehearse presentation", 25),
        ("Final edits and polish", 20)
    ],
    "coding": [
        ("Understand problem requirements", 15),
        ("Design logic/flowchart", 20),
        ("Write initial code", 45),
        ("Test and debug", 40),
        ("Write comments and documentation", 20)
    ],
    "revision": [
        ("List topics to review", 10),
        ("Create a revision schedule", 15),
        ("Study key concepts", 40),
        ("Do practice problems", 30),
        ("Take mini mock test", 25)
    ],
    "experiment": [
        ("Plan experiment steps", 20),
        ("Gather materials", 15),
        ("Run the experiment", 45),
        ("Record and analyze results", 30),
        ("Write conclusion/report", 35)
    ],
    "reading": [
    ("Skim the chapter", 10),
    ("Read carefully", 30),
    ("Highlight key points", 15),
    ("Write a short summary", 20)
    ],
    "language": [
    ("Revise vocabulary", 15),
    ("Practice speaking", 20),
    ("Do grammar exercises", 25),
    ("Listen to audio or video", 20),
    ("Quiz yourself", 20)
    ],
    "art": [
    ("Brainstorm concept", 15),
    ("Sketch rough draft", 30),
    ("Create final piece", 60),
    ("Add details and color", 30),
    ("Label or explain artwork", 15)
    ],
    "groupwork": [
    ("Divide responsibilities", 15),
    ("Do your part", 60),
    ("Share updates", 15),
    ("Review each other's work", 30),
    ("Combine and finalise", 30)
    ],
    "exam": [
    ("List exam topics", 10),
    ("Review key notes", 30),
    ("Practice old exams", 40),
    ("Identify weak areas", 20),
    ("Do timed mock test", 45)
    ],
    "research": [
    ("Choose a research question", 20),
    ("Find reliable sources", 30),
    ("Take notes and quotes", 30),
    ("Organise findings", 20),
    ("Write report or summary", 45)
    ],
    "language": [
    ("Revise vocabulary", 15),
    ("Practice speaking", 20),
    ("Do grammar exercises", 25),
    ("Listen to audio or video", 20),
    ("Quiz yourself", 20)
    ]
    
    }  # [Insert full dictionary above]

# Keyword mapping
keyword_map = {
    "essay": ["essay", "writing", "english"],
    "project": ["project", "assignment", "build"],
    "study": ["study", "prepare", "review"],
    "presentation": ["presentation", "speech", "slides"],
    "coding": ["code", "program", "python", "develop", "java"],
    "revision": ["revision", "revise", "test prep"],
    "experiment": ["experiment", "lab", "science"],
    "reading": ["read", "book", "chapter", "novel", "literature"],
    "art": ["art", "draw", "paint", "poster", "design"],
    "groupwork": ["group", "team", "collaborate", "shared"],
    "exam": ["exam", "final", "test", "prepare exam"],
    "research": ["research", "sources", "report", "investigate"],
    "math": ["math", "algebra", "homework", "problems"],
    "language": ["language", "duolingo", "vocab", "french", "japanese", "spanish"]
    }  # [Insert full map above]

# Task splitter
def split_task(task):
    task = task.lower()
    for category, keywords in keyword_map.items():
        for word in keywords:
            if word in task:
                return category, task_templates[category]
    return "custom", [("Break task into steps", 15), ("Do the steps", 45)]

# Main program
def main():
    print("🧠 Smart Task Splitter")
    big_task = input("Enter your task: ")

    category, subtasks = split_task(big_task)

    print(f"\nBreakdown of: {big_task}\n")
    for i, (step, time) in enumerate(subtasks, start=1):
        print(f"{i}. {step} – {time} minutes")

if __name__ == "__main__":
    main()
