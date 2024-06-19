# # # # # # # name=input("emp1:")
# # # # # # # id=int(input("empid1:"))
# # # # # # # design=input("designation:")
# # # # # # # Sal=int(input("salary:"))
# # # # # # # if((Sal<45000) and (Sal>10000)):
# # # # # # #     print("hr")
# # # # # # # elif((Sal<55000) or (Sal>45000)):
# # # # # # #     print("Manager")
# # # # # # # else:
# # # # # # #     print("none")
# # # # # # #for loop
# # # # # # for x in range(0,10):
# # # # # #     print(x,end=",")
# # # # # car={"brand":"swift","year":2024,"total":94}
# # # # # for x in car:
# # # # #     print(x,car[x])
# # # # try:
# # # #  a=10/0
# # # #  print(a)
# # # #
# # # # except ArithmeticError:
# # # #     print("a")
# # # # else:
# # # #     print("success")
# # # try:
# # #     a=10/0;
# # #     print("Exception occurred")
# # # finally:
# # #     print("Code to be executed")
# # obj=open("abc.csv","w")
# # obj.write("1")
# # try:
# #  obj1=open("def.txt","r")
# #  s=obj1.read()
# #  print(s)
# # except EOFError:
# #     print("not defined")
# # else:
# #     print("success")
#
# try:
#     file=open('def.txt','w')
#     file.write("abcd")
#     file=open('def.txt','r')
#     while True:
#         line=file.readline()
#         if not line:
#          break
# except FileNotFoundError as file_error:
#     print("file not found error")
# except IOError as  io_error:
#     print("IO error occured")
# except EOFError:
#     print("End of file reached")
# except Exception as error:
#     print("Unexpected error")
# finally:
#     if 'file' in locals():
#         file.close()
#
#
#
