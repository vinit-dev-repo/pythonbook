class RouteBase:
    def ping(self):
        print("base ping")

class RouteFirst(RouteBase):
    def pong(self):
        print("first pong")

class RouteSecond(RouteBase):
    def pong(self):
        print("second pong")

class RouteCombined(RouteFirst, RouteSecond):
    def ping(self):
        print("combined ping")
        super().ping()

    def trace(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        RouteSecond.pong(self)

RouteCombined().trace()
