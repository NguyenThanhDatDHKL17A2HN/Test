import xml.etree.ElementTree as ET

class XmlReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def read_xml(self):
            tree = ET.parse(self.file_path)
            self.data = tree.getroot()
 
    def display_data(self):
        if self.data:
            print("Thông tin khách hàng:")
            for customer in self.data.findall('khach_hang'):
                name = customer.find('ten').text 
                address = customer.find('dia_chi').text 
                phone = customer.find('so_dien_thoai').text 
                print(f"Tên: {name}, Địa chỉ: {address}, Số điện thoại: {phone}")
        else:
            print("Không có dữ liệu để hiển thị.")

file_path = 'D:\\09_Dat_0096\\Data\\khach_hang.xml'
reader = XmlReader(file_path)
reader.read_xml()
reader.display_data()
