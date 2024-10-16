def gerar(nome: str):
    template = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="estilo1.css" />
    <title>{nome}</title>
  </head>
  <body>
    <div class="barrasuperior">
      <p class="textodireito"><a href="index.html">Home</a></p>
      <img src="imagens/blockchain.png" class="iconeprincipal" />
    </div>
    <div class="conteudocentral"></div>
  </body>
</html>"""
    with open(f"{nome}.html", "w") as arquivo:
        arquivo.write(template)
    arquivo.close

nome = gerar(input("Insira o nome do arquivo: "))
