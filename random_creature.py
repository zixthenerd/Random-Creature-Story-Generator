import random
import textwrap
import time

SYLLABLES = [
    "ka", "zo", "mi", "ra", "tu", "ne", "li", "ph", "on", "el",
    "gu", "sa", "ri", "do", "vi", "qua", "sha", "be", "xo", "yu"
]

EYES = ["o o", "• •", "o.O", "° °", "⊙ ⊙", "@ @", "≧ ≦", "◕ ◕"]
MOUTHS = ["__", "~~", "o", "O", "w", "ᴥ", "‿", "︶"]
BODIES = [
    ["  /\\_/\\  ", " ( {E} ) ", "  \\_V_/  "],
    ["   ___   ", "  ( {E} ) ", "  /|{M}|\\ "],
    ["  .---.  ", " ( {E} ) ", "  `-^-´  "],
    ["  (___)  ", " ( {E} ) ", "  /   \\  "],
    ["  <| |>  ", " ( {E} ) ", "  /_{M}_\\ "],
]
ACCESSORIES = [
    "a tattered flag",
    "a glowing crystal",
    "a tiny backpack",
    "a smug hat",
    "a rusty bell",
    "a pair of spectacles",
    "a map with coffee stains",
    "a pocket full of stars"
]

LOCATIONS = [
    "mossy ruins", "a starlit cliff", "a thunderplain", "a hidden glen",
    "an abandoned observatory", "a shallow lagoon", "a wind-swept dune",
    "a neon market"
]

TRAITS = [
    "curious", "shy", "brave", "mischievous", "ancient", "playful",
    "melancholic", "inquisitive", "restless", "gentle"
]

ACTIONS = [
    "collects forgotten songs", "chases sunbeams",
    "trades secrets for berries", "maps the constellations",
    "repairs broken umbrellas", "tells stories to stones",
    "sleeps under ant hills", "teaches lanterns to glow"
]

FORTUNES_POS = [
    "Today you will find a small but meaningful coincidence.",
    "A pleasant surprise waits behind the nearest door.",
    "Someone will say something that will change your plans — for the better."
]

FORTUNES_NEG = [
    "Beware the cookie you did not bake yourself.",
    "An unexpected detour may cost time — and a sock.",
    "A minor embarrassment approaches; smile anyway."
]


def make_name(syllables=3):
    name = "".join(random.choice(SYLLABLES).capitalize() if i == 0 else random.choice(SYLLABLES)
                   for i in range(syllables))
    if random.random() < 0.25:
        name += random.choice(["-ix", "-oo", "-ra", "-eth", "-u"])
    return name


def choose_body():
    template = random.choice(BODIES)
    eyes = random.choice(EYES)
    mouth = random.choice(MOUTHS)
    body = [line.format(E=eyes, M=mouth) for line in template]
    return body


def generate_story(name):
    location = random.choice(LOCATIONS)
    trait = random.choice(TRAITS)
    action = random.choice(ACTIONS)
    accessory = random.choice(ACCESSORIES)
    lines = [
        f"{name} is a {trait} creature found near {location}.",
        f"It often {action} and carries {accessory}.",
        f"Locals say {name} hums when the moons are full."
    ]
    return "\n".join(lines)


def mood_and_fortune():
    mood_score = random.gauss(0, 1)
    if mood_score > 0.5:
        mood = "cheerful"
        fortune = random.choice(FORTUNES_POS)
    elif mood_score < -0.5:
        mood = "grouchy"
        fortune = random.choice(FORTUNES_NEG)
    else:
        mood = "pensive"
        fortune = "A quiet day — observe, then act."
    return mood, fortune


def print_card(name, body_lines, story, mood, fortune):
    border = "=" * 50
    print(border)
    print(f"Creature: {name}    Mood: {mood}")
    print(border)
    for line in body_lines:
        print(line.center(50))
    print("-" * 50)
    wrapped = textwrap.fill(story, width=50)
    print(wrapped)
    print("-" * 50)
    print("Fortune:")
    print(textwrap.fill(fortune, width=50))
    print(border)


def main(runs=1, seed=None, delay=0.25):
    if seed is not None:
        random.seed(seed)
    for i in range(runs):
        name = make_name(random.choice([2, 3, 3, 4]))
        body = choose_body()
        story = generate_story(name)
        mood, fortune = mood_and_fortune()
        print_card(name, body, story, mood, fortune)
        if i != runs - 1:
            time.sleep(delay)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Random Creature & Story generator")
    parser.add_argument("--n", "-n", type=int, default=1, help="how many creatures to generate")
    parser.add_argument("--seed", type=int, default=None, help="seed for deterministic output")
    args = parser.parse_args()
    main(runs=max(1, args.n), seed=args.seed)

    input("\nPress Enter to exit...")
