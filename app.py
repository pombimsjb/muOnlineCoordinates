from flask import Flask, render_template

app = Flask(__name__)

# Lista de nomes de arquivos de imagem
image_files = ["AbyssAtlans1.png","AbyssAtlans2.png","AbyssAtlans3.png", "Acheron.png","Aida.png",
               "ArenilTemple.png","AshenAida.png","Atlans.png","BlazeKethotum.png","BloodyTarkan.png",
               "CuberaMine.png","Darkness.png","Debenter.png","DeepDungeon1.png", "DeepDungeon2.png",
               "DeepDungeon3.png", "DeepDungeon4.png", "DeepDungeon5.png","Devias.png","Dungeon.png",
               "Elbeland.png","Ferea.png","Icarus.png","IgnisVulcano.png","Kalima.png","Kanturu.png",
               "KanturuRelics.png","KanturuRuins.png","KanturuUnderground.png", "Karutan1.png","Karutan2.png",
               "Lorencia.png","LostTower.png","Nars.png","NixiesLake.png","Noria.png","OldKethotum.png",
               "Raklion.png","RedSmokeIcarus.png","ScorchedCanyon.png","SwampOfCalmness.png","Tarkan.png",
               "TormentaIsland.png","UrukMontain.png","Vulcanus.png"]

# Dicionário de coordenadas para cada imagem
image_coordinates = {
    "AbyssAtlans1.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "AbyssAtlans2.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "AbyssAtlans3.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Acheron.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Aida.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "ArenilTemple.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Atlans.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "BlazeKethotum.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "BloodyTarkan.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "CuberaMine.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Darkness.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Debenter.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon1.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon2.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon3.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon4.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon5.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Devias.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Dungeon.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Elbeland.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Ferea.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Icarus.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "IgnisVulcano.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Kalima.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Kanturu.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "KanturuRelics.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "KanturuRuins.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "KanturuUnderground.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Karutan1.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Karutan2.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Lorencia.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "LostTower.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Nars.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "NixiesLake.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Noria.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "OldKethotum.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Raklion.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "RedSmokeIcarus.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "ScorchedCanyon.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "SwampOfCalmness.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Tarkan.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "TormentaIsland.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "UrukMontain.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Vulcanus.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250}
}


@app.route("/")
def index():
    return render_template("index.html", image_files=image_files)


@app.route("/view_image/<image>", methods=["GET"])
def view_image(image):
    coordinates = image_coordinates.get(image, {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250})
    return render_template("view_image.html", image=image, coordinates=coordinates)


if __name__ == "__main__":
    app.run(debug=True)
