import os
import random
import sys
import pytumblr
import google.generativeai as genai

# Add better debug logging
print("Starting bot.py script")
print(f"Python version: {sys.version}")

# Check for environment variables
gemini_key = os.environ.get("GEMINI_API_KEY")
if not gemini_key:
    print("ERROR: GEMINI_API_KEY environment variable is not set!")
else:
    print("GEMINI_API_KEY is set (hidden for security)")

# Check Tumblr env vars
tumblr_vars = [
    "TUMBLR_CONSUMER_KEY",
    "TUMBLR_CONSUMER_SECRET",
    "TUMBLR_OAUTH_TOKEN",
    "TUMBLR_OAUTH_SECRET",
    "TUMBLR_BLOG_NAME"
]

for var in tumblr_vars:
    if not os.environ.get(var):
        print(f"ERROR: {var} environment variable is not set!")
    else:
        print(f"{var} is set (hidden for security)")

try:
    print("Configuring Gemini API")
    genai.configure(api_key=gemini_key)
except Exception as e:
    print(f"ERROR configuring Gemini API: {e}")
    sys.exit(1)
    
def generate_tracking_number():
    return f"{random.randint(1000,9999)}-{random.choice(['X', 'Y', 'Z'])}{random.randint(10,99)}-{random.randint(100,999)}"

def generate_poetic_tracking_update():
    package_states = [
        "lost in a sorting facility",
        "misrouted to a phantom city",
        "delayed by celestial interference",
        "flagged by temporal customs",
        "stuck between dimensions",
        "left at a nonexistent doorstep",
        "unboxed in a memory not your own",
        "delivered to the void",
        "transferred to the Department of Regret",
        "looping through undeliverable time zones"
    ]
    state = random.choice(package_states)
    tracking = generate_tracking_number()

    prompt = (
        f"You're a poetic postal entity. Write a 40-word surreal shipping update.\n"
        f"Package Tracking #: {tracking}\n"
        f"Status: {state}\n"
        f"Tone: haunting, beautiful, eerie. Use imagery and subtle melancholy."
    )
    
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)
        poem = response.text.strip()
    except Exception:
        fallback_poems = [
            f"📦 Tracking #{tracking}\nStatus: {state}\n\nIt waits beside forgotten crates,\nwrapped in shadow, addressed in dust.\nSorting arms passed it without seeing.\nIt hums quietly now—an echo of something once meant for you.",
            f"📦 Tracking #{tracking}\nStatus: {state}\n\nThe barcode is now a prayer.\nYour package wanders through expired routes,\nclutching fragments of memory wrapped in string.\nArrival: uncertain. Intention: unchanged.",
        ]
        poem = random.choice(fallback_poems)

    return f"📦 Tracking #{tracking}\nStatus: {state}\n\n{poem}"


def post_to_tumblr():
    """Post the poetic update to Tumblr"""
    print("Generating poetic update")
    text = generate_poetic_tracking_update()
    print(f"Generated text: {text}")
    
    try:
        print("Creating Tumblr client")
        client = pytumblr.TumblrRestClient(
            os.environ.get("TUMBLR_CONSUMER_KEY"),
            os.environ.get("TUMBLR_CONSUMER_SECRET"),
            os.environ.get("TUMBLR_OAUTH_TOKEN"),
            os.environ.get("TUMBLR_OAUTH_SECRET")
        )
        
        blog_name = os.environ.get("TUMBLR_BLOG_NAME")
        
        # Create the post
        print(f"Posting to blog: {blog_name}")
        response = client.create_text(
            blog_name, 
            state="published", 
            body=text, 
            tags=["lost package", "shipping update", "bot", "thelostpackage-bot", 
                  "poetry bot", "melancholy", "postal limbo", "ai generated", "surrealism"]
        )
        
        print(f"Tumblr API response: {response}")
        print(f"Successfully posted to {blog_name}")
        
    except Exception as e:
        print(f"ERROR posting to Tumblr: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    print("Starting main function")
    post_to_tumblr()
    print("Script completed successfully")
