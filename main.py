import os
from dotenv import load_dotenv
from chatbot import ChatBot
from quiz import Qiuz
from quiz_format import Question
from quiz_brain import QuizBrain
import json

load_dotenv()

# Replace with your OpenRouter API key
API_KEY = os.environ.get("API_KEY_SECRET")
API_URL = 'https://openrouter.ai/api/v1/chat/completions'

# Define the headers
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

# Conversation history
messages = [
    {"role": "system", "content": "You are very helpful."}
]

chat = ChatBot(api_key=API_KEY, api_url=API_URL, headers=headers, messages=messages)
questions = Qiuz(api_url=API_URL, api_key=API_KEY, headers=headers)


# question will be generated based on one of these topics
question_topics = {1: "Parts of Speech:  Nouns, verbs, adjectives, etc.",
                   2: "Tenses:  Past, Present, Future etc.",
                   3: "Sentence Correction:	 Error spotting",
                   4: "Subject-Verb Agreement:	Plural/singular mismatch",
                   5: "Modals & Conditionals:  Can, should, if-clauses",
                   6: "Passive & Reported Speech:  Voice & indirect speech",
                   7: "Prepositions & Articles:  in/on/at, a/an/the",
                   8: "Clauses and Phrases:  Noun/adjective/adverb clauses",
                   9: "Clauses and Phrases:  Noun/adjective/adverb clauses",
                   10: "Punctuation & Style:  Commas, periods, semicolons, etc."}

# questions difficulty will be one of these levels
question_levels = {1: "Beginner",
                   2: "Intermediate",
                   3: "Advanced"}


def data_manipulation():
    """this function cleans and prepared the question data"""
    with open("english_questions.json", mode="r") as file:
        raw_data = file.read()
    cleaned = raw_data.strip('""').replace("```python\\n", "").replace("\\n```", "")
    json_text = cleaned.replace("questions = ", "")
    json_text = bytes(json_text, "utf-8").decode("unicode_escape")
    json_questions = json.loads(json_text)
    # print(len(json_questions))
    # print(type(json_questions))
    # print(json_questions)
    return json_questions

def chat_with_ai():
    """this function create chat box with artificial intelligence"""
    while True:
        user_input = input("YOU: ")
        if user_input.lower() in ["exit", "quit", "goodbye", "bye"]:
            break
        print("Loading....")
        chat.create_chat(user_input=user_input)

question_bank = []
def making_quiz():
    """this function creates questions based on user inputs"""
    user_level = ""
    user_topic = ""

    print("Level:")
    for level in question_levels:
        print(f"{level}. {question_levels[level]}")

    input_level = int(input("Which level do you want to choose. 1/2/3: "))

    print("Question topics:")
    for type in question_topics:
        print(f"{type}. {question_topics[type]}")

    input_topic = int(input("Which topic do you want to choose. 1 to 10: "))

    input_number = int(input("how many questions do you want: "))

    for u_level in question_levels:
        if input_level == u_level:
            user_level = question_levels[u_level]

    for u_topic in question_topics:
        if input_topic == u_topic:
            user_topic = question_topics[u_topic]

    questions.create_quiz(level=user_level, number=input_number, types=user_topic)
    json_questions = data_manipulation()
    for i in json_questions:
        quiz_options = {}
        n = 0
        quiz_text = i["question"]
        # print(quiz_text)
        quiz_answer = i["answer"]
        # print(quiz_answer)
        for option in i["options"]:
            n += 1
            quiz_options[n] = option
        result = Question(q_text=quiz_text, q_answer=quiz_answer, q_options=quiz_options)
        question_bank.append(result)
    current_quiz = QuizBrain(question_bank)
    while current_quiz.still_question_remaining():
        current_quiz.next_question()


choice = input("Do you want chat with AI or quiz. Chat/Quiz: ").lower()
if choice == "chat":
    chat_with_ai()
elif choice == "quiz":
    making_quiz()
