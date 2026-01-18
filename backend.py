import random

name = input("What is your name? ")

print(f"Good Luck ! {name}. this is a League of Legends champion guessing game")

words = ["aatrox", "ahri", "akali", "akshan", "alistar", "ambessa", "amumu",
  "anivia", "annie", "aphelios", "ashe", "aurelion sol", "aurora", "azir",
  "bard", "bel'veth", "blitzcrank", "brand", "braum", "briar", "caitlyn",
  "camille", "cassiopeia", "cho'gath", "corki", "darius", "diana", "dr. mundo",
  "draven", "ekko", "elise", "evelynn", "ezreal", "fiddlesticks", "fiora",
  "fizz", "galio", "gangplank", "garen", "gnar", "gragas", "graves"
  "hecarim", "heimerdinger", "hwei", "illaoi", "irelia", "ivern", "janna",
  "jarvan iv", "jax", "jayce", "jhin", "jinx", "kai'sa", "kalista", "karma",
  "karthus", "kassadin", "katarina", "kayle", "kayn", "kennen", "kha'zix",
  "kindred", "kled", "kog'maw", "k'sante", "lillia", "leblanc", "lee sin",
  "leona", "lucian", "lulu", "lux", "malphite", "malzahar", "maokai", "mel",
  "milio", "miss fortune" , "sona", "soraka", "swain", "sylas", "syndra", "tahm kench", "taliyah", "talon",
  "taric", "teemo", "thresh", "tristana", "trundle", "tryndamere", "twisted fate",
  "twitch", "udyr", "urgot", "varus", "vayne", "veigar"  "vel'koz",
  "vex","vi","viego","viktor","vladimir","volibear","warwick","wukong","xayah",
  "xerath","xin zhao","yasuo","yone","yorick","yuumi","zac","zed","zeri","ziggs",
  "zilean","zoe","zyra"]

champion_abilities = {
    "aatrox": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "ahri": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "akali": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "akshan": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "alistar": {"q": "utility", "w": "utility", "e": "dmg", "r": "support"},
    "ambessa": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "amumu": {"q": "utility", "w": "dmg", "e": "dmg", "r": "utility"},
    "anivia": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "annie": {"q": "dmg", "w": "dmg", "e": "support", "r": "dmg"},
    "aphelios": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "ashe": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "aurelion sol": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "aurora": {"q": "dmg", "w": "utility", "e": "dmg", "r": "utility"},
    "azir": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},

    "bard": {"q": "utility", "w": "support", "e": "utility", "r": "utility"},
    "bel'veth": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "blitzcrank": {"q": "utility", "w": "utility", "e": "dmg", "r": "utility"},
    "brand": {"q": "dmg", "w": "dmg", "e": "dmg", "r": "dmg"},
    "braum": {"q": "utility", "w": "support", "e": "support", "r": "utility"},
    "briar": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},

    "caitlyn": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "camille": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "cassiopeia": {"q": "dmg", "w": "utility", "e": "dmg", "r": "utility"},
    "cho'gath": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "corki": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},

    "darius": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "diana": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "dr. mundo": {"q": "dmg", "w": "support", "e": "dmg", "r": "support"},
    "draven": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},

    "ekko": {"q": "dmg", "w": "utility", "e": "dmg", "r": "utility"},
    "elise": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "evelynn": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "ezreal": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},

    "fiddlesticks": {"q": "utility", "w": "dmg", "e": "utility", "r": "dmg"},
    "fiora": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "fizz": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},

    "galio": {"q": "dmg", "w": "utility", "e": "utility", "r": "utility"},
    "gangplank": {"q": "dmg", "w": "support", "e": "dmg", "r": "utility"},
    "garen": {"q": "dmg", "w": "support", "e": "dmg", "r": "dmg"},
    "gnar": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "gragas": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "graves": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},

    "hecarim": {"q": "dmg", "w": "support", "e": "utility", "r": "utility"},
    "heimerdinger": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "hwei": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},

    "illaoi": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "irelia": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "ivern": {"q": "utility", "w": "support", "e": "support", "r": "support"},

    "janna": {"q": "utility", "w": "utility", "e": "support", "r": "support"},
    "jarvan iv": {"q": "dmg", "w": "support", "e": "dmg", "r": "utility"},
    "jax": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "jayce": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "jhin": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "jinx": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},

    "kai'sa": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "kalista": {"q": "dmg", "w": "utility", "e": "dmg", "r": "utility"},
    "karma": {"q": "dmg", "w": "utility", "e": "support", "r": "utility"},
    "karthus": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "kassadin": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "katarina": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "kayle": {"q": "dmg", "w": "support", "e": "dmg", "r": "support"},
    "kayn": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "kennen": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "kha'zix": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "kindred": {"q": "dmg", "w": "utility", "e": "utility", "r": "support"},
    "kled": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "kog'maw": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "k'sante": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},

    "lillia": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "leblanc": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "lee sin": {"q": "dmg", "w": "support", "e": "utility", "r": "utility"},
    "leona": {"q": "utility", "w": "support", "e": "utility", "r": "utility"},
    "lucian": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "lulu": {"q": "utility", "w": "support", "e": "support", "r": "support"},
    "lux": {"q": "dmg", "w": "support", "e": "utility", "r": "dmg"},

    "malphite": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "malzahar": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "maokai": {"q": "utility", "w": "utility", "e": "utility", "r": "utility"},
    "mel": {"q": "dmg", "w": "support", "e": "utility", "r": "dmg"},
    "milio": {"q": "support", "w": "support", "e": "support", "r": "support"},
    "miss fortune": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},

    "sona": {"q": "support", "w": "support", "e": "support", "r": "utility"},
    "soraka": {"q": "dmg", "w": "support", "e": "utility", "r": "support"},
    "swain": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "sylas": {"q": "dmg", "w": "support", "e": "utility", "r": "dmg"},
    "syndra": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},

    "tahm kench": {"q": "utility", "w": "utility", "e": "support", "r": "utility"},
    "taliyah": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "talon": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "taric": {"q": "support", "w": "support", "e": "utility", "r": "support"},
    "teemo": {"q": "utility", "w": "utility", "e": "dmg", "r": "dmg"},
    "thresh": {"q": "utility", "w": "support", "e": "utility", "r": "utility"},
    "tristana": {"q": "dmg", "w": "utility", "e": "dmg", "r": "utility"},
    "trundle": {"q": "dmg", "w": "support", "e": "utility", "r": "utility"},
    "tryndamere": {"q": "support", "w": "utility", "e": "dmg", "r": "support"},
    "twisted fate": {"q": "dmg", "w": "utility", "e": "utility", "r": "utility"},
    "twitch": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},

    "udyr": {"q": "dmg", "w": "support", "e": "utility", "r": "dmg"},
    "urgot": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},

    "varus": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "vayne": {"q": "utility", "w": "dmg", "e": "utility", "r": "dmg"},
    "veigar": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "vel'koz": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "vex": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "vi": {"q": "dmg", "w": "dmg", "e": "dmg", "r": "utility"},
    "viego": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "viktor": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "vladimir": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "volibear": {"q": "dmg", "w": "dmg", "e": "support", "r": "dmg"},

    "warwick": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "wukong": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},

    "xayah": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},
    "xerath": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "xin zhao": {"q": "dmg", "w": "dmg", "e": "utility", "r": "utility"},

    "yasuo": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "yone": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "yorick": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "yuumi": {"q": "dmg", "w": "support", "e": "support", "r": "support"},

    "zac": {"q": "utility", "w": "dmg", "e": "utility", "r": "utility"},
    "zed": {"q": "dmg", "w": "utility", "e": "dmg", "r": "dmg"},
    "zeri": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "ziggs": {"q": "dmg", "w": "dmg", "e": "utility", "r": "dmg"},
    "zilean": {"q": "dmg", "w": "utility", "e": "support", "r": "support"},
    "zoe": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"},
    "zyra": {"q": "dmg", "w": "utility", "e": "utility", "r": "dmg"}
}

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end=" ")

        else: 
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("You Win")
        print("The word is: ", word)

        print(f"now its time to for a quiz about {word}'s abilities!")
        abilities = champion_abilities.get(word, {})
        for ability, ability_type in abilities.items():
            answer = input(f"What type of ability is {ability.upper()}? (dmg/utility/support): ")
            if answer.lower() == ability_type:
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {ability_type}.")
                turns -= 1
                print(f"You have {turns} more guesses")
        break
       
    

    print()
    guess = input("guess a character:")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print(f"You have {turns} more guesses")

        if turns == 0:
            print("You Lose")