# Jogo


## Índice
1. [Descrição](#1-descrição)
2. [Tecnologias utilizadas](#2-tecnologias-utilizadas)
3. [Requisitos](#3-requisitos)
4. [Como jogar](#4-como-jogar)
5. [Controles](#5-controles)
6. [Autores](#6-autores)
7. [Reprodução](#7-reprodução)

---
## 1. Descrição
    Projeto desenvolvido para a disciplina de Estruturas de Linguagens. O objetivo era desenvolver alguma aplicação
    utilizando funcionalidades da linguagem Python e apresenta-las de forma didática em aula.

    Se trata de um duelo onde os jogadores têm 100 pontos de vida, 10 munições, e cada projétil causa 10 de dano.
    Ao eliminar um adversário, o nome do jogador que vencer tem 1 ponto registrado na tabela de pontuação (Score).
    Ao ficar sem munição, é possível remuniciar ao coletar uma das caixas de munição que caem do avião.
---
## 2. Tecnologias utilizadas
    Python 3.12
    Pygames 2.6.0
    Pycharm
    Git
---
## 3. Requisitos
    Dois jogadores
    Python 3.12 instalado
    Pygames 2.6.0 instalado
    50MB de espaço em disco
---
## 4. Como jogar
    1 - Abra o terminal
    2 - Clone o repositório utilizando o comando:
~~~bash
  git clone https://github.com/GabryelJ/Jogo.git
~~~  
    3 - Execução:
        Observações: Será necessário instalar a biblioteca Pygames para executar o jogo.
            Caso contrário, será apresentado um erro solicitando este módulo.
            Você pode optar por instalar o módulo diretamente no ambiente global do Python
            ou instalá-lo em um ambiente virtual. Pode utilizar o Venv ou o Conda, o que preferir. 
            Ao fazer isto você garante que os módulos instalados não causem conflitos em seus outros projetos.
        3.1 - Navegue até o diretório que o repositório se encontra.
        3.2 - execute o programa principal utilizando:
~~~bash 
  py main.py
~~~
---
## 5. Controles

    Menu:
        1. Seleciona a opção Play, que inicia o jogo.
        2. Seleciona a opção Quit, que encerra a aplicação.
        3. Seleciona a opção Score, que exibe as pontuações da sessão de jogo.

    Jogo: 
        Jogador 1 : 
            W. Faz o personagem pular.
            A. Faz o personagem andar para a esquerda.
            S. Faz o personagem atirar.
            D. Faz o personagem andar para a direita.
        Jogador 2 :
            ↑(seta para cima). Faz o personagem pular. 
            ←(seta para esquerda). Faz o personagem andar para a esquerda.
            ↓(seta para baixo). Faz o personagem atirar.
            →(seta para direita). Faz o personagem andar para a direita.
    
    Tabela de pontuações (Score):
        1. Voltar ao menu.

---
## 6. Autores
https://github.com/GabryelJ

https://github.com/lucasferreiralima

https://github.com/sergiolencioni10

---

## 7. Reprodução
[![Demo do Jogo](https://img.youtube.com/vi/Ownh_UOwzsI/maxresdefault.jpg)](https://youtu.be/Ownh_UOwzsI)
