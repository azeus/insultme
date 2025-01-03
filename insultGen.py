import random

def generate_insult(name):
    column1 = [
        "artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered",
        "clouted", "craven", "currish", "dankish", "dissembling", "droning",
        "errant", "fawning", "fobbing", "froward", "frothy", "gleeking",
        "goatish", "gorbellied", "impertinent", "infectious", "jarring",
        "loggerheaded", "lumpish", "mammering", "mangled", "mewling", "paunchy",
        "pribbling", "puking", "puny", "quailing", "rank", "reeky", "roguish",
        "ruttish", "saucy", "spleeny", "spongy", "surly", "tottering",
        "unmuzzled", "vain", "venomed", "villainous", "warped", "wayward",
        "weedy", "yeasty"
    ]

    column2 = [
        "base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained",
        "clapper-clawed", "clay-brained", "common-kissing", "crook-pated",
        "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted",
        "earth-vexing", "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed",
        "fly-bitten", "folly-fallen", "fool-born", "full-gorged", "guts-griping",
        "half-faced", "hasty-witted", "hedge-born", "hell-hated", "idle-headed",
        "ill-breeding", "ill-nurtured", "knotty-pated", "milk-livered",
        "motley-minded", "onion-eyed", "plume-plucked", "pottle-deep",
        "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed",
        "shard-borne", "sheep-biting", "spur-galled", "swag-bellied",
        "tardy-gaited", "tickle-brained", "toad-spotted", "urchin-snouted",
        "weather-bitten"
    ]

    column3 = [
        "apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear",
        "bum-bailey", "canker-blossom", "clack-dish", "clotpole", "coxcomb",
        "codpiece", "death-token", "dewberry", "flap-dragon", "flax-wench",
        "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon",
        "haggard", "harpy", "hedge-pig", "horn-beast", "hugger-mugger",
        "jolthead", "lewdster", "lout", "maggot-pie", "malt-worm", "mammet",
        "measle", "minnow", "miscreant", "moldwarp", "mumble-news", "nut-hook",
        "pigeon-egg", "pignut", "puttock", "pumpion", "ratsbane", "scut",
        "skainsmate", "strumpet", "varlet", "vassal", "whey-face", "wagtail"
    ]

    # Randomly select one word from each column
    part1 = random.choice(column1)
    part2 = random.choice(column2)
    part3 = random.choice(column3)

    # Construct the insult
    insult = f"Thou {part1} {part2} {part3}, {name}!"
    return insult

def main():
    print("Welcome to the Shakespearean Insult Generator!")
    name = input("Enter a name to insult: ")
    if name.strip():  # Ensure the name is not empty
        insult = generate_insult(name.strip())
        print("\nHere's your Shakespearean insult:")
        print(insult)
    else:
        print("You need to provide a name to insult!")

if __name__ == "__main__":
    main()