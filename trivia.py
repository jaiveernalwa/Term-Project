from openai import OpenAI
from config import OPENAI_API_KEY
import random

client = OpenAI(api_key=OPENAI_API_KEY)


def question_generator(prompt):
    """This function uses the OpenAI API to generate a trivia question taking a prompt as the input. it returns the generated trivia question."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a Trivia generating bot. Your job is to generate trivia questions based on the category and difficulty inputted by the user.",
            },
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


def genre_randomizer():
    """This function randomizes the genre from a selection of genre options and returns the selected genre."""
    category_count = random.randint(2, 7)
    if category_count == 2:
        category = "Entertainment"
    elif category_count == 3:
        category = "Geography"
    elif category_count == 4:
        category = "History"
    elif category_count == 5:
        category = "Art & Literature"
    elif category_count == 6:
        category = "Science & Nature"
    elif category_count == 7:
        category = "Sports & Leisure"
    return category


def prompt_creator(category, difficulty):
    """This function creates a prompt for the OpenAI API to read by taking a question category and difficulty level as the input parameters. It returns the prompt in a way readable by the OpenAI API."""
    prompt = f"Give me a trivia question that fits in the category: {category}. The question should be {difficulty} difficulty. Only type out the question and any multiple choice options if they exist. Don't even type out the word 'Question:' before the question. Don't type out the correct answer as it is my job to figure it out."
    return prompt


def answer_is_true(question, answer):
    """This function takes a question and a potential answer as input parameters. It uses the OpenAI API to check if the inputted answer is an acceptable answer to the question. It returns a boolean confirming if the answer is acceptable or not."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are an answer checking bot. Your job is the check if the given answer is a correct response to the given question.",
            },
            {
                "role": "user",
                "content": f"The question is {question}. Is {answer} an acceptable answer? Answer YES if the answer is acceptable, or NO if the answer is not acceptable.",
            },
        ],
    )
    checker = response.choices[0].message.content
    if "yes" in checker.lower():
        return True
    elif "no" in checker.lower():
        return False


def question_loop(question_number, seen_questions):
    """This function generates and asks questions to the user, prompting them to answer the question. It returns a tuple of both the question and the answer."""
    cat = genre_randomizer()
    print(f"\nThe category is {cat}.")
    print(f"Question {question_number}:")
    if question_number <= 5:
        question = question_generator(prompt_creator(cat, "Easy"))
        if question not in seen_questions:
            seen_questions.add(question)
            print(question)
        else:
            question_loop(question_number, seen_questions)
    elif 5 < question_number <= 10:
        question = question_generator(prompt_creator(cat, "Medium"))
        if question not in seen_questions:
            seen_questions.add(question)
            print(question)
        else:
            question_loop(question_number, seen_questions)
    elif 10 < question_number <= 15:
        question = question_generator(prompt_creator(cat, "Hard"))
        if question not in seen_questions:
            seen_questions.add(question)
            print(question)
        else:
            question_loop(question_number, seen_questions)
    else:
        question = question_generator(prompt_creator(cat, "Very Hard"))
        if question not in seen_questions:
            seen_questions.add(question)
            print(question)
        else:
            question_loop(question_number, seen_questions)
    answer = input("\nWhat is your answer: ")
    return question, answer


def read_leaderboard(filename="leaderboard.txt"):
    """This function reads a saved leaderboard file and returns the leaderboard data in a list."""
    leaderboard = []
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.strip().split(":")
                leaderboard.append((name, int(score)))
    except FileNotFoundError:
        print("Leaderboard is empty. Please play the game to save your scores!")
    return leaderboard


def save_leaderboard(name, score, filename="leaderboard.txt"):
    """This function saves the current user's score to the leaderboard file and sorts it in descending order."""
    leaderboard = read_leaderboard(filename)
    leaderboard.append((name, score))
    leaderboard.sort(key=lambda x: x[1], reverse=True)

    with open(filename, "w") as file:
        for player, score in leaderboard:
            file.write(f"{player}: {score}\n")


def trivia_game():
    """This function includes the skeleton of the overall trivia game. It uses all the previous functions to successfully run the trivia game."""
    life_counter = 3
    question_counter = 1
    score_counter = 0
    seen_questions = set()
    print("Welcome to the Trivia Game!")
    print(
        "The categories are: 'Entertainment', 'Geography', 'History', 'Art & Literature', 'Science & Nature' and 'Sports & Leisure'"
    )
    name = input("To begin, enter your name: ")
    print(f"Welcome, {name}! You have {life_counter} lives remaining.")
    while life_counter > 0:
        question, answer = question_loop(question_counter, seen_questions)
        is_true = answer_is_true(question, answer)
        if is_true:
            score_counter += 1
            print(f"Congratulations, you are correct! Your score is {score_counter}\n")
            question_counter += 1
        else:
            life_counter -= 1
            question_counter += 1
            print(
                f"Sorry, you are wrong! You now have {life_counter} lives remaining.\n"
            )
    print(
        f"Game Over! Thanks for playing, {name}, your final score was {score_counter}."
    )
    save_leaderboard(name, score_counter)
    leaderboard = read_leaderboard()
    print("\nLeaderboard:")
    if leaderboard:
        for i, (player, score) in enumerate(leaderboard, start=1):
            print(f"{i}. {player}: {score}")
    else:
        print(
            "The leaderboard is currently empty. Please play the game to save your score!"
        )


def main():
    trivia_game()


if __name__ == "__main__":
    main()
