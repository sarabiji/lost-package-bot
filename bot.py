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
    print(f"Selected package state: {state}")
    
    try:
        print("Creating Gemini model instance")
        model = genai.GenerativeModel("gemini-1.5-pro")  # Corrected model name
        
        print("Creating prompt")
        prompt = (
            "You are a poet who writes beautiful, melancholic poems about lost packages.\n"
            f"Write a short, poetic shipping update for a package that is {state}.\n"
            "Keep it under 50 words, wistful and a bit mysterious."
        )
        
        print("Generating content")
        response = model.generate_content(prompt)
        print("Successfully generated content from Gemini API")
        return response.text.strip()
        
    except Exception as e:
        print(f"ERROR generating content from Gemini: {str(e)}")
        # Fallback poem in case of API issues
        fallback_poems = [
            # Original concept poems with surreal, narrative elements
            f"Your package now whispers to dust motes, {state}.\nIt tells tales of conveyor belts that spiral into nebulae,\nof barcode scanners that read the language of stars.\nThe cardboard remembers your fingerprints, waiting.",
            f"In dreams of bubble wrap and packing tape,\nyour parcel has become a traveler {state}.\nIt befriended a forgotten luggage at midnight,\nlearned secrets from rain-soaked labels,\nand writes you postcards it cannot send.",
            f"The tracking number transformed into a constellation last night.\nYour package, {state},\ndances with moonlight through warehouse windows,\nits contents shifting like tides\nunder the watch of fluorescent guardians.",
            f"What stories your shipment collects, {state}.\nIt's witnessed the midnight confessions of forklift operators,\nheard the lullabies of sorting machines,\nbefore slipping between the cracks of ordinary time.",
            f"Somewhere between departure and arrival,\nyour box entered a postal dimension {state}.\nThere, packages grow memories like moss,\nand delivery dates stretch like taffy\npulled by the hands of forgotten clock-makers.",
            f"The address label faded into a map of an impossible city.\nYour parcel wanders there now, {state},\nwhere streets are named after lost children's toys\nand every intersection smells of cardboard and possibility.",
            f"In the cathedral of misplaced things,\nyour package kneels {state}.\nIt prays to patron saints of zip codes,\nconfesses desires wrapped in brown paper,\nand waits for redemption in the form of delivery.",
        ]
        
        print("Using fallback poem due to error")
        return random.choice(fallback_poems)

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
