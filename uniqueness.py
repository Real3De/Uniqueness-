

import Flask
import requests
import json

app = Flask(__name__)

def get_unique_text_snippets(search_query):
  """Gets a list of all the unique text snippets that contain the given search query."""
  response = requests.get("https://api.stackexchange.com/2.2/search/advanced?q={}".format(search_query))
  data = json.loads(response.content)
  text_snippets = []
  for result in data["items"]:
    text_snippets.append(result["snippet"])
  return text_snippets

@app.route("/")
def index():
  """The index route."""
  search_query = request.args.get("q")
  text_snippets = get_unique_text_snippets(search_query)
  return json.dumps(text_snippets)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
