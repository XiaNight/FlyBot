import config
from openai import OpenAI

api_key = config.OPENAI_API_KEY
client = OpenAI(api_key = api_key)

def CreateResponse(model, system, context, max_tokens=256, temperature=1, top_p=1, frequency_penalty=0, presence_penalty=0):
	response = client.chat.completions.create(
	model = model,
	messages=[
		{
		"role": "system",
		"content": system
		},
		{
		"role": "user",
		"content": context
		}
	],
	temperature=1,
	max_tokens=256,
	top_p=1,
	frequency_penalty=0,
	presence_penalty=0
	)

	return response

def GetResponse(response):
	return response.choices[0].message.content