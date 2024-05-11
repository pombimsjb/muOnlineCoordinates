from flask import Flask, render_template

app = Flask(__name__)

# Lista de nomes de arquivos de imagem
image_files = [
    "Devias.png", "Lorencia.png", "LostTower1.png", "Noria.png", "Lost tower 3.png", "Aida.png",
    "DeepDungeon1.png", "DeepDungeon2.png", "DeepDungeon3.png", "DeepDungeon4.png", "DeepDungeon5.png",
    "Ferea.png", "TormentaIsland.png", "SwampOfCalmness.png", "UrukMontain.png", "Acheron.png", "Nars.png"
]

# Dicionário de coordenadas para cada imagem
image_coordinates = {
    "Devias.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Lorencia.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "LostTower1.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Noria.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Lost tower 3.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon1.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon2.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon3.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon4.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "DeepDungeon5.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Ferea.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "TormentaIsland.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "SwampOfCalmness.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "UrukMontain.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Acheron.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250},
    "Nars.png": {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250}
}


@app.route("/")
def index():
    return render_template("index.html", image_files=image_files)


@app.route("/view_image/<image>", methods=["GET"])
def view_image(image):
    coordinates = image_coordinates.get(image, {"x_min": 0, "x_max": 250, "y_min": 0, "y_max": 250})
    if image not in image_files:
        return "Image not found", 404
    return render_template("view_image.html", image=image, coordinates=coordinates)


# Remova a condição if __name__ == "__main__" para permitir o deploy no Vercel
# if __name__ == "__main__":
#     app.run(debug=True)
