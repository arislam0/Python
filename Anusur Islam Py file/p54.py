class Phone:
    def call(self):
        print("You can call")
    def message(self):
        print("You can message")

class Samsung(Phone):
    def photo(self):
         print("You can take photo")

"""
p = Phone()
p.message()
p.call()
print()
"""

s = Samsung()
s.message()
s.call()
s.photo()

print(issubclass(Samsung,Phone))
print(issubclass(Phone,Samsung))