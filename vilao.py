from personagem import Personagem
import random

class Vilao(Personagem):
    """Classe que representa os vilões do jogo."""

    NIVEIS_VALIDOS = ['Baixa', 'Média', 'Alta', 'Suprema']

    def __init__(self, nome, vida, maldade, descricao="", ataques_custom=None):
        super().__init__(nome, vida=vida, ataque_base=20, defesa_base=8)
        if maldade not in self.NIVEIS_VALIDOS:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {self.NIVEIS_VALIDOS}")
        self.maldade = maldade
        self.descricao = descricao

        self.ataques = ataques_custom or [
            {
                "nome": "👊 Empurrão",
                "descricao": "O adversário te empurra na multidão!",
                "dano_min": 10,
                "dano_max": 20
            },
            {
                "nome": "📢 Gritar",
                "descricao": "O adversário grita tão alto que você fica tonto!",
                "dano_min": 8,
                "dano_max": 15
            },
            {
                "nome": "🦶 Pisar no Pé",
                "descricao": "O adversário pisa no seu pé com sandália de borracha!",
                "dano_min": 5,
                "dano_max": 25
            }
        ]

    def escolher_ataque(self):
        return random.choice(self.ataques)

    def atacar(self, heroi):
        ataque = self.escolher_ataque()
        dano = random.randint(ataque["dano_min"], ataque["dano_max"])
        dano_real = heroi.receber_dano(dano)
        return ataque, dano_real

    def __str__(self):
        return f"Vilão: {self.nome} | Vida: {self.vida}/{self.vida_maxima} | Maldade: {self.maldade}"


# --- Vilões do jogo ---

def criar_guarda_metro():
    return Vilao(
        nome="Guardinha do VLT",
        vida=50,
        maldade='Média',
        descricao="Um guarda de segurança cansado que não aguenta mais acordar tão cedo.",
        ataques_custom=[
            {"nome": "📣 Apito Ensurdecedor", "descricao": "O guarda apita no seu ouvido!", "dano_min": 10, "dano_max": 20},
            {"nome": "📋 Burocracia", "descricao": "O guarda pede 3 documentos que você não tem!", "dano_min": 8, "dano_max": 18},
            {"nome": "🔦 Lanterna no Olho", "descricao": "O guarda joga a lanterna no seu rosto. Você fica cego por um momento!", "dano_min": 12, "dano_max": 25}
        ]
    )

def criar_motorista():
    return Vilao(
        nome="Motorista Raivoso",
        vida=75,
        maldade='Alta',
        descricao="Um motorista que nunca sorriu na vida e odeia catraca pulada.",
        ataques_custom=[
            {"nome": "🚗 Freada Brusca", "descricao": "O motorista freia do nada! Você vai de encontro à barra!", "dano_min": 18, "dano_max": 30},
            {"nome": "😤 Olhar Raivoso", "descricao": "O motorista olha pelo espelho retrovisor com ódio. Você perde a vontade de viver.", "dano_min": 5, "dano_max": 10},
            {"nome": "🎵 Volume Máximo no Rádio", "descricao": "Banda Calcinha Preta no talo às 5 da manhã. Dano psicológico.", "dano_min": 10, "dano_max": 20}
        ]
    )

def criar_guarda_onibus():
    return Vilao(
        nome="Fiscal de Ônibus",
        vida=70,
        maldade='Média',
        descricao="Um fiscal que só aparece quando você mais não quer.",
        ataques_custom=[
            {"nome": "🎫 Pedir Passagem", "descricao": "O fiscal pede seu bilhete. Você não tem. Dano à alma.", "dano_min": 20, "dano_max": 35},
            {"nome": "📱 Ligar pra Polícia", "descricao": "O fiscal ameaça chamar a polícia! Você entra em pânico!", "dano_min": 10, "dano_max": 22},
            {"nome": "🗣️ Humilhar na Frente de Todos", "descricao": "O fiscal grita sua situação pro ônibus inteiro. Dano social extremo.", "dano_min": 15, "dano_max": 28}
        ]
    )

def criar_professor_cleyton():
    return Vilao(
        nome="Prof. Cleyton",
        vida=120,
        maldade='Suprema',
        descricao="O Boss Final. Mestre do código limpo e inimigo da indentação errada.",
        ataques_custom=[
            {
                "nome": "📐 Conceitos de POO",
                "descricao": "Cleyton pergunta sobre herança múltipla e polimorfismo ao mesmo tempo!",
                "dano_min": 20,
                "dano_max": 35
            },
            {
                "nome": "📊 Fluxograma na Lousa",
                "descricao": "Cleyton pede para você desenhar o fluxograma do App RiBank na Lousa!",
                "dano_min": 15,
                "dano_max": 25
            },
            {
                "nome": "📄 Artigo Científico de 40 Páginas",
                "descricao": "Cleyton manda um artigo pra ler até a próxima aula. Você desespera.",
                "dano_min": 25,
                "dano_max": 40
            },
            {
                "nome": "❓ Qual é esse Pokémon?",
                "descricao": "Cleyton mostra uma silhueta e pergunta: Pikachu? Bulbasaur? Snorlax? ERRADO — você é o reprovado!",
                "dano_min": 35,
                "dano_max": 999,  # hit kill no modo difícil
                "especial": "pokemon"
            }
        ]
    )