from personagem import Personagem
import random

class Heroi(Personagem):
    """Classe que representa o herói (o player) do jogo."""

    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque_base=25, defesa_base=10)
        self.escudo_usos = 3
        self.pocao_usos = 2

        # Ataques do herói
        self.ataques = [
            {
                "nome": "💳 Lançar VEM",
                "descricao": "Você arremessa o seu VEM no adversário com força de estudante frustrado!",
                "dano_min": 18,
                "dano_max": 30,
                "tipo": "ataque"
            },
            {
                "nome": "🛡️ Escudo de BSI",
                "descricao": "Você ergue o TCC como escudo e absorve o dano!",
                "dano_min": 0,
                "dano_max": 0,
                "tipo": "defesa",
                "usos": lambda: self.escudo_usos > 0
            },
            {
                "nome": "🤡 Mostrar Nota Vermelha",
                "descricao": "Você mostra sua nota 4 no celular... o adversário gargalha tanto que perde 3 turnos por vergonha alheia!",
                "dano_min": 20,
                "dano_max": 50,
                "tipo": "ataque_especial"
            }
        ]

        # Ataques da batalha final (códigos errados)
        self.ataques_finais = [
            {
                "nome": '💬 print sem aspas',
                "descricao": "print(Hello World) — erro clássico do calouro!",
                "dano_min": 15,
                "dano_max": 25,
                "nivel_grotesco": 1
            },
            {
                "nome": "🐍 função sem def",
                "descricao": "minhaFuncao(): — Professor Cleyton estressa!",
                "dano_min": 25,
                "dano_max": 35,
                "nivel_grotesco": 2
            },
            {
                "nome": "💀 classe sem __init__",
                "descricao": "class Aluno: pass — O professor chora por dentro.",
                "dano_min": 35,
                "dano_max": 50,
                "nivel_grotesco": 3
            },
            {
                "nome": "☠️ Indentação com TAB e Espaço Misturados",
                "descricao": "O arquivo parece um picasso. Cleyton tem um ataque cardíaco de raiva!",
                "dano_min": 50,
                "dano_max": 70,
                "nivel_grotesco": 4
            }
        ]

    def usar_ataque(self, indice, adversario, modo_final=False):
        if modo_final:
            ataques = self.ataques_finais
        else:
            ataques = self.ataques

        ataque = ataques[indice]

        if ataque.get("tipo") == "defesa":
            if self.escudo_usos <= 0:
                return None, "❌ Sem usos de Escudo de BSI restantes!"
            self.escudo_usos -= 1
            self.defesa_base += 15
            msg = f"🛡️ {self.nome} usa o Escudo de BSI! Defesa aumentada por este turno! (Usos restantes: {self.escudo_usos})"
            self.registrar(msg)
            return 0, msg

        dano = random.randint(ataque["dano_min"], ataque["dano_max"])
        dano_real = adversario.receber_dano(dano)
        msg = f"{ataque['descricao']} Causou {dano_real} de dano!"
        self.registrar(f"Atacou com {ataque['nome']}: {dano_real} dano")
        return dano_real, msg

    def resetar_defesa(self):
        self.defesa_base = 10