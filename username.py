# データ型宣言: UserName
#     属性:
#         実際のユーザー名
#     ルール:
#         ・４文字以上２０文字以下である
#     できること:
#         ・ユーザー名を大文字に変換する

class UserName:
    def __init__(self, name):
        if not(4 <= len(name) <= 20):
            raise ValueError(f'{name}は文字数のルール違反です。')

        self.namae = name

    def screen_name(self):
        return self.name.upper()


# UserNameクラスのインスタンス化をしている。
hibiki = UserName(name='hibiki')
# print(hibiki)
# print(type(hibiki))

print(hibiki.namae)
print(hibiki.screen_name)

# class DisneyName:
#     def __init__(self, name):
#         self.namae = name
#         self.hello = name + "さんこんにちは"
#
# mickey = DisneyName(name = 'mickey')
# print(mickey.hello)