class ReprFailure(Exception):
    def __repr__(self):
        return "debug view"

class DisplayFailure(Exception):
    def __str__(self):
        return "Please check the record"

first = ReprFailure("original message")
second = DisplayFailure("original message")
