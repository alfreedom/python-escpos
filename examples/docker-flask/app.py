from escpos.printer import CupsPrinter
from flask import Flask

# Initialize Flask app
app = Flask(__name__)


@app.route("/", methods=["GET"])
def do_print():
    # p = Usb(0x04b8, 0x0e28, 0)
    p = CupsPrinter(host="localhost", port=631, printer_name="TM-T20III")
    p.text("Hello World\n")
    p.cut()
    p.close()
    return "OK"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=9999)
