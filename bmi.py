"""
class (成人の)BMI:
    関連しそうな属性:
        - 身長
        - 体重
        - BMIという値そのもの
    ルール:
        - 10以上40以下
        - 表示するときは、少数第２位まで
            -ex: 23.678 -> 23.67
            -ex: 23.671 -> 23.67
    できること:
        - ???
"""
# クラス名はUpperCamelCaseが普通
class BMI():
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)



hibiki_bmi = BMI(height=1.75, weight=58.2)
noriya_bmi = BMI(height=1.68, weght=67.3)
print('Hibiki')
print(hibiki_bmi.height)
print(hibiki_bmi.calculate_bmi())

