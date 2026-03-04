import urllib.request
import json

def inicial_filmes():
    url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=a5b52866db3a4cde65767462549350c8"
    resposta = urllib.request.urlopen(url)
    dados = resposta.read()
    dados_json = json.loads(dados)
    return dados_json["results"]


def resultado_filmes(tipo):
    if tipo == "Animações":
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=a5b52866db3a4cde65767462549350c8"
    elif tipo == "2023":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2023&sort_by=vote_average.desc&api_key=a5b52866db3a4cde65767462549350c8"
    elif tipo == "2024":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2024&sort_by=vote_average.desc&api_key=a5b52866db3a4cde65767462549350c8"
    elif tipo == "2025":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2025&sort_by=vote_average.desc&api_key=a5b52866db3a4cde65767462549350c8"
    
    resposta = urllib.request.urlopen(url)

    dados = resposta.read()

    dados_json = json.loads(dados)

    return dados_json["results"]

#print(dados_json["results"])