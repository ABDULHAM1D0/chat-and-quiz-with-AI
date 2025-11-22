import requests
class ChatBot:
    def __init__(self, api_url, api_key, headers, messages):
        self.messages = messages
        self.api_url = api_url
        self.aoi_key = api_key
        self.headers = headers

    def create_chat(self, user_input):
        self.messages.append({"role": "user", "content": user_input})

        data = {
            "model": "deepseek/deepseek-chat:free",  # Correct model name for OpenRouter
            "messages": self.messages
        }

        # Send request
        response = requests.post(self.api_url, json=data, headers=self.headers)

        if response.status_code == 200:
            response_data = response.json()
            assistant_message = response_data['choices'][0]['message']['content']
            print("AI:", assistant_message)

            # Add assistant reply to messages.
            self.messages.append({"role": "assistant", "content": assistant_message})

        else:
            print("Error:", response.status_code, response.text)
