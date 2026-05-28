# 🚌 UFRPE ou Bust 🚌

> *"Sobreviver ao trajeto já é metade da nota."*

Um jogo de aventura textual cômico sobre a luta épica de um estudante de BSI para chegar à UFRPE no dia da prova de POO. Desenvolvido como extensão do projeto da disciplina **Princípios de Programação** — DEINFO/UFRPE.

---

## 📖 História

Era uma quinta-feira. O alarme tocou. Você ignorou três vezes.  
Na quarta, a memória brutal: **PROVA DE POO HOJE.**

Você mora em Marcos Freire. Seu destino é o Campus da UFRPE — Dois Irmãos.  
O problema: seus bolsos estão mais vazios que o SIGA às 23h59.

Dois caminhos, guardas no caminho, e o **Prof. Cleyton** esperando no final.  
Boa sorte.

---

## 🚀 Como Executar

**Pré-requisito:** Python 3.7 ou superior.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/ufrpe-ou-bust.git
cd ufrpe-ou-bust

# Execute o jogo
python main.py
```

Não é necessário instalar nenhuma biblioteca externa — o jogo usa apenas a biblioteca padrão do Python.

---

## 🗺️ Rotas Disponíveis

### 🚌 Terminal do Barro — SUPER DIFÍCIL 💀
> A rota raiz do sofrimento.

```
Ônibus Marcos Freire → Cajueiro Seco
        ↓
Ônibus Cajueiro Seco → Barro
        ↓
Ônibus Barro → Macaxeira (Várzea)
        ↓
    🎓 CEAGRI 2 / UFRPE
```

### 🚇 Terminal Tancredo Neves — DIFÍCIL 😰
> Ar-condicionado incluído. Riscos também.

```
VLT Marcos Freire → Cajueiro Seco
        ↓
Metrô → Tancredo Neves
        ↓
Ônibus Tancredo → Macaxeira
        ↓
    🎓 CEAGRI 2 / UFRPE
```

### 🛌 Não Ir — FÁCIL (Game Over imediato)
> Tecnicamente fácil. Academicamente fatal.

---

## ⚔️ Mecânicas de Combate

O sistema de batalha é por **turnos**, com máximo de **10 turnos** por luta. Sobreviver os 10 turnos equivale à vitória.

A cada turno, o adversário **anuncia seu próximo ataque** antes de você agir — planeje bem!

### Ataques do Herói

| Ataque | Dano | Descrição |
|--------|------|-----------|
| 🧻 Lançar VEM | 18–30 | Arremessa um rolo de VEM com força de estudante frustrado |
| 🛡️ Escudo de BSI | — | Usa o TCC como escudo. Aumenta defesa no turno. **3 usos por batalha** |
| 🤡 Mostrar Nota Vermelha | 10–40 | O adversário gargalha de vergonha alheia. Dano variável e imprevisível |

### Adversários

| Vilão | Vida | Dificuldade | Aparece em |
|-------|------|-------------|------------|
| Fiscal de Ônibus | 70 | Média | Rota do Barro |
| Motorista Raivoso | 75 | Alta | Ambas as rotas |
| Guardinha do VLT | 80 | Média | Rota de Tancredo |
| Fiscal do Metrô | 80 | Média | Rota de Tancredo |
| **Prof. Cleyton** 👨‍🏫 | **120** | **Suprema** | Batalha Final |

---

## 🎲 Eventos Aleatórios

O destino do Grande Recife é imprevisível. Em cada cena podem ocorrer eventos aleatórios — alguns apenas causam dano, outros encerram o jogo na hora.

| Evento | Chance | Consequência |
|--------|--------|--------------|
| BR-101 totalmente engarrafada | 25% | 💀 Game Over |
| Cachorro no terminal do Barro | 20% | 💀 Game Over |
| Fila quilométrica no Barro | 20% | 💀 Game Over |
| Sufocado no calor do ônibus Cajueiro-Barro | 30% | 💀 Game Over |
| Metrô quebrado em Cajueiro | 20% | 💀 Game Over |
| Pisoteado pela multidão no metrô | 25% | 💀 Game Over |
| Dormiu no ônibus com ar-condicionado | 35% | 💀 Game Over |
| Motorista errou o caminho (foi pra Caruaru) | 10% | 💀 Game Over |
| Lombada quase te mata | 20% | ⚠️ -25 de vida |
| Senhora com guarda-chuva aberto no vagão | 15% | ⚠️ -20 de vida |
| Motorista no talo do sertanejo universitário | 15% | ⚠️ -15 de vida |
| Guardinha viu você entrar sem pagar no VLT | 45% | ⚔️ Batalha surpresa |

---

## 👨‍🏫 Batalha Final — Prof. Cleyton

A batalha final é no **estilo Pokémon** — onde os "pokémons" são conceitos acadêmicos e os seus ataques são **erros de código**.

### Ataques do Prof. Cleyton

| Ataque | Dano | Descrição |
|--------|------|-----------|
| 📐 Conceitos de POO | 20–35 | Herança múltipla e polimorfismo ao mesmo tempo |
| 📊 Fluxograma na Lousa | 15–25 | Copie na prova. Agora. |
| 📄 Artigo Científico de 40 Páginas | 25–40 | Pra ler até amanhã |
| ❓ Qual é esse Pokémon? | 35–999 | **Hit-kill no modo Super Difícil.** Nenhuma resposta salva você |

### Seus Ataques na Batalha Final

Os ataques normais são substituídos por **erros de código**. Quanto mais grotesco o erro, maior o dano!

| Ataque | Dano | Nível de Grotesco |
|--------|------|-------------------|
| 💬 `print sem aspas` | 15–25 | ⭐ |
| 🐍 `função sem def` | 25–35 | ⭐⭐ |
| 💀 `classe sem __init__` | 35–50 | ⭐⭐⭐ |
| ☠️ Indentação com TAB e Espaço Misturados | 50–70 | ⭐⭐⭐⭐ |

---

## 🏆 Final

Ao derrotar o Prof. Cleyton, um diálogo épico se desenrola:

> *"Bom... isso foi... criativo."*  
> *"Tecnicamente errado em 11 lugares diferentes..."*  
> *"...mas a ideia estava lá. Acho."*

**✨ NOTA LANÇADA: 7.0** *(Mínimo pra passar. Mas você passou!)*

---

## 🗂️ Estrutura do Projeto

```
ufrpe-ou-bust/
│
├── main.py          # Arquivo principal — execute este
├── personagem.py    # Classe base com vida, dano e barra de HP
├── heroi.py         # Classe Herói com todos os ataques do player
├── vilao.py         # Classe Vilão + todos os inimigos do jogo
├── batalha.py       # Sistema de batalha por turnos
├── utils.py         # Utilitários: menus, efeitos, eventos aleatórios
└── README.md        # Este arquivo
```

---

## 🧩 Conceitos de POO Aplicados

Este projeto foi desenvolvido aplicando os conceitos da disciplina:

- **Herança** — `Heroi` e `Vilao` herdam de `Personagem`
- **Encapsulamento** — atributos e métodos organizados por responsabilidade
- **Polimorfismo** — `__str__` sobrescrito em cada classe; ataques com comportamentos distintos
- **Listas e Dicionários** — ataques, eventos e histórico de ações armazenados em estruturas de dados
- **Estruturas de repetição e decisão** — laço de batalha, menus interativos, eventos condicionais
- **Modularização** — código dividido em módulos com responsabilidades claras

---

## 👨‍💻 Créditos

Desenvolvido como atividade prática da disciplina **Princípios de Programação**  
**Universidade Federal Rural de Pernambuco — UFRPE**  
Departamento de Estatística e Informática — DEINFO  
Bacharelado em Sistemas de Informação

---

*Nenhum estudante foi reprovado na produção deste README. Provavelmente.*
