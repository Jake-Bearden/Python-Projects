import requests

def get_card_data(card_name):
    url = "https://api.scryfall.com/cards/named"
    params = {"fuzzy": card_name}

    headers = {
        "User-Agent": "MTGDeckAnalyzer/1.0",
        "Accept": "application/json"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=15
        )

        print("Status Code:", response.status_code)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)
        return None

def display_card(card):
    """Display useful information about a Magic card."""

    print("\n" + "=" * 40)
    print("CARD INFORMATION")
    print("=" * 40)

    print("Name:", card["name"])
    print("Mana Cost:", card.get("mana_cost", "N/A"))
    print("Type:", card["type_line"])
    print("Color Identity:", card.get("color_identity", []))
    print("Rarity:", card["rarity"])

    if "prices" in card:
        print("USD Price:", card["prices"].get("usd"))

    print("\nRules Text:")
    print(card.get("oracle_text", "No rules text available."))

    print("=" * 40)


def main():
    print("=" * 40)
    print("       MTG DECK ANALYZER")
    print("=" * 40)

    while True:
        card_name = input("\nEnter a card name (or 'quit'): ")

        if card_name.lower() == "quit":
            print("Thanks for using MTG Deck Analyzer!")
            break

        if not card_name.strip():
            print("Please enter a card name.")
            continue

        card = get_card_data(card_name)

        if card:
            display_card(card)


if __name__ == "__main__":
    main()