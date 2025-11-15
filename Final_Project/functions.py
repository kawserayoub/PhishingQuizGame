import random
from data import quiz_data

# Randomize question order
def init_quiz():
    qs = random.sample(quiz_data, len(quiz_data))
    return {"questions": qs, "index": 0, "score": 0, "total": len(qs)}

def current_question(state):
    return state["questions"][state["index"]]

def answer(state, choice):
    q = current_question(state)
    # Check correctness
    correct = choice == q["answer"]
    # Increase score if correct
    state["score"] += correct
    # Move to next question
    state["index"] += 1
    # Check if quiz finished
    finished = state["index"] == state["total"]
    return correct, q["explanation"], finished

# Wipe state and replace with a fresh quiz
def reset(state):
    state.clear()
    state.update(init_quiz())