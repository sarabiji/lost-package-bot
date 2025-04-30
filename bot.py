import openai
import pytumblr
import os
from datetime import datetime

# Load credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

tumblr_client = pytumblr.TumblrRestClient(
    os.getenv("TUMBLR_CONSUMER_KEY"),
    os.getenv("TUMBLR_CONSUMER_SECRET"),
    os.getenv("TUMBLR_OAUTH_TOKEN"),
    os.getenv("TUMBLR_OAUTH_SECRET")
)

blog_name = os.getenv("TUMBLR_BLOG_NAME")

def generate_poetic_tracking_update():
    prompt = (
        "Invent a poetic, surreal status update for a lost package. "
        "Example: 'March 14 – Package seen in a foggy train station.' "
        "Use the same format. Only one line."
    )
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def post_to_tumblr():
    text = generate_poetic_tracking_update()
    print(f"Generated: {text}")
    tumblr_client.create_text(
        blogname=blog_name,
        state="published",
        title="",
        body=text
    )

if __name__ == "__main__":
    post_to_tumblr()
