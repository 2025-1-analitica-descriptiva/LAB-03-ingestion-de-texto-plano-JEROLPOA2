import pandas as pd
import re

def pregunta_01():
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    data_lines = lines[4:]  # Saltamos encabezados y separadores
    clusters = []

    current = []
    for line in data_lines:
        if re.match(r"\s+\d+\s+\d+\s+\d+,\d+\s+", line):
            if current:
                clusters.append(" ".join(current))
            current = [line.strip()]
        else:
            current.append(line.strip())
    if current:
        clusters.append(" ".join(current))

    registros = []
    for cluster in clusters:
        parts = re.split(r"\s{2,}", cluster)
        cluster_id = int(parts[0])
        cantidad = int(parts[1])
        porcentaje = float(parts[2].replace(",", ".").replace("%", "").strip())
        palabras_clave = " ".join(parts[3:]).strip()

        # Limpieza adicional
        palabras_clave = re.sub(r"\s+", " ", palabras_clave)             # Espacios múltiples
        palabras_clave = palabras_clave.replace(", ", ",").replace(",", ", ")  # Comas sin dobles espacios
        if palabras_clave.endswith("."):
            palabras_clave = palabras_clave[:-1]  # Eliminar punto final

        registros.append((cluster_id, cantidad, porcentaje, palabras_clave))

    df = pd.DataFrame(
        registros,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )

    return df
