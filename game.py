import random

classes_str = {
    "1": "Guerreiro",
    "2": "Mago",
    "3": "Arqueiro",
    "4": "Curandeiro",
    "5": "Espadachim",
    "6": "Ninja",
    "7": "Lutador"
}

def player_creation():

    nome_jogador = input("Olá, qual o seu nickname? -> ")
    print(f"| Seja bem-vindo, {nome_jogador}!\n"
          f"| "
          f"\n| Guerreiro  -> 1"
          f"\n| Mago       -> 2"
          f"\n| Arqueiro   -> 3"
          f"\n| Curandeiro -> 4"
          f"\n| Espadachim -> 5"
          f"\n| Ninja      -> 6"
          f"\n| Lutador    -> 7")

    classe_escolhida = input("Escolha uma das classes acima -> ")
    while classe_escolhida not in classes_str:
        classe_escolhida = input("Digite uma classe existente! -> ")

    status_classes = {
        "Guerreiro": {
            "nome": nome_jogador,
            "hp": 125,
            "dmg": 12,
            "def": 5,
            "dodge_chance": 0.02,
            "crit_chance": 0.10,
            "crit_dmg": 1.20
        }, # ==================
        "Mago": {
            "nome": nome_jogador,
            "hp": 60,
            "dmg": 15,
            "def": 2,
            "dodge_chance": 0.02,
            "crit_chance": 0.20,
            "crit_dmg": 1.20
        }, # ==================
        "Arqueiro": {
            "nome": nome_jogador,
            "hp": 75,
            "dmg": 10,
            "def": 3,
            "dodge_chance": 0.10,
            "crit_chance": 0.20,
            "crit_dmg": 1.15
        },  # ==================
        "Curandeiro": {
            "nome": nome_jogador,
            "hp": 100,
            "dmg": 2,
            "def": 4.5,
            "dodge_chance": 0.07,
            "crit_chance": 0.05,
            "crit_dmg": 1.30
        },  # ==================
        "Espadachim": {
            "nome": nome_jogador,
            "hp": 130,
            "dmg": 19.5,
            "def": 3.5,
            "dodge_chance": 0.15,
            "crit_chance": 0.22,
            "crit_dmg": 1.25
        },  # ==================
        "Ninja": {
            "nome": nome_jogador,
            "hp": 80,
            "dmg": 12,
            "def": 2,
            "dodge_chance": 0.25,
            "crit_chance": 0.50,
            "crit_dmg": 1.10
        },  # ==================
        "Lutador": {
            "nome": nome_jogador,
            "hp": 135,
            "dmg": 17,
            "def": 3,
            "dodge_chance": 0.15,
            "crit_chance": 0.10,
            "crit_dmg": 1.30
        },  # ==================
    }

    status_jogador = status_classes[classes_str[classe_escolhida]]

turnos = 0
turno_atual = 1
### Ideia: contar turnos normalmente a cada ataque e contar ondas/waves a cada monstro derrotado!

if __name__ == "__main__":
    player_creation()