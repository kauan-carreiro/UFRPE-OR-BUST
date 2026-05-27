import random

class Personagem:
    """Classe base para todos os personagens do jogo."""

    def __init__(self, nome, vida=100, ataque_base=20, defesa_base=10):
        self.nome = nome
        self.vida_maxima = vida
        self.vida = vida
        self.ataque_base = ataque_base
        self.defesa_base = defesa_base
        self.historico = []

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        dano_real = max(1, dano - self.defesa_base // 2)
        self.vida = max(0, self.vida - dano_real)
        return dano_real

    def registrar(self, evento):
        self.historico.append(evento)

    def status(self):
        barra = self._barra_vida()
        return f"{self.nome} | Vida: {self.vida}/{self.vida_maxima} {barra}"

    def _barra_vida(self):
        tamanho = 20
        preenchimento = int((self.vida / self.vida_maxima) * tamanho)
        barra = "█" * preenchimento + "░" * (tamanho - preenchimento)
        if self.vida > 60:
            cor = "verde"
        elif self.vida > 30:
            cor = "amarelo"
        else:
            cor = "vermelho"
        return f"[{barra}]"

    def __str__(self):
        return f"Personagem: {self.nome}, Vida: {self.vida}/{self.vida_maxima}"