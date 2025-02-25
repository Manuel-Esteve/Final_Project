import random


def missing11():
    teams = {
        "Liverpool (2019 Champions League)": [
            ("GK", "Becker"),
            ("LB", "Robertson"),
            ("CB", "Van Dijk"),
            ("CB", "Matip"),
            ("RB", "Alexander-Arnold"),
            ("CM", "Fabinho"),
            ("CM", "Wijnaldum"),
            ("CM", "Milner"),
            ("LW", "Mane"),
            ("RW", "Salah"),
            ("ST", "Firmino")
        ],
        "Bayern Munich (2020 Champions League)": [
            ("GK", "Neuer"),
            ("LB", "Davies"),
            ("CB", "Boateng"),
            ("CB", "Alaba"),
            ("RB", "Pavard"),
            ("CM", "Kimmich"),
            ("CM", "Goretzka"),
            ("CM", "Muller"),
            ("LW", "Coman"),
            ("RW", "Gnabry"),
            ("ST", "Lewandowski")
        ],
        "Chelsea (2021 Champions League)": [
            ("GK", "Mendy"),
            ("LB", "Azpilicueta"),
            ("CB", "Thiago Silva"),
            ("CB", "Rudiger"),
            ("RB", "James"),
            ("CM", "Jorginho"),
            ("CM", "Kante"),
            ("CM", "Mount"),
            ("LW", "Pulisic"),
            ("RW", "Havertz"),
            ("ST", "Werner")
        ],
        "Real Madrid (2022 Champions League)": [
            ("GK", "Courtois"),
            ("LB", "Mendy"),
            ("CB", "Militao"),
            ("CB", "Alaba"),
            ("RB", "Carvajal"),
            ("CM", "Casemiro"),
            ("CM", "Modric"),
            ("CM", "Kroos"),
            ("LW", "Vinicius"),
            ("RW", "Asensio"),
            ("ST", "Benzema")
        ],
        "Manchester City (2023 Champions League)": [
            ("GK", "Ederson"),
            ("LB", "Stones"),
            ("CB", "Dias"),
            ("CB", "Laporte"),
            ("RB", "Walker"),
            ("CM", "Rodri"),
            ("CM", "De Bruyne"),
            ("CM", "Silva"),
            ("LW", "Foden"),
            ("RW", "Mahrez"),
            ("ST", "Haaland")
        ],
        "Italy (2006 World Cup)": [
            ("GK", "Buffon"),
            ("LB", "Zambrotta"),
            ("CB", "Cannavaro"),
            ("CB", "Materazzi"),
            ("RB", "Grosso"),
            ("CM", "Pirlo"),
            ("CM", "Gattuso"),
            ("CM", "De Rossi"),
            ("LW", "Del Piero"),
            ("RW", "Totti"),
            ("ST", "Toni")
        ],
        "Spain (2010 World Cup)": [
            ("GK", "Casillas"),
            ("LB", "Capdevila"),
            ("CB", "Ramos"),
            ("CB", "Pique"),
            ("RB", "Puyol"),
            ("CM", "Alonso"),
            ("CM", "Xavi"),
            ("CM", "Iniesta"),
            ("LW", "David Villa"),
            ("RW", "Fabregas"),
            ("ST", "Torres")
        ],
        "Germany (2014 World Cup)": [
            ("GK", "Neuer"),
            ("LB", "Lahm"),
            ("CB", "Hummels"),
            ("CB", "Boateng"),
            ("RB", "Howedes"),
            ("CM", "Schweinsteiger"),
            ("CM", "Kroos"),
            ("CM", "Ozil"),
            ("LW", "Götze"),
            ("RW", "Muller"),
            ("ST", "Klose")
        ],
        "France (2018 World Cup)": [
            ("GK", "Lloris"),
            ("LB", "Hernandez"),
            ("CB", "Varane"),
            ("CB", "Umtiti"),
            ("RB", "Pavard"),
            ("CM", "Kante"),
            ("CM", "Pogba"),
            ("CM", "Matuidi"),
            ("LW", "Griezmann"),
            ("RW", "Mbappe"),
            ("ST", "Giroud")
        ],
        "Argentina (2022 World Cup)": [
            ("GK", "Martinez"),
            ("LB", "Acuña"),
            ("CB", "Romero"),
            ("CB", "Otamendi"),
            ("RB", "Molina"),
            ("CM", "De Paul"),
            ("CM", "Paredes"),
            ("CM", "Mac Allister"),
            ("LW", "Di Maria"),
            ("RW", "Messi"),
            ("ST", "Martínez")
        ]
    }
    # Teams with positions defined in order: GK, LB, CB, CB, RB, CM, CM, CM, LW, RW, ST.

    # Randomly select a team.
    team_name, lineup = random.choice(list(teams.items()))
    print(f"Guess the starting 11 for {team_name}!")
    print("Enter player names one by one. (Type 'quit' to exit)\n")

    guessed = set()
    attempts = 0
    while len(guessed) < 11:
        guess = input("Your guess: ").strip()
        if guess.lower() == "quit":
            print("Game exited.")
            return
        attempts += 1
        normalized_guess = guess.lower()
        found = False

        # Check the guess against each player's name.
        for pos, player in lineup:
            if player.lower() == normalized_guess:
                if player in guessed:
                    print(f"You already guessed {player}.")
                else:
                    guessed.add(player)
                    print(f"Correct! {player} plays as {pos}.")
                found = True
                break

        if not found:
            print("Incorrect guess.")

        # Display the full lineup with positions, showing "???" for unguessed players.
        print("\nCurrent lineup:")
        for pos, player in lineup:
            if player in guessed:
                print(f"{pos}: {player}")
            else:
                print(f"{pos}: ???")
        print(f"\n{len(guessed)}/11 players found.\n")

    print(f"Congratulations! You completed the lineup in {attempts} guesses.")
    print("\nThe full starting 11 was:")
    for pos, player in lineup:
        print(f"{pos}: {player}")


if __name__ == "__main__":
    missing11()
