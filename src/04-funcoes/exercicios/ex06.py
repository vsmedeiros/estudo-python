def calcular_volume(aquario):
    return (aquario["comprimento"] * aquario["altura"] * aquario["largura"]) / 1000


def calcular_potencia_termostato(volume, aquario):
    return volume * 0.05 * (aquario["temp_desejada"] - aquario["temp_ambiente"])


def calcular_filtragem(volume):
    return volume * 2, volume * 3


aquario = {
    "comprimento": float(input("Comprimento (cm): ")),
    "altura": float(input("Altura (cm): ")),
    "largura": float(input("Largura (cm): ")),
    "temp_desejada": float(input("Temperatura desejada (°C): ")),
    "temp_ambiente": float(input("Temperatura ambiente (°C): "))
}

volume = calcular_volume(aquario)
potencia = calcular_potencia_termostato(volume, aquario)
filtragem_min, filtragem_max = calcular_filtragem(volume)

print(f"\nVolume do aquário: {volume:.2f} L")
print(f"Potência do termostato: {potencia:.2f} W")
print(f"Filtragem recomendada: {filtragem_min:.2f} a {filtragem_max:.2f} L/h")
