import openai
import pyttsx3

# Set up OpenAI API key
openai.api_key = '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
'  # replace with your actual API key

# Set up text-to-speech
engine = pyttsx3.init()

def literacy_bot(prompt):
    # Use OpenAI to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Extract the response text
    response_text = response['choices'][0]['message']['content']
    
    # Print and read the response out loud
    print(response_text)
    engine.say(response_text)
    engine.runAndWait()

# Example usage
user_input = input("Enter a word or phrase to learn: ")
literacy_bot(user_input)
