import time
import random
import sys
import os

# ===================== FORMATAÇÃO =====================

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def digitar(texto, velocidade=0.03, cor=None):
    """Imprime texto com efeito de digitação."""
    cores = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "magenta": "\033[95m",
        "ciano": "\033[96m",
        "branco": "\033[97m",
        "negrito": "\033[1m",
        "reset": "\033[0m"
    }
    inicio = cores.get(cor, "") if cor else ""
    fim = cores["reset"] if cor else ""
    print(inicio, end="")
    for char in texto:
        print(char, end="", flush=True)
        time.sleep(velocidade)
    print(fim)

def titulo(texto, simbolo="═"):
    largura = 60
    print("\n" + simbolo * largura)
    print(texto.center(largura))
    print(simbolo * largura + "\n")

def secao(texto):
    print(f"\n{'─' * 60}")
    print(f"  {texto}")
    print('─' * 60)

def pausa(msg="", limpar=True):
    if msg:
        print(f"\n{msg}")
    input("\n  [ENTER para continuar...]\n")
    if limpar:
        limpar_tela()

def escolha(opcoes, titulo_menu=None):
    """Apresenta um menu de escolha e retorna o índice escolhido."""
    if titulo_menu:
        secao(titulo_menu)
    for i, op in enumerate(opcoes, 1):
        print(f"  [{i}] {op}")
    while True:
        try:
            escolha = int(input("\n  Sua escolha: "))
            if 1 <= escolha <= len(opcoes):
                return escolha - 1
            print("  ❌ Opção inválida! Tente novamente.")
        except ValueError:
            print("  ❌ Digite um número válido!")

def game_over(motivo, heroi=None):
    limpar_tela()
    titulo("💀 GAME OVER 💀", "═")
    digitar(f"\n  {motivo}", cor="vermelho")
    if heroi:
        print(f"\n  Seu personagem {heroi.nome} não chegou à UFRPE hoje.")
        print(f"  Histórico de ações: {len(heroi.historico)} eventos registrados.")
    print("\n  O professor Cleyton vai ter que dar aula sem você... ")
    print("  Que alívio. (para ele)\n")
    pausa("  Pressione ENTER para encerrar.")
    sys.exit(0)

def vitoria_final(heroi):
    limpar_tela()
    titulo("🎉 PARABÉNS! VOCÊ CONSEGUIU! 🎉", "★")
    digitar("\n  Prof. Cleyton olha para o seu código final...", velocidade=0.05)
    time.sleep(1)
    digitar("  Ele coça a cabeça.", velocidade=0.05)
    time.sleep(0.5)
    digitar("  Ele suspira fundo.", velocidade=0.05)
    time.sleep(0.5)
    digitar("\n  Prof. Cleyton:", cor="amarelo")
    digitar(f'  "Bom... {heroi.nome}... Isso foi... criativo."', velocidade=0.05, cor="amarelo")
    time.sleep(0.7)
    digitar('  "Tecnicamente errado em 11 lugares diferentes..."', velocidade=0.05, cor="amarelo")
    time.sleep(0.7)
    digitar('  "...mas a ideia estava lá. Acho."', velocidade=0.05, cor="amarelo")
    time.sleep(1)
    digitar('\n  Ele digita algo no sistema...', velocidade=0.04)
    time.sleep(1.5)
    digitar('\n  ✨ NOTA LANÇADA: 7.0 ✨', cor="verde")
    time.sleep(0.5)
    digitar('  (Mínimo pra passar. Mas você passou!)\n', cor="verde")
    time.sleep(1)
    titulo("📜 HISTÓRICO DE BATALHA", "─")
    print(f"  Eventos registrados: {len(heroi.historico)}")
    for ev in heroi.historico[-5:]:
        print(f"  • {ev}")
    print("\n  🎓 Fim de jogo. Você sobreviveu a mais um dia de aula na UFRPE.\n")

def evento_aleatorio(chance, descricao, heroi, e_game_over=False, dano=0):
    """Retorna True se o evento aconteceu."""
    if random.random() < chance:
        secao(f"⚠️ EVENTO ALEATÓRIO!")
        digitar(f"\n  {descricao}", velocidade=0.04, cor="amarelo")
        if e_game_over:
            time.sleep(1.5)
            game_over(descricao, heroi)
        elif dano > 0:
            heroi.receber_dano(dano)
            digitar(f"\n  Você perdeu {dano} pontos de vida!", cor="vermelho")
            if not heroi.esta_vivo():
                game_over("Você não resistiu aos ferimentos.", heroi)
        pausa()
        return True
    return False
