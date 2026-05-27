import time
import random
from utils import digitar, secao, titulo, pausa, escolha, game_over, limpar_tela

MAX_TURNOS = 10

def mostrar_status_batalha(heroi, vilao):
    print("\n" + "═" * 60)
    print(f"  {heroi.status()}")
    print(f"  {vilao.status()}")
    print("═" * 60)

def mostrar_turno(turno, heroi, vilao):
    titulo(f"⚔️  TURNO {turno}/{MAX_TURNOS}  ⚔️", "─")
    mostrar_status_batalha(heroi, vilao)

def batalha(heroi, vilao, modo_dificil=False, modo_final=False):
    """Sistema de batalha por turnos."""
    limpar_tela()
    titulo(f"⚔️  BATALHA: {heroi.nome} vs {vilao.nome}  ⚔️")
    digitar(f"\n  {vilao.descricao}", cor="vermelho", velocidade=0.04)
    pausa()

    turno = 0
    while heroi.esta_vivo() and vilao.esta_vivo() and turno < MAX_TURNOS:
        turno += 1
        limpar_tela()
        mostrar_turno(turno, heroi, vilao)

        # Adversário anuncia o próximo ataque
        proximo_ataque_vilao = vilao.escolher_ataque()
        secao(f"📢 {vilao.nome} se prepara para: {proximo_ataque_vilao['nome']}!")
        digitar(f"  \"{proximo_ataque_vilao['descricao']}\"", cor="vermelho", velocidade=0.03)
        pausa()
        mostrar_turno(turno, heroi, vilao)

        # Turno do player
        if modo_final:
            _turno_player_final(heroi, vilao)
        else:
            _turno_player(heroi, vilao)
        pausa()

        if not vilao.esta_vivo():
            break

        # Turno do vilão
        mostrar_turno(turno, heroi, vilao)
        ataque_usado, dano_real = vilao.atacar(heroi)
        secao(f"💥 {vilao.nome} usa {ataque_usado['nome']}!")

        # Verificar ataque especial pokemon (hit kill no modo difícil)
        if ataque_usado.get("especial") == "pokemon" and modo_dificil:
            digitar("\n  ❓ Cleyton mostra uma silhueta misteriosa...", velocidade=0.04)
            opcoes_pokemon = [" Pikachu", " Bulbasaur", " Snorlax"]
            escolhido = escolha(opcoes_pokemon, "Qual é esse Pokémon?")
            time.sleep(0.5)
            digitar(f"\n  Prof. Cleyton: \"ERRADO! Você é o Pokémon reprovado!\"", cor="amarelo", velocidade=0.04)
            digitar("  (A resposta certa era: VOCÊ REPROVADO — não importa o que escolher)", cor="vermelho")
            game_over("O ataque Pokémon de Cleyton foi letal no modo Super Difícil!", heroi)
        elif ataque_usado.get("especial") == "pokemon":
            digitar("\n  ❓ Cleyton mostra uma silhueta misteriosa...", velocidade=0.04)
            opcoes_pokemon = [" Pikachu", " Bulbasaur", " Snorlax"]
            escolhido = escolha(opcoes_pokemon, "Qual é esse Pokémon?")
            time.sleep(0.5)
            digitar(f"\n  Prof. Cleyton: \"ERRADO! Você é o Pokémon reprovado!\"", cor="amarelo", velocidade=0.04)
            digitar("  (Sorte que você não está no modo Super Difícil...)", cor="verde")
            dano_real = heroi.receber_dano(30)

        digitar(f"\n  {ataque_usado['descricao']}", cor="vermelho", velocidade=0.03)
        if dano_real > 0:
            digitar(f"  Você sofreu {dano_real} de dano!", cor="vermelho")

        heroi.resetar_defesa()

        if not heroi.esta_vivo():
            digitar(f"\n  💀 {heroi.nome} foi derrotado por {vilao.nome}!", cor="vermelho")
            pausa()
            game_over(f"Você foi derrotado por {vilao.nome}.", heroi)

        pausa()

    # Resultado
    if vilao.esta_vivo() and turno >= MAX_TURNOS:
        limpar_tela()
        titulo("🏃 VOCÊ SOBREVIVEU!")
        digitar(f"\n  Você aguentou {MAX_TURNOS} turnos contra {vilao.nome}!", cor="verde")
        digitar("  O adversário desistiu de te expulsar. Vitória técnica!\n", cor="verde")
        heroi.registrar(f"Sobreviveu {MAX_TURNOS} turnos contra {vilao.nome}")
        heroi.vida = heroi.vida_maxima
        pausa()
        return True
    elif not vilao.esta_vivo():
        limpar_tela()
        titulo("🏆 VITÓRIA!")
        digitar(f"\n  Você derrotou {vilao.nome}!", cor="verde")
        heroi.registrar(f"Derrotou {vilao.nome}")
        heroi.vida = heroi.vida_maxima
        pausa()
        return True

    return False


def _turno_player(heroi, vilao):
    print("\n  O que você vai fazer?")
    nomes_ataques = [a["nome"] for a in heroi.ataques]
    if heroi.escudo_usos <= 0:
        nomes_ataques[1] = f"{nomes_ataques[1]} (SEM USOS)"
    nomes_ataques.append("🍵 Esperar e Rezar (pula o turno)")

    opcao = escolha(nomes_ataques, "Escolha sua ação")

    if opcao == len(heroi.ataques):
        digitar("\n  Você fecha os olhos e reza pro sistema de créditos não cair...", velocidade=0.04)
        return

    dano, msg = heroi.usar_ataque(opcao, vilao)
    if dano is None:
        digitar(f"\n  {msg}", cor="vermelho")
    else:
        secao(f"🎯 {heroi.nome} usa {heroi.ataques[opcao]['nome']}!")
        digitar(f"\n  {msg}", cor="verde" if dano > 0 else "azul")


def _turno_player_final(heroi, vilao):
    print("\n  Escolha seu código errado:")
    nomes_ataques = [f"{a['nome']} — Grotesco nível {a['nivel_grotesco']}" for a in heroi.ataques_finais]
    nomes_ataques.append("🙏 Implorar por Misericórdia (pula o turno)")

    opcao = escolha(nomes_ataques, "Escolha seu ataque de código bugado")

    if opcao == len(heroi.ataques_finais):
        digitar("\n  Você olha pro Cleyton com aquele olhar de 'por favor professor...'", velocidade=0.04)
        digitar("  Ele ignora solenemente.", velocidade=0.04)
        return

    ataque = heroi.ataques_finais[opcao]
    dano = random.randint(ataque["dano_min"], ataque["dano_max"])
    dano_real = vilao.receber_dano(dano)
    secao(f"💻 {heroi.nome} apresenta: {ataque['nome']}!")
    digitar(f"\n  {ataque['descricao']}", cor="ciano", velocidade=0.03)
    digitar(f"  Prof. Cleyton sofreu {dano_real} de dano intelectual!", cor="verde")
    heroi.registrar(f"Usou {ataque['nome']}: {dano_real} dano")
