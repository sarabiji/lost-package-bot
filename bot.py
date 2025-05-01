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
            "An example is given: Your parcel has developed consciousness, {state}.\nIt contemplates the existential nature of shipping,\nthe philosophy of arrival, the poetry of waiting,\nwhile postal workers pass by, unaware of its enlightenment."
            "or Somewhere between departure and arrival,\nyour box entered a postal dimension {state}.\nThere, packages grow memories like moss,\nand delivery dates stretch like taffy\npulled by the hands of forgotten clock-makers.",
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
    f"Your shipment has befriended the shadows, {state}.\nThey tell it secrets of other lost things—\nlove letters never received, keys to forgotten doors,\nsingle socks that vanished from dryers.\nIt's learning the geography of absence.",
    f"The delivery truck that should have carried your package\ndrive through a puddle reflecting another world.\nNow {state},\nyour parcel breathes air from that inverted dimension,\nwhere destinations are just beautiful suggestions.",
    f"Time moves backwards for items {state}.\nYour package is unremembering its journey,\nunknowing its contents, unbecoming its shape,\nwhile dreaming of the moment you ordered it\nas if it were a future still to come.",
    f"Your parcel has developed consciousness, {state}.\nIt contemplates the existential nature of shipping,\nthe philosophy of arrival, the poetry of waiting,\nwhile postal workers pass by, unaware of its enlightenment.",
    f"Last night, your package joined a secret society\nof items {state}.\nThey meet in forgotten corners of distribution centers,\nexchanging origin stories and destination dreams,\nplanning gentle rebellions against linear delivery.",
    f"In the space between tracking scans,\nyour shipment slipped sideways through reality, {state}.\nIt now witnesses the quantum foam of logistics,\nexists in superposition of locations,\nuntil observation collapses its journey once more.",
    f"Your box has started collecting artifacts: {state},\ndust from impossible countries,\nechoes of conversations between scanners,\nthe weight of anticipation growing heavier each day,\nas it curates a museum of transit you'll never see.",
    f"The barcode on your package has begun singing\na melody that changes with each scan.\n{state},\nit harmonizes with the hum of conveyor belts,\ncreating a symphony of dislocation only night-shift workers hear.",
    f"Your parcel has fallen in love with stillness, {state}.\nIt's rewriting its molecular structure to include\nthe patience of mountains, the stories of shelf dust,\nthe slow poetry of items that resist arrival.",
    f"At the intersection of intended and actual routes,\nyour package has built a nest {state}.\nIt collabs with airborne dreams and discarded receipts,\nlearning to find home in perpetual between-ness.",
    f"Your shipment has been adopted by the postal spirits, {state}.\nThey've wrapped it in gossamer tracking numbers,\nfed it stories of other journeys interrupted,\nand taught it to dance between the margins of delivery logs.",
    f"Tonight, under fluorescent moons,\nyour package will tell fortunes to other parcels {state}.\nIt reads the creases in their cardboard,\ninterpreting manufacturer stamps like tarot,\npredicting arrivals that defy tracking systems.",
    f"Your box breathes slowly {state},\ndreaming of hands that packed it,\nhands that will unpack it,\nwhile existing in the liminal prayer\nof items midway through their stories.",
    f"In the parliament of lost shipments,\nyour package has been elected speaker, {state}.\nIt advocates for the dignity of undelivered things,\nargues that journeys matter more than arrivals,\nand filibusters motions to expedite delivery.",
    f"The address on your parcel has begun to shift\nlike constellations rearranging nightly.\n{state},\nit rewrites its own destination in invisible ink,\ntelling itself stories of where it truly belongs.",
    f"Your shipment has discovered a network of postal wormholes.\n{state},\nit glimpses parallel deliveries of itself—\none arriving yesterday, one next week, one never—\nand wonders which timeline it currently inhabits.",
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
    client.create_text(blog_name, state="published", body=text, tags=["lost package", "poetry", "shipping update", "bot","the-lost-package-tracker"])
    
    print(f"Posted to {blog_name}: {text}")

if __name__ == "__main__":
    post_to_tumblr()
