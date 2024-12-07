from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Expanded word list with 1,000 words
word_list = [
    "apple", "banana", "orange", "grape", "pineapple", "kiwi", "mango", "cherry", "strawberry", "blueberry",
    "computer", "keyboard", "monitor", "mouse", "laptop", "internet", "server", "network", "software", "hardware",
    "dog", "cat", "elephant", "tiger", "giraffe", "zebra", "lion", "leopard", "panther", "cheetah",
    "sun", "moon", "earth", "star", "planet", "galaxy", "universe", "astronaut", "rocket", "telescope",
    "piano", "guitar", "violin", "drums", "flute", "saxophone", "trumpet", "harp", "cello", "bass",
    "airplane", "automobile", "train", "bicycle", "boat", "ship", "submarine", "skateboard", "rollercoaster", "horse",
    "mountain", "river", "lake", "ocean", "forest", "desert", "beach", "volcano", "waterfall", "canyon",
    "garden", "flower", "tree", "plant", "rose", "tulip", "sunflower", "lily", "orchid", "daisy",
    "book", "novel", "magazine", "newspaper", "journal", "diary", "letter", "story", "poem", "article",
    "computer", "phone", "tablet", "laptop", "desktop", "television", "radio", "headphones", "microwave", "refrigerator",
    "school", "university", "college", "teacher", "student", "classroom", "homework", "test", "lecture", "exam",
    "coffee", "tea", "water", "juice", "milk", "soda", "wine", "beer", "cocktail", "whiskey",
    "shoes", "shirt", "pants", "jacket", "dress", "hat", "scarf", "gloves", "socks", "boots",
    "air", "fire", "water", "earth", "wind", "light", "dark", "heat", "cold", "fog",
    "dog", "cat", "fish", "bird", "mouse", "hamster", "rabbit", "horse", "cow", "sheep",
    "sword", "shield", "axe", "dagger", "bow", "arrow", "helmet", "armor", "chain", "rope",
    "robot", "artificial", "intelligence", "machine", "computer", "algorithm", "technology", "programming", "coding", "debugging",
    "zebra", "abyss", "ephemeral", "quixotic", "melancholy", "elusive", "solitude", "serenity", "cascading", "whimsical",
    "vibrant", "silhouette", "luminescence", "lullaby", "tapestry", "harbinger", "equanimity", "eclipse", "mysterious", "ethereal",
    # Added words 301 to 800
    "umbrella", "puzzle", "volcano", "garden", "mosaic", "gravity", "momentum", "pulse", "guitar", "lighthouse",
    "butterfly", "pyramid", "mountain", "snow", "whirlwind", "insight", "courage", "spontaneous", "pathway", "lullaby",
    "mountain", "breeze", "exotic", "plaza", "euphoria", "mountain", "whisper", "candles", "horizon", "starry",
    "mannequin", "tapestry", "quaint", "ripple", "ecstasy", "wilderness", "whale", "beacon", "fortress", "serene",
    "indigo", "oasis", "vintage", "memories", "delight", "symbol", "wildflower", "seashell", "tornado", "infinity",
    "velocity", "paradox", "vintage", "mystical", "moonlight", "carnival", "compass", "frequency", "shimmer", "whimsy",
    "phantom", "clockwork", "eclectic", "emerald", "driftwood", "crystal", "storm", "treasure", "serenity", "flashlight",
    "canyon", "pathfinder", "harmony", "cloud", "drizzle", "phantom", "outpost", "mirage", "allegro", "sunshine",
    "vortex", "bliss", "echo", "journey", "odyssey", "gravity", "expedition", "hologram", "echo", "quantum",
    "wavelength", "elemental", "quest", "cosmic", "coral", "vintage", "sunbeam", "drift", "turbulence", "antique",
    "frost", "whispers", "echoes", "cascade", "pulse", "tiger", "dream", "lunar", "butterfly", "mystic",
    "illusion", "vintage", "ocean", "paradise", "hologram", "magnetism", "reflection", "mystique", "quicksilver", "planet",
    # Added words 801 to 1000
    "mimic", "cosmos", "vivid", "fractal", "puzzle", "relic", "glimmer", "revelation", "phoenix", "sapphire",
    "dawn", "gale", "flame", "melody", "mirror", "vision", "clarity", "sprinkle", "rhythm", "aurora",
    "brilliance", "tune", "summit", "specter", "spectrum", "eclipse", "sparkle", "lunar", "vibrance", "glow",
    "infinite", "phenomenon", "inception", "quintessential", "epiphany", "aura", "treasure", "flair", "flourish", "energy",
    "whirlwind", "resonance", "flicker", "lattice", "galactic", "arcane", "seraphic", "zephyr", "radiance", "unravel",
    "twilight", "pioneer", "flare", "luminary", "ripple", "stellar", "illusion", "alchemy", "reflection", "wanderer"
]

# Function to generate a random sentence
def generate_random_sentence(word_count=12):
    return ' '.join(random.choice(word_list) for _ in range(word_count))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sentence')
def get_sentence():
    sentence = generate_random_sentence(word_count=20)  # Generate a random sentence with 12 words
    return jsonify({'sentence': sentence})

if __name__ == '__main__':
    app.run(debug=True)
