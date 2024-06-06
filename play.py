from openai import OpenAI

client = OpenAI()

print("""



"""  )
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a fashion expert, skilled in design,understanding astehthics, style and matching outfitss with creative flair accourding to user requests."},
    {"role": "user", "content": "Compose an outfit that fits amsterdam weather in june, semi formal with dark overtones."}
  ]
)

print(completion.choices[0].message.content)

