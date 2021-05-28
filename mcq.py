from mcq_question import Question
question_prompt = [
    "The author of Anuradha is?\n a)Bijay Malla\n b)slkfjslkj\n c)sdjklsjdl\n d)slkjdklsj\n\n",
    "The Capial of USA is?\n a)New York\n b)Washington DC\n c)sljkljf\n d)dkhfjkdh\n\n",
    "Largest Animal?\n a)jkdfjldk\n b)dkjlkdfj\n c)dlkfjkdlfj\n d)Whale\n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "b"),
    Question(question_prompt[2], "d")
    
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    if score == 0:
        print("\nYou didn't answer any questions correctly")
    else:
        print("\nYou got", score, "correct answer(s)") 
run_test(questions)

