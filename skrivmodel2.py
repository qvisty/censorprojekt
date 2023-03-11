from django.apps import apps
from django.db import models
import matplotlib.pyplot as plt


def print_models():
    # Opret en tabel med modellernes navne som kolonnehoveder
    header = ["Model"] + [model.__name__ for model in apps.get_models()]
    data = [header]

    # Tilføj rækker med felter for hver model til tabellen
    for field in apps.get_models():
        row = [field.__name__]
        for other_field in apps.get_models():
            fields = [f.name for f in other_field._meta.fields]
            if field in [type(f) for f in other_field._meta.fields]:
                row.append("* " + ", ".join(fields))
            else:
                row.append(", ".join(fields))
        data.append(row)

    # Opret en figur og en akse til tabellen
    fig, ax = plt.subplots(1, 1)
    ax.axis("off")

    # Opret tabellen som et billede og tilføj den til akset
    table = ax.table(cellText=data, colLabels=None, cellLoc="left", loc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 1.5)
    plt.savefig("models.png", bbox_inches="tight", pad_inches=0)

    # Udskriv filnavnet på det gemte billede
    print("Table saved as models.png")

print_models()