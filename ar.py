# # # # import datetime
# # # # class reliance:
# # # #
# # # #      def __init__(self):
# # # #          num_person = int(input("ENTER the number of person:"))
# # # #          for x in range(1, num_person + 1):
# # # #           self.product=int(input("Enter the product:"))
# # # #           self.date=datetime.datetime.now()
# # # #           self.price=int(input("Enter the price:"))
# # # #           print("product:", self.product, "date", self.date, "price", self.price)
# # # #      def view(self):
# # # #           print("product:",self.product,"date",self.date,"price",self.price)
# # # # obj1=reliance()
# # # # obj1.view()
# # # class person:
# # #     def __init__(self,name,age=50):
# # #         self.name=name
# # #         self.age=age
# # #     def display(self):
# # #         print("name",self.name,"age",self.age)
# # # obj=person("abc",56)
# # # obj.display()
# # # obj1=person("def")
# # # obj1.display()
# #
# # class medical:
# #     def database1(self):
# #         self.ID=int(input("ID:"))
# #         self.Name=input("Name:")
# #         self.Number=int(input("NUMBER:"))
# # class trans(medical):
# #     def database2(self):
# #         self.address=input("Address:")
# #         self.pincode=int(input("PINCODE:"))
# #
# # obj=trans()
# # obj.database1()
# # obj.database2()
# import email,datetime
# class bank:
#     def personaldetail(self):
#         self.id=int(input("ID:"))
#         self.Name=input("Name:")
#         self.age=int(input("age:"))
# class data(bank):
#     def transcation(self):
#         self.email=input("email")
#         self.phone=int(input("phone:"))
#         self.date=datetime.datetime.now()
# class data1(data):
#     def billing(self):
#         print("Name",self.Name,"age",self.age,"EMAIL",self.email,"phone",self.phone,"date",self.date)
# obj=data1()
# obj.personaldetail()
# obj.transcation()
# obj.billing()
