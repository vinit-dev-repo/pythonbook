class ParentToken:
    def __init__(self):
        self.__token = "parent"

    def parent_token(self):
        return self.__token

class ChildToken(ParentToken):
    def __init__(self):
        super().__init__()
        self.__token = "child"

    def child_token(self):
        return self.__token

token = ChildToken()
print(token.parent_token(), token.child_token())
print(token._ParentToken__token, token._ChildToken__token)
