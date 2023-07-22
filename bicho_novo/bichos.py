# Código para armazenar os dados dos bichos
class Animais:

    def __init__(self):
        self.animais = {
            "Avestruz": range(1, 5),
            "Águia": range(5, 9),
            "Burro": range(9, 13),
            "Borboleta": range(13, 17),
            "Cachorro": range(17, 21),
            "Cabra": range(21, 25),
            "Carneiro": range(25, 29),
            "Camelo": range(29, 33),
            "Cobra": range(33, 37),
            "Coelho": range(37, 41),
            "Cavalo": range(41, 45),
            "Elefante": range(45, 49),
            "Galo": range(49, 51),
            "Gato": range(53, 57),
            "Jacaré": range(57, 61),
            "Leão": range(61, 65),
            "Macaco": range(65, 69),
            "Porco": range(69, 73),
            "Pavão": range(73, 77),
            "Peru": range(77, 81),
            "Touro": range(81, 85),
            "Tigre": range(85, 89),
            "Urso": range(89, 93),
            "Veado": range(93, 97),
            "Vaca": range(97, 101),
        }

    def formatar_numeros(self, numeros):
        return ', '.join(f'{numero % 100:02}' for numero in numeros)

    def mostrar_animais(self):
        for i, (animal, numeros) in enumerate(self.animais.items(), 1):
            numeros_formatados = self.formatar_numeros(numeros)
            print(f'{i:02}) {animal} - {numeros_formatados}')