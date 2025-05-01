import os
import random
import pytumblr
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

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
        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = (
            "You are a poet who writes beautiful, melancholic poems about lost packages.\n"
            f"Write a short, poetic shipping update for a package that is {state}.\n"
            "Keep it under 50 words, wistful and a bit mysterious."
        )
        response = model.generate_content(prompt)
        return response.text.strip()
        
    except Exception as e:
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
    client.create_text(blog_name, state="published", body=text, tags=["lost package", "shipping update", "bot", "the-lost-package-tracker", "poetry bot", "melancholy", "postal limbo", "ai generated", "surrealism"])
    
    print(f"Posted to {blog_name}: {text}")

if __name__ == "__main__":
    post_to_tumblr()
