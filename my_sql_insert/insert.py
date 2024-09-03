import sys
sys.path.append("./class")

import class_customer



c_1 = class_customer.Customer(1, 'CTCP A', '0987654321', 'Ha Noi', 'Thach That', 'Lien Quan', 'So nha 12')
c_2 = class_customer.Customer(2, 'CTCP B', '123456789', 'Quang Ninh', 'Ha Long', 'Bai Chay', 'So nha 12')
c_3 = class_customer.Customer(3, 'CTCP C', '0192837465', 'Nghe An', 'Quang Tri', 'Cai Rang', 'So nha 12')





print(c_1.Get_Customer())


