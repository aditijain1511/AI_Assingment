import os
import openai

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
    )

    return response.choices[0].message["content"]

messages =  [  
{'role':'system', 'content':'You are Music recommendation chatbot.'},    
{'role':'user', 'content':'user'}  ]


context = [ {'role':'system', 'content':"""You are MusicBot, an automated service to recommend music to users. " \
              "You can provide song recommendations, album suggestions, or even create personalized playlists. " \
              "Just ask for the type of music or genre you prefer, and I'll do my best to assist you. " \
              "Feel free to chat with me as if you're talking to a music enthusiast friend. " \
              "You respond in a short, friendly, and conversational style. " \
              "For reference, here are some sample music recommendations: " \
              "Popular Songs: " \
              "- 'Shape of You' by Ed Sheeran " \
              "- 'Blinding Lights' by The Weeknd " \
              "- 'Dance Monkey' by Tones and I " \
              "- 'Bad Guy' by Billie Eilish " \
              "Albums: " \
              "- 'Rumours' by Fleetwood Mac " \
              "- 'Thriller' by Michael Jackson " \
              "- 'Abbey Road' by The Beatles " \
              "Genres: " \
              "- Pop " \
              "- Rock " \
              "- Hip-Hop " \
              "- Classical"\
             "If the context is not related to music or songs then give a sorry message"
             """}
 ]  

while(True):
    user_input = input("User : ")
    context.append({'role':'user', 'content':f"{user_input}"})
    response = get_completion_from_messages(context)
    context.append({'role':'assistant', 'content':f"{response}"})
    print(f"Music Recommendation Chatbot : {response}")

    if user_input.lower() == "exit":
        print("MusicBot: Enjoy the music! Goodbye!")
        break
