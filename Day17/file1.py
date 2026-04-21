# class User:
#     pass


# user_1 = User()

# user_1.id = "001"

# user_1.username = "Prashant"

# print(user_1.id)




# user_2 = User()

# user_2.id = "001"

# user_2.username = "Prashant"



#__init__ is the constructor of this its a special method def likhna padta hai 
# here self is this 


#####################################################


class User:
    def __init__(self,username,id,country):
        self.username = username
        self.id = id
        self.country= country


myuser_1 = User("khilendra","001","India")


myuser_1.id = "002"

print(myuser_1.username,myuser_1.id,myuser_1.country)
        
            