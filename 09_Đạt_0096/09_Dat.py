import json
#a
class CustomerReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_json(self):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
       
    def display_data(self):
        if self.data:
            print("Thông tin khách hàng:")
            for customer in self.data:
                print(f"Name: {customer['name']}, Phone: {customer['phone']}, Address:{customer['address']}")
#b
file_path = 'D:\\09_Đạt_0096\\Data\\khach_hang.json'
reader = CustomerReader(file_path)
reader.read_json()
reader.display_data()
