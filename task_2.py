
import tkinter as tk
from tkinter import scrolledtext
import re
import math
from collections import Counter

# ---------------- FAQ DATABASE ----------------

faqs = [
    # Admissions
    {"question": "How can I apply for admission?",
     "answer": "Apply through the official admission portal or contact the college admission office."},
    {"question": "What are the admission requirements?",
     "answer": "Requirements depend on the course. Check the official admission notice for eligibility details."},
    {"question": "Which documents are required for admission?",
     "answer": "Common documents include marksheets, identity proof, photographs and a leaving certificate, as applicable."},
    {"question": "What is the last date for admission?",
     "answer": "Admission deadlines change each year. Check the official college or university admission notice."},
    {"question": "Can I apply for admission online?",
     "answer": "Check the official admission portal to see whether online applications are available."},
    {"question": "How can I check my admission status?",
     "answer": "Check the admission portal or contact the college admission office."},
    {"question": "Can I change my course after admission?",
     "answer": "Course changes depend on college rules, eligibility and seat availability. Contact the admission office."},
    {"question": "Can diploma students get direct second year admission?",
     "answer": "Eligible diploma holders may apply for direct second-year admission, subject to current rules and seat availability."},
    {"question": "What is the eligibility for engineering admission?",
     "answer": "Engineering eligibility depends on the current admission rules, qualifying subjects and applicable entrance requirements."},
    {"question": "Is an entrance exam required for admission?",
     "answer": "Entrance exam requirements depend on the course and current admission rules."},
    {"question": "How can I get an admission form?",
     "answer": "Visit the official admission portal or contact the college admission office."},
    {"question": "Can I cancel my admission?",
     "answer": "Contact the admission office to learn the cancellation procedure and applicable refund rules."},
    {"question": "What is a merit list?",
     "answer": "A merit list ranks applicants according to the criteria used for a particular admission process."},
    {"question": "How do I check the merit list?",
     "answer": "Check the official admission portal or college notice board."},
    {"question": "Can I get admission after a diploma?",
     "answer": "Some degree courses offer admission to eligible diploma holders. Check the current admission rules."},

    # Fees and scholarships
    {"question": "What are the college fees?",
     "answer": "Fees depend on the course and admission category. Contact the accounts office for the latest fee structure."},
    {"question": "How can I pay college fees?",
     "answer": "Follow the payment instructions provided by your college. Online and office payment options depend on college policy."},
    {"question": "Can I pay fees in installments?",
     "answer": "Installment facilities depend on college policy. Contact the accounts office."},
    {"question": "What is the fee refund policy?",
     "answer": "Refund eligibility depends on applicable college, university and regulatory rules. Contact the accounts office."},
    {"question": "Are scholarships available?",
     "answer": "Scholarships may be available depending on eligibility and applicable schemes. Contact the scholarship section."},
    {"question": "How can I apply for a scholarship?",
     "answer": "Check the official scholarship portal and college announcements for application instructions."},
    {"question": "Which documents are required for scholarships?",
     "answer": "Depending on the scheme, documents may include marksheets, income or category certificates, bank details and identity proof."},
    {"question": "How can I check my scholarship status?",
     "answer": "Check the relevant scholarship portal or contact the college scholarship section."},

    # Academics and examinations
    {"question": "When does the college start?",
     "answer": "Check official college announcements or the academic calendar for the start date."},
    {"question": "How can I get my timetable?",
     "answer": "Check your department notice board, student portal or official college communication group."},
    {"question": "Where can I find the academic calendar?",
     "answer": "Check the official college or university website."},
    {"question": "When are the examinations?",
     "answer": "Check the official examination timetable published by your college or university."},
    {"question": "How can I download my hall ticket?",
     "answer": "Follow your university's official hall-ticket download process or contact the examination section."},
    {"question": "Where can I check my results?",
     "answer": "Check the official university result website or student portal."},
    {"question": "What happens if I fail an exam?",
     "answer": "Check your university's supplementary or backlog examination rules and notifications."},
    {"question": "How can I apply for revaluation?",
     "answer": "Follow the official university revaluation procedure and apply before the announced deadline."},
    {"question": "What is the attendance requirement?",
     "answer": "Attendance requirements depend on college and university regulations. Confirm the applicable rules with your department."},
    {"question": "How can I get study materials?",
     "answer": "Ask your faculty and check the official learning platform or student communication groups."},
    {"question": "How do I contact my class teacher?",
     "answer": "Contact your department office or check official class communication channels."},

    # Certificates and identity cards
    {"question": "How can I get a bonafide certificate?",
     "answer": "Submit a request to the college office according to its certificate application procedure."},
    {"question": "How can I get a student ID card?",
     "answer": "Contact the college office or department to apply for a student ID card."},
    {"question": "What should I do if I lose my ID card?",
     "answer": "Report the loss to the college office and ask how to obtain a replacement."},
    {"question": "How can I get a character certificate?",
     "answer": "Contact the college office to learn the application process and required documents."},
    {"question": "How can I get a leaving certificate?",
     "answer": "Contact the college office and follow the leaving certificate application procedure."},

    # Placements and careers
    {"question": "Does the college provide placements?",
     "answer": "Contact the Training and Placement Cell for current placement information and eligibility."},
    {"question": "How can I contact the placement cell?",
     "answer": "Check official college announcements or contact your department for placement cell details."},
    {"question": "How can I apply for an internship?",
     "answer": "Look for opportunities through your placement cell, verified job portals and official company websites."},
    {"question": "How can I prepare for a placement interview?",
     "answer": "Practise aptitude, communication, technical fundamentals, coding where relevant and interview questions."},
    {"question": "Does the college conduct workshops?",
     "answer": "Check department announcements and official college channels for workshops and technical events."},
    {"question": "How can I prepare my resume?",
     "answer": "Include your education, skills, projects, internships, achievements and contact information in a clear format."},

    # Campus facilities
    {"question": "Where is the college library?",
     "answer": "Check the campus map or ask the college reception for directions to the library."},
    {"question": "What are the library rules?",
     "answer": "Maintain silence, follow borrowing and return rules, and carry your student ID if required."},
    {"question": "Does the college have a computer lab?",
     "answer": "Ask your department or check the college facilities page for computer laboratory information."},
    {"question": "Is hostel accommodation available?",
     "answer": "Contact the college office or hostel administration to confirm availability, eligibility and fees."},
    {"question": "Is a bus facility available?",
     "answer": "Contact the college transport office for available routes, schedules and transport fees."},
    {"question": "Where can I find college contact details?",
     "answer": "Visit the official college website or contact the college reception."},
    {"question": "How can I join a student club?",
     "answer": "Follow college announcements and contact the relevant faculty coordinator or student club representative."},
    {"question": "How can I complain about a problem?",
     "answer": "Contact your class teacher, department or the appropriate college grievance cell."},
    {"question": "What courses does the college offer?",
     "answer": "Check the official college website or admission office for the current list of courses."},

    # General conversation
    {"question": "Thank you",
     "answer": "You're welcome! Feel free to ask another college-related question."}
]

# ---------------- TEXT PREPROCESSING ----------------

stop_words = {
    "the", "is", "a", "an", "are", "am", "i", "you", "me",
    "my", "to", "of", "for", "in", "on", "and", "can",
    "how", "do", "does", "what", "where", "when", "please",
    "tell", "about", "get", "have", "has", "it", "this",
    "could", "would", "should", "want", "know", "some"
}


def preprocess(text):
    text = text.lower()
    words = re.findall(r"[a-z0-9]+", text)
    return [word for word in words if word not in stop_words]


# ---------------- COSINE SIMILARITY ----------------

def cosine_similarity(words1, words2):
    vector1 = Counter(words1)
    vector2 = Counter(words2)

    common = set(vector1) & set(vector2)

    dot_product = sum(
        vector1[word] * vector2[word] for word in common
    )

    magnitude1 = math.sqrt(
        sum(value * value for value in vector1.values())
    )
    magnitude2 = math.sqrt(
        sum(value * value for value in vector2.values())
    )

    if magnitude1 == 0 or magnitude2 == 0:
        return 0.0

    return dot_product / (magnitude1 * magnitude2)


# Prepare the FAQ questions for matching
for faq in faqs:
    faq["words"] = preprocess(faq["question"])


# ---------------- CHATBOT RESPONSE ----------------

def get_answer(user_question):
    question = user_question.strip()

    if not question:
        return "Please type a question."

    cleaned = question.lower().strip()
    cleaned = re.sub(r"[!.?,]+$", "", cleaned)

    greetings = {
        "hi", "hello", "hey", "good morning",
        "good afternoon", "good evening"
    }

    if cleaned in greetings:
        return "Hello! Welcome to the College Helpdesk. How can I help you?"

    if cleaned in {"bye", "goodbye", "exit"}:
        return "Thank you for chatting with the College Helpdesk. Goodbye!"

    user_words = preprocess(question)

    if not user_words:
        return "Please enter a question related to college services."

    best_score = 0.0
    best_faq = None

    for faq in faqs:
        score = cosine_similarity(user_words, faq["words"])

        if score > best_score:
            best_score = score
            best_faq = faq

    if best_faq is not None and best_score >= 0.25:
        return best_faq["answer"]

    return (
        "Sorry, I couldn't find a suitable answer. "
        "Try asking about admission, documents, fees, scholarships, "
        "exams, timetable, certificates, placements or college facilities."
    )


# ---------------- CHAT WINDOW ----------------

def add_message(sender, message):
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, sender + ": " + message + "\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)


def send_message(event=None):
    question = message_entry.get().strip()

    if not question:
        return "break"

    add_message("You", question)
    message_entry.delete(0, tk.END)

    answer = get_answer(question)
    add_message("Chatbot", answer)

    return "break"


def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete("1.0", tk.END)
    chat_area.config(state=tk.DISABLED)

    add_message(
        "Chatbot",
        "Chat cleared! Ask me a question about your college."
    )


# ---------------- GUI DESIGN ----------------

root = tk.Tk()
root.title("College Helpdesk FAQ Chatbot")
root.geometry("680x620")
root.minsize(500, 450)
root.configure(bg="#f0f4f8")

title_label = tk.Label(
    root,
    text="College Helpdesk Chatbot",
    font=("Arial", 18, "bold"),
    bg="#1f4e79",
    fg="white",
    pady=15
)
title_label.pack(fill=tk.X)

subtitle = tk.Label(
    root,
    text="Ask about admissions, fees, exams, scholarships and more",
    font=("Arial", 10),
    bg="#f0f4f8",
    fg="#333333"
)
subtitle.pack(pady=8)

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 11),
    state=tk.DISABLED,
    bg="white",
    padx=10,
    pady=10
)
chat_area.pack(padx=15, pady=5, fill=tk.BOTH, expand=True)

input_frame = tk.Frame(root, bg="#f0f4f8")
input_frame.pack(fill=tk.X, padx=15, pady=10)

message_entry = tk.Entry(
    input_frame,
    font=("Arial", 12)
)
message_entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=8
)
message_entry.bind("<Return>", send_message)

send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#1f4e79",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15
)
send_button.pack(side=tk.LEFT, padx=(8, 0))

clear_button = tk.Button(
    root,
    text="Clear Chat",
    command=clear_chat,
    font=("Arial", 10),
    padx=12
)
clear_button.pack(pady=(0, 10))

add_message(
    "Chatbot",
    "Hello! Welcome to the College Helpdesk. "
    "Ask me a question to get started."
)

message_entry.focus_set()
root.mainloop()
