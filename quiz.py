import requests
import json
class Qiuz:
    def __init__(self, api_url, api_key, headers):
        self.api_url = api_url
        self.api_key = api_key
        self.headers = headers

    def create_quiz(self, level, number, types):
        user_prompt = f'make me {number} {level}-level question, with asnwers and with 4 options on {types} in english language, questions must be as a dictionary inside list of python. without anything even introduction. list name must be questions.'
        print(user_prompt)
        message = [{"role": "user", "content": user_prompt}]

        data = {
            "model": "deepseek/deepseek-chat:free",  # Correct model name for OpenRouter
            "messages": message
        }

        # Send request.
        response = requests.post(self.api_url, json=data, headers=self.headers)

        if response.status_code == 200:
            response_data = response.json()
            assistant_message = response_data['choices'][0]['message']['content']
            # print("AI:", assistant_message)

            # Add assistant reply to messages

            with open("english_questions.json", mode="w") as file:
                json.dump(assistant_message, file, indent=4)


        else:
            print("Error:", response.status_code, response.text)



