import time
import random
import sys
from heroi import Heroi
from vilao import (criar_guarda_metro, criar_motorista, criar_guarda_onibus, criar_professor_cleyton)
from utils import (digitar, secao, titulo, pausa, escolha, game_over,
                   evento_aleatorio, vitoria_final, limpar_tela)
from batalha import batalha

# ================================================================
#  INTRODUÇÃO E SETUP
# ================================================================

def introducao():
    limpar_tela()
    titulo("🚌  UFRPE OU BUST  🚌", "★")
    digitar("  Um jogo sobre sobrevivência urbana de um universitário da UFRPE.", cor="ciano")
    digitar("  Criado com base no projeto da disciplina de Princípios de Programação", cor="ciano")
    digitar("  UFRPE — Departamento de Estatística e Informática\n", cor="ciano")
    time.sleep(0.5)

    digitar("  Era uma quinta-feira. Mais uma quinta-feira.", velocidade=0.04)
    digitar("  O sol ainda nem surgiu direito às 5 da manhã em Marcos Freire.", velocidade=0.04)
    digitar("  O alarme tocou. Você ignorou. Três vezes.", velocidade=0.04)
    digitar("  Na quarta, você lembrou: PROVA DE POO HOJE.", velocidade=0.04, cor="vermelho")
    time.sleep(0.5)
    digitar("\n  Você mora em Marcos Freire.", velocidade=0.05)
    digitar("  O destino: Campus da UFRPE — Dois Irmãos.", velocidade=0.05)
    digitar("  O problema: seus bolsos estão mais vazios que o SIGAA às 23h59.", velocidade=0.05, cor="amarelo")
    pausa()

def pedir_nome():
    limpar_tela()
    titulo("👤 CRIAR PERSONAGEM")
    print("  Como você se chama, corajoso estudante?\n")
    while True:
        nome = input("  Seu nome: ").strip()
        if nome:
            return nome
        print("  ❌ Você precisa de um nome! (Até estudante sem nota tem nome)")

def escolher_caminho(heroi):
    limpar_tela()
    titulo("🗺️  ESCOLHA SEU DESTINO")
    digitar(f"\n  {heroi.nome}, você acorda e olha pro teto.", velocidade=0.04)
    digitar("  O desespero bate. A prova bate mais forte.", velocidade=0.04)
    digitar("\n  Dois caminhos surgem na sua mente confusa:", velocidade=0.04)
    time.sleep(0.5)

    opcoes = [
        "🚌 Terminal do Barro — (Dificuldade: SUPER DIFÍCIL 💀)",
        "🚇 Terminal Tancredo Neves — (Dificuldade: DIFÍCIL 😰)",
        "🛌 Não ir — (Dificuldade: FÁCIL — mas você reprovará)"
    ]

    escolhido = escolha(opcoes, "Qual caminho você escolhe?")

    if escolhido == 0:
        return "barro", True   # super difícil
    elif escolhido == 1:
        return "tancredo", False  # difícil
    else:
        limpar_tela()
        titulo("😴 FIM DE JOGO: A ESCOLHA DO COVARDE")
        digitar("\n  Você apagou o alarme e voltou a dormir.", velocidade=0.04)
        digitar("  A prova aconteceu. Você não estava lá.", velocidade=0.04)
        digitar("  O professor Cleyton olhou pra lista de chamada...", velocidade=0.04)
        digitar(f"  ...riscou {heroi.nome} com caneta vermelha.", cor="vermelho")
        digitar("\n  REPROVADO por falta. Parabéns.", cor="vermelho")
        digitar("\n  (Às vezes a única batalha que você pode ganhar é a de não ir.)", cor="amarelo")
        digitar("  Mas isso não é um final feliz.\n")
        pausa()
        sys.exit(0)

# ================================================================
#  ROTA DO BARRO (SUPER DIFÍCIL)
# ================================================================

def rota_barro(heroi):
    limpar_tela()
    titulo("🚌 ROTA DO BARRO — SUPER DIFÍCIL")
    digitar("\n  Você decide enfrentar a BR-101.", velocidade=0.04)
    digitar("  O ônibus da linha Marcos Freire–Cajueiro Seco já está saindo.", velocidade=0.04)
    digitar("  Você corre. Grita. O motorista fecha a porta na sua cara.", velocidade=0.04)
    digitar("  E reabre. Milagre.\n", cor="verde")
    pausa()

    # --- CENA 1: Ônibus Marcos Freire – Cajueiro Seco ---
    limpar_tela()
    secao("🚌 CENA 1: Ônibus Marcos Freire → Cajueiro Seco")
    digitar("\n  O ônibus está lotado. Seu rosto está colado no vidro embaçado.", velocidade=0.04)
    digitar("  Um senhor com bolsa de feira resolve apoiar o cotovelo nas suas costelas.", velocidade=0.04)
    digitar("  O fiscal de ônibus aparece do nada, olhando torto pra você.\n", velocidade=0.04)

    # Evento aleatório — BR-101 engarrafada
    if evento_aleatorio(0.25,
        "⚠️ A BR-101 está completamente parada. Engarrafamento total. O motorista desliga o motor.",
        heroi, e_game_over=True):
        return

    # Evento aleatório — cachorro no terminal
    if evento_aleatorio(0.20,
        "🐕 Um cachorro vira-lata raivoso invadiu o ônibus e foi direto pra você. MORDE TUDO.",
        heroi, e_game_over=True):
        return

    digitar("\n  O fiscal de ônibus está te olhando de cabeça a pé...", velocidade=0.04, cor="amarelo")
    pausa("  O que você faz?")
    opcoes = ["🎫 Tentar mostrar um print de comprovante falso", "🤫 Fingir que está dormindo", "🏃 Tentar passar sem pagar"]
    opcao = escolha(opcoes)

    if opcao == 2:
        digitar("\n  Você tenta pular a catraca.", velocidade=0.04)
        if random.random() < 0.5:
            digitar("  O motorista te viu pelo espelho retrovisor!", cor="vermelho")
            digitar("  Ele para o ônibus no meio da pista e te expulsa.", cor="vermelho")
            game_over("Expulso do ônibus por tentar pular a catraca.", heroi)
        else:
            digitar("  O motorista estava olhando o celular. Passou!", cor="verde")

    vilao1 = criar_guarda_onibus()
    pausa()
    batalha(heroi, vilao1, modo_dificil=True)

    # --- CENA 2: Ônibus Cajueiro Seco – Barro ---
    limpar_tela()
    secao("🚌 CENA 2: Ônibus Cajueiro Seco → Barro")
    digitar("\n  Você chegou em Cajueiro Seco.", velocidade=0.04)
    digitar("  O próximo ônibus está cheio de gente. Nenhuma novidade.", velocidade=0.04)
    digitar("  Uma senhora com perfume forte ocupa o espaço do seu nariz.\n", velocidade=0.04)

    if evento_aleatorio(0.30,
        "🌡️ O calor dentro do ônibus chegou a 45°C. Você sufoca e desmaia antes de chegar.",
        heroi, e_game_over=True):
        return

    if evento_aleatorio(0.15,
        "🐕 Ao chegar no Terminal do Barro, um cachorro raivoso te ataca na saída do ônibus!",
        heroi, e_game_over=True):
        return

    if evento_aleatorio(0.20,
        "📋 No Terminal do Barro, a fila para o próximo ônibus era quilométrica. Você desistiu.",
        heroi, e_game_over=True):
        return

    vilao2 = criar_motorista()
    pausa()
    batalha(heroi, vilao2, modo_dificil=True)

    # --- CENA 3: Ônibus Barro – Macaxeira (Várzea) ---
    limpar_tela()
    secao("🚌 CENA 3: Ônibus Barro → Macaxeira (Várzea)")
    digitar("\n  O ônibus da Várzea. Famoso. Histórico. Assustador.", velocidade=0.04)
    digitar("  O motorista faz curvas como se estivesse num videogame de corrida.", velocidade=0.04)
    digitar("  Um guarda sobe conferindo passagens com olhar de delegado.\n", velocidade=0.04)

    evento_ocorreu = False
    if evento_aleatorio(0.20,
        "💥 O ônibus bateu numa lombada com toda força. Você voou do banco. Dano físico e espiritual.",
        heroi, dano=25):
        evento_ocorreu = True

    if evento_aleatorio(0.10,
        "🤯 O motorista errou o caminho e acabou indo pra o Ibura. Game Over.",
        heroi, e_game_over=True):
        return

    vilao3 = criar_guarda_onibus()
    vilao3.nome = "Guarda da Várzea"
    vilao3.descricao = "Um guarda experiente e sem paciência pra desculpa de universitário."
    if not evento_ocorreu:
        pausa()
    batalha(heroi, vilao3, modo_dificil=True)

    digitar("\n  🎉 Você chegou no Ceagri 2! A UFRPE está à vista!", cor="verde")
    pausa()

# ================================================================
#  ROTA DE TANCREDO (DIFÍCIL)
# ================================================================

def rota_tancredo(heroi):
    limpar_tela()
    titulo("🚇 ROTA DE TANCREDO — DIFÍCIL")
    digitar("\n  Você escolheu o caminho do VLT + Metrô.", velocidade=0.04)
    digitar("  Mais confortável. Em teoria.", velocidade=0.04)
    digitar("  O VLT de Marcos Freire sai em 10 minutos. Você corre.\n", velocidade=0.04)
    pausa()

    # --- CENA 1: VLT Marcos Freire – Cajueiro Seco ---
    limpar_tela()
    secao("🚃 CENA 1: VLT Marcos Freire → Cajueiro Seco")
    digitar("\n  O VLT está cheio de gente séria, cabeça baixa, fone no ouvido.", velocidade=0.04)
    digitar("  Um guardinha de colete laranja faz a ronda, olhando cada passageiro.", velocidade=0.04)
    digitar("  Você não tem crédito no cartão.\n", velocidade=0.04, cor="amarelo")

    opcoes = ["🎭 Tentar entrar discretamente sem ser notado", "💳 Inventar que o cartão está com problema"]
    opcao = escolha(opcoes, "O que você faz?")

    if opcao == 0:
        digitar("\n  Você tenta se misturar na multidão...", velocidade=0.04)
        if random.random() < 0.45:
            digitar("  O guardinha te viu. Ele já estava te esperando.", cor="vermelho")
            digitar("  'Ô estudante, para aí!'", cor="amarelo")
            vilao_g = criar_guarda_metro()
            pausa()
            batalha(heroi, vilao_g, modo_dificil=False)
        else:
            digitar("  Deu certo! O guardinha estava olhando pro celular.", cor="verde")
            pausa()
    else:
        digitar("\n  Você vai até o guardinha e fala que o cartão tá com problema.", velocidade=0.04)
        digitar("  Ele te olha por 5 segundos sem piscar.", velocidade=0.04)
        if random.random() < 0.4:
            digitar("  Ele não acreditou. 'Sistema puxa tudo, boyzinho(a).'", cor="vermelho")
            vilao_g = criar_guarda_metro()
            pausa()
            batalha(heroi, vilao_g, modo_dificil=False)
        else:
            digitar("  Ele acreditou. Seja lá por qual razão.", cor="verde")
            pausa()

    # --- CENA 2: Metrô até Tancredo Neves ---
    limpar_tela()
    secao("🚇 CENA 2: Metrô → Tancredo Neves")
    digitar("\n  Você chega à estação do metrô em Cajueiro Seco.", velocidade=0.04)

    if evento_aleatorio(0.20,
        "🔧 O metrô está quebrado. Todos os trens parados por tempo indeterminado. Fim da linha.",
        heroi, e_game_over=True):
        return

    digitar("  O metrô chega. Está lotado pra além do possível.", velocidade=0.04, cor="amarelo")
    digitar("  Parece que todo Recife decidiu andar de metrô hoje.", velocidade=0.04)

    if evento_aleatorio(0.25,
        "👣 Ao tentar subir no metrô, a multidão te pisoteou completamente. Você some entre as pernas.",
        heroi, e_game_over=True):
        return

    digitar("\n  Você conseguiu entrar! Sua caixa torácica discorda.", cor="verde", velocidade=0.04)

    evento_ocorreu = False
    if evento_aleatorio(0.15,
        "🌪️ Uma senhora com guarda-chuva aberto dentro do vagão te acertou no olho. Dano crítico.",
        heroi, dano=20):
        evento_ocorreu = True

    vilao2 = criar_guarda_metro()
    vilao2.nome = "Fiscal do Metrô"
    vilao2.descricao = "Diferente do guardinha do VLT, esse usa walkie-talkie e tem autoridade."
    if not evento_ocorreu:
        pausa()
    batalha(heroi, vilao2, modo_dificil=False)

    # --- CENA 3: Ônibus Tancredo – Macaxeira ---
    limpar_tela()
    secao("🚌 CENA 3: Ônibus Tancredo Neves → Macaxeira")
    digitar("\n  Você chegou em Tancredo Neves. Falta pouco.", velocidade=0.04)
    digitar("  O ônibus pra Macaxeira tem ar-condicionado!", velocidade=0.04, cor="verde")
    digitar("  PERIGOSAMENTE confortável para um estudante privado de sono.\n", velocidade=0.04, cor="amarelo")

    if evento_aleatorio(0.35,
        "😴 O ar-condicionado era bom demais. Você dormiu. E dormiu. E passou do ponto. E chegou em Nárnia.",
        heroi, e_game_over=True):
        return

    evento_ocorreu = False
    if evento_aleatorio(0.15,
        "📵 O motorista ligou o som no talo. Sertanejo universitário às 7h30. Dano psicológico severo.",
        heroi, dano=15):
        evento_ocorreu = True

    vilao3 = criar_motorista()
    vilao3.nome = "Cobrador Estressado"
    vilao3.descricao = "Um cobrador que acordou errado e quer que todo mundo pague por isso."
    if not evento_ocorreu:
        pausa()
    batalha(heroi, vilao3, modo_dificil=False)

    digitar("\n  🎉 Você chegou na Macaxeira! A UFRPE está à vista!", cor="verde")
    pausa()

# ================================================================
#  BATALHA FINAL — PROF. CLEYTON
# ================================================================

def batalha_final(heroi, modo_dificil):
    limpar_tela()
    titulo("⚡ BATALHA FINAL: PROF. CLEYTON ⚡", "★")

    digitar("\n  Você entra na sala de aula.", velocidade=0.04)
    digitar("  Silêncio. Todos olham pra você.", velocidade=0.04)
    digitar("  O professor Cleyton coloca os óculos devagar.", velocidade=0.04)
    time.sleep(0.5)
    digitar("\n  Prof. Cleyton:", cor="amarelo")
    digitar(f"  \"Interessante. {heroi.nome} decidiu aparecer.\"", cor="amarelo", velocidade=0.04)
    digitar("  \"Chegou atrasado. A prova já começou.\"", cor="amarelo", velocidade=0.04)
    digitar("  \"Mas tudo bem. ESSA prova é especial.\"", cor="amarelo", velocidade=0.04)
    time.sleep(0.5)

    digitar("\n  Música dramática começa a tocar... (na sua cabeça)", velocidade=0.04, cor="ciano")
    digitar("\n  ─────────────────────────────────────────────────────", cor="magenta")
    digitar("    BATALHA NO ESTILO POKÉMON!", cor="magenta")
    digitar("    Os ataques são: ERROS DE CÓDIGO!", cor="magenta")
    digitar("    Quanto mais grotesco o erro, mais dano no Prof. Cleyton!", cor="magenta")
    digitar("  ─────────────────────────────────────────────────────\n", cor="magenta")
    pausa()

    cleyton = criar_professor_cleyton()
    batalha(heroi, cleyton, modo_dificil=modo_dificil, modo_final=True)

    vitoria_final(heroi)

# ================================================================
#  MAIN
# ================================================================

def main():
    introducao()
    nome = pedir_nome()
    heroi = Heroi(nome)

    limpar_tela()
    titulo(f"🎮 BEM-VINDO(A), {nome.upper()}!")
    digitar(f"\n  Status inicial:", cor="ciano")
    print(f"  {heroi.status()}")
    digitar(f"  Escudo de BSI: {heroi.escudo_usos} usos", cor="azul")
    digitar(f"  Missão: Chegar à UFRPE sem ser preso, expulso ou pisoteado.\n")
    pausa()

    caminho, modo_dificil = escolher_caminho(heroi)

    if caminho == "barro":
        rota_barro(heroi)
    else:
        rota_tancredo(heroi)

    batalha_final(heroi, modo_dificil)

if __name__ == "__main__":
    main()
