import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api=os.getenv('api')

history=[]

client = Groq(api_key=api)
print("""\nWelcome to Smart Conversational Assistant!
- Ask any question.
- Have a natural conversation.
- Type 'exit' / 'quit' anytime to quit.
""")

while True:
    userinput=input('Ask Groq : ')
    if any(word in userinput for word in ['quit','exit']):
        print("Programme terminated !")
        break
    else:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user",
                "content": f"{userinput}",}],
            model="llama-3.3-70b-versatile",)

        print(chat_completion.choices[0].message.content)
        print()