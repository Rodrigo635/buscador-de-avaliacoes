from datetime import datetime
from random import choice, randint
from django.db import IntegrityError
from .models import Avaliacoes
from django.contrib.auth.models import User

user_names = ["Cristiano Ronaldo", "Metallica", "Blind Guardian", "Black Sabbath", "Ana Maria Braga", "Billie Eilish", "Nirvana", "Eminem", "AC/DC", "Hatsune Miku", "Batman & Robin", "Juninho Portugal", "Lionel Messi", "Banda Dejavu", "Ozzy Osbourne", "Zeca Pagodinho", "Esqueleto (do He-Man)", "He-Man", "Bob Esponja", "Freddy Fazbear", "Ayel LOL", "MC Pipokinha", "Pato Donald", "Orfeu Somaceo", "Queen", "Milionário e José Rico", "Cillian Murphy", "Benedict Cumberbatch", "Donald Trump", "Barack Obama", "Pereira²", "Borin Produções", "Curry & Blankets", "Ronaldinho Gaúcho", "Gabriel Ribeiro Pereira", "Russell Crowe", "Black Jack", "The Rock", "Sonic", "Mario", "Amado Batista", "Luciano Cassol", "Jorge e Mateus", "Corpo e Alma", "Gusttavo Lima", "Luiz Gonzaga", "Ariana Grande", "Beyoncé", "Leonardo DiCaprio", "Taylor Swift", "Robert Downey Jr.", "Jennifer Lawrence", "Selena Gomez", "Tom Hanks", "Angelina Jolie", "Brad Pitt", "Johnny Depp", "Meryl Streep", "Katy Perry", "Junior Cocco","Marco Antonio da Luz Maciel da Costa", "Antonio Meneghetti", "Rhauani Weber" ,"Dwayne Johnson", "Emma Watson", "Chris Hemsworth", "Neymar", "Shakira", "Justin Bieber", "Kim Kardashian", "Kanye West", "Lady Gaga", "Mark Zuckerberg", "Oprah Winfrey"]
texto_choices = ["Bom demais!", "Ruim horrivel", "Excelente", "Hospedagem boa", "Acho que foi bom", "Acho que não foi bom", "Mediano"]
plataforma_choices = ["plataforma 1", "plataforma 2", "plataforma 3", "plataforma 4", "plataforma 5"]
classificacao_choices = [1, 2, 3, 4, 5]
idioma_choices = ["pt-br", "pt", "ing", "esp", "itn"]

def gerar_avaliacoes(num_games=1):
    avaliacoes_random = []

    for _ in range(num_games):
        nome = choice(user_names)
        texto = choice(texto_choices)
        plataforma = choice(plataforma_choices)
        data = datetime(randint(2000, 2023), randint(1, 12), randint(1, 28), randint(0, 23), randint(0, 59))
        classificacao = choice(classificacao_choices)
        idioma = choice(idioma_choices)
        encontrado_por = choice(User.objects.all())

        avaliacao = Avaliacoes(nome=nome, texto=texto, plataforma=plataforma, data=data, classificacao=classificacao, idioma=idioma, encontrado_por=encontrado_por)

        try:
            avaliacao.save()
            avaliacoes_random.append(avaliacao)
        except IntegrityError as e:
            print(f"Erro salvando a avaliação: {e}")

    return avaliacoes_random
