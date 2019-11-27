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
        self.value = weight / (height ** 2)
        if not (10 <= self.value <= 40):
            raise ValueError('BMIが正常値の範囲外です。')
    def __str__(self):
        return f'{self.value:.2f}'



hibiki_bmi = BMI(height=1.75, weight=58.2)
noriya_bmi = BMI(height=1.68, weight=67.3)
print('Hibiki')
print(hibiki_bmi)

