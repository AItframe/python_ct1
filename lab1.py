import random

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")

bye_count = 0

while True:
    u_input = input("> ").strip()

    if not u_input:
        continue

    if u_input == "ПОКА!":
        bye_count += 1
    else:
        bye_count = 0
    
    
    if bye_count == 3:
        print("ДО СВИДАНИЯ, МИЛЫЙ!")
        break

    if u_input.isupper():
        year = random.randint(1930, 1950)
        print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")