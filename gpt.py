from openai import OpenAI

def fetch_response(language, prompt, user_api_key):
  client = OpenAI(api_key=user_api_key)

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a language teacher. Validate your response by using google translate. Extremely important to provide Phonetic spelling. Format your response (extremely important to be table-aligned via python string, and format heading in table): Phonetic Spelling | written in actual language | english translation."},
      {"role": "user", "content": "Give 10 sentences to learn in " + language + " to speak " + prompt}
    ]
  )

  return completion.choices[0].message.content