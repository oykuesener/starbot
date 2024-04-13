import random


def random_string():
    random_list = [
        "Daha basit bir şey yazar mısın?",
        "Bunu henüz anlayamıyorum :(",
        "Çok özür dilerim! Anlayamadım.",
        "Bunu şu an cevaplayamıyorum."
        "Henüz bu kadar gelişmiş değilim ama senin için gelişiyorum!"
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
