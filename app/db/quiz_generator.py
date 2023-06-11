from app.db.functions import Questions


async def create_quiz():
    quiz = {}
    for tier in [1, 2, 3, 4, 5, 6]:
        question = await Questions.get_question(tier=tier)
        q = create_question(question)
        quiz.update(q)

    return quiz


def create_question(question):
    tier = question.tier
    question_text = question.question
    code = question.answers_code.split(",")

    answers = question.answers.split("|")
    for i, item in enumerate(answers):
        answers[i] = f"{i + 1}. {item}"

    result = {
        tier: {"question": question_text,
               "answers": answers,
               "code": code,
               }
    }

    return result
