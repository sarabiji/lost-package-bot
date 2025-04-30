import os
import random
import pytumblr
from openai import OpenAI

def generate_poetic_tracking_update():
    """Generate a poetic tracking update for a lost package"""
    
    # List of possible package states
    package_states = [
        "lost in a sorting facility",
        "delayed due to weather",
        "misrouted to another city",
        "sitting in customs",
        "awaiting recipient pickup",
        "damaged in transit",
        "mistakenly marked as delivered",
        "on a truck going the wrong direction",
        "stuck between dimensions",
        "forgotten in a warehouse corner"
    ]
    
    # Randomly select a package state
    state = random.choice(package_states)
    
    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a poet who writes beautiful, melancholic poems about lost packages."},
                {"role": "user", "content": f"Write a short, poetic shipping update for a package that is {state}. Keep it under 100 words, wistful and a bit mysterious."}
            ],
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        # Fallback poem in case of API issues
        fallback_poems = [
            f"Your package wanders, {state}.\nLost in the labyrinth of commerce.\nWaiting, always waiting, for reunion.",
            f"Between sender and receiver,\n{state}.\nA journey unfinished, a story untold.",
            f"In transit limbo, {state}.\nSomeday it may find its way home.\nOr perhaps it has found a new destiny."
        ]
        print(f"Error calling OpenAI API: {e}")
        return random.choice(fallback_poems)

def post_to_tumblr():
    """Post the poetic update to Tumblr"""
    text = generate_poetic_tracking_update()
    
    client = pytumblr.TumblrRestClient(
        os.environ.get("TUMBLR_CONSUMER_KEY"),
        os.environ.get("TUMBLR_CONSUMER_SECRET"),
        os.environ.get("TUMBLR_OAUTH_TOKEN"),
        os.environ.get("TUMBLR_OAUTH_SECRET")
    )
    
    blog_name = os.environ.get("TUMBLR_BLOG_NAME")
    
    # Create the post
    client.create_text(blog_name, state="published", body=text, tags=["lost package", "poetry", "shipping update", "bot"])
    
    print(f"Posted to {blog_name}: {text}")

if __name__ == "__main__":
    post_to_tumblr()
