import os
from groq import Groq
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()
api=os.getenv('groq_api')
travily_api=os.getenv('travily_api')

history = [
    {"role": "system",
    "content": "You are a helpful AI assistant. Answer clearly and concisely."}]
realtime_keywords = ["current","latest","today","news","weather","price","stock"]

client = Groq(api_key=api)
travily_client = TavilyClient(api_key=travily_api)

def groq_clilent(inputdata):
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user","content": inputdata}],
        model="llama-3.3-70b-versatile",)
    return chat_completion.choices[0].message.content

def search(query):
    result = travily_client.search(
        query=query,
        max_results=5)
    
    search_data = ""
    for item in result["results"]:
        search_data += item["content"] + "\n"

    return search_data


print("""\nWelcome to Smart Conversational Assistant!
- Ask any question.
- Have a natural conversation.
- Type 'exit' / 'quit' anytime to quit.
""")

while True:
    userinput=input('Ask Groq : ')
    if userinput.lower() in ['quit', 'exit']:
        ch=input('press "y" to get conversation history else any key to exit : ')
        if ch.lower()=='y':
            print("\nConversation History:\n")
            for msg in history:
                print(f"{msg['role']} : {msg['content']}")
                if msg['role'] == 'assistant':
                    print()
            print("Programme terminated !")
            break
        else:
            print("Programme terminated !")
            break
    else:
        history.append({'role':'user','content':userinput})

        check_prompt = f"""Determine whether the query requires real-time information.
        Reply ONLY with:
        YES
        or
        NO
        Query: {userinput}"""
        
        checkresp=groq_clilent(check_prompt)

        if checkresp.lower()=='yes':    # checks for real-time usage
            search_result=search(userinput)
            prompt=f"""Answer the user's question using the following web search results. Question:{userinput}
            Search Results:{search_result}"""
            resp=groq_clilent(prompt)
            history.append({'role':'assistant','content':resp})
            print(resp)
            print()
        else:   # if there's no real-time usage
            chat_completion = client.chat.completions.create(
                messages=history,
                model="llama-3.3-70b-versatile",)
            resp=chat_completion.choices[0].message.content
            history.append({'role':'assistant','content':resp})
            print(resp)
            print('---------------------')



