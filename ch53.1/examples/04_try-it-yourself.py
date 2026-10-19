from flask import Flask

app = Flask(__name__)


# 3
@app.route("/price/<float:amount>")
def price(amount):
    return f"Price: {amount:.2f}"


client = app.test_client()
print(client.get("/price/4.5").get_data(as_text=True))
print(client.get("/price/abc").status_code)
