import requests

class MyClass:
    def __init__(self):
        self.response = requests.get('https://catfact.ninja/breeds')
        self.data = self.response.json()
    
    def get_breed(self,value1):
        self.set = self.data['data']
        value = self.set[value1]
        return value['breed']



obj = MyClass()
for i in range(0, 11):
    print("Breed for "+ str(i) +": "+obj.get_breed(i))