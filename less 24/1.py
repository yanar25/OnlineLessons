# class Something:
#     def __new__(cls, *args, **kwargs):
#         print(f'сработал __new__ для класса srabotali argumenti: {args, kwargs}')
#         instance = super().__new__(cls)
#         instance.new_attribute = 'добавлено'
#         return instance
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# ex = Something('igor', 24)
# print(ex)


class FileObject:
    def __init__(self, filename):
        self.filename = filename
    def read_file(self):