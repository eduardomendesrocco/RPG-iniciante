import random
import os
import pygame

classes_str = {
    "1": "Guerreiro",
    "2": "Mago",
    "3": "Arqueiro",
    "4": "Curandeiro",
    "5": "Espadachim",
    "6": "Ninja",
    "7": "Lutador"
}

mapas_str = {
    "1": "Floresta",
    "2": "Deserto",
    "3": "Caverna",
    "4": "Montanhas Gélidas",
    "5": "Vulcão",
    "6": "Ninho dos Dragões"
}

def tocar_musica(mapa):
    if mapa == "Floresta":
        return 0

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def player_creation():
    clear_terminal()
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

    if nome_jogador and classe_escolhida and status_jogador:
        choose_map()

mapas_desbloqueados = []

def choose_map():
    clear_terminal()
    print(f"| Mapas\n"
          f"| "
          f"\n| Floresta          -> 1"
          f"\n| Deserto           -> 2"
          f"\n| Caverna           -> 3"
          f"\n| Montanhas Gélidas -> 4"
          f"\n| Vulcão            -> 5"
          f"\n| Ninho dos Dragões -> 6")

    if mapas_desbloqueados:
        mapa_escolhido = input("Escolha um mapa para se aventurar -> ")
        while mapa_escolhido not in mapas_desbloqueados:
            print(f"\nMapa ainda não desbloqueado, enfrente os anteriores para desbloquear mais mapas.")
            mapa_escolhido = input("Escolha um mapa para se aventurar -> ")
        game()
    else:
        mapas_desbloqueados.append(mapas_str["1"])
        return choose_map()

    return mapa_escolhido

def game():


    return 0

turnos = 0
turno_atual = 1
### Ideia: contar turnos normalmente a cada ataque e contar ondas/waves a cada monstro derrotado!

if __name__ == "__main__":
    player_creation()
