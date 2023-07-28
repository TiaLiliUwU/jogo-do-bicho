# Código para armazenar os dados dos bichos
class Animais:

    def __init__(self):
        self.animais = {
            "Avestruz": [1, 2, 3, 4],
            "Águia": [5, 6, 7, 8],
            "Burro": [9, 10, 11, 12],
            "Borboleta": [13, 14, 15, 16],
            "Cachorro": [17, 18, 19, 20],
            "Cabra": [21, 22, 23, 24],
            "Carneiro": [25, 26, 27, 28],
            "Camelo": [29, 30, 31, 32],
            "Cobra": [33, 34, 35, 36],
            "Coelho": [37, 38, 39, 40],
            "Cavalo": [41, 42, 43, 44],
            "Elefante": [45, 46, 47, 48],
            "Galo": [49, 50],
            "Gato": [53, 54, 55, 56],
            "Jacaré": [57, 58, 59, 60],
            "Leão": [61, 62, 63, 64],
            "Macaco": [65, 66, 67, 68],
            "Porco": [69, 70, 71, 72],
            "Pavão": [73, 74, 75, 76],
            "Peru": [77, 78, 79, 80],
            "Touro": [81, 82, 83, 84],
            "Tigre": [85, 86, 87, 88],
            "Urso": [89, 90, 91, 92],
            "Veado": [93, 94, 95, 96],
            "Vaca": [97, 98, 99, 100],
        }

    def formatar_numeros(self, numeros):
        return ', '.join(f'{numero % 100:02}' for numero in numeros)

    def mostrar_animais(self):
        for i, (animal, numeros) in enumerate(self.animais.items(), 1):
            numeros_formatados = self.formatar_numeros(numeros)
            print(f'{i:02}) {animal} - {numeros_formatados}')