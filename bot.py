import openai
import pytumblr
import os
from datetime import datetime

# Get credentials from environment
openai.api_key = os.getenv("OPENAI_API_KEY")

tumblr_client = pytumblr.TumblrRestClient(
    os.getenv("TUMBLR_CONSUMER_KEY"),
    os.getenv("TUMBLR_CONSUMER_SECRET"),
    os.getenv("TUMBLR_OAUTH_TOKEN"),
    os.getenv("TUMBLR_OAUTH_SECRET")
)

blog_name = os.getenv("TUMBLR_BLOG_NAME")  # Just the blog name (not the URL)

def generate_poetic_tracking_update():
    prompt = (
        "Invent a poetic, surreal status update for a lost package. "
        "Example: 'March 14 – Package seen in a foggy train station.' "
        "Use the same format, with a mysterious tone."
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content'].strip()

def post_to_tumblr():
    text = generate_poetic_tracking_update()
    date_str = datetime.utcnow().strftime("%B %d")
    print(f"{date_str} – {text}")
    tumblr_client.create_text(
        blogname=blog_name,
        state="published",
        title="",
        body=text
    )

post_to_tumblr()
