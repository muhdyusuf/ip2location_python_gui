from flask import Flask, request, render_template, send_file
import csv, io
import os
import IP2Location

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "db", "IP2LOCATION-LITE-DB1.BIN")
asn_path = os.path.join(basedir, "db", "IP2LOCATION-LITE-ASN.BIN")

db_location = IP2Location.IP2Location(db_path)
db_asn = IP2Location.IP2Location(asn_path)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["csvfile"]
    if not file:
        return "No file uploaded", 400

    # Read IPs from uploaded CSV
    content = file.read().decode("utf-8")
    ip_list = [row.strip() for index, row in enumerate(content.splitlines()) if row.strip() and index > 0]

    # Prepare CSV output
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["IP", "Country", "ISP"])

    for ip in ip_list:
        try:
            country = db_location.get_all(ip).country_long
            isp = db_asn.get_all(ip).as_name
            writer.writerow([ip, country or "N/A", isp or "N/A"])
        except:
            writer.writerow([ip, "Error", "Error"])

    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype="text/csv",
        as_attachment=True,
        download_name="ip_results.csv"
    )

if __name__ == "__main__":
    app.run(debug=True)
