
## 🚀 How to Run

1. **Download the required IP2Location `.BIN` files** and place them in the `db/` folder:
   - [IP2LOCATION-LITE-DB1.BIN](https://lite.ip2location.com/download?id=2)
   - [IP2LOCATION-LITE-ASN.BIN](https://lite.ip2location.com/download?id=57)

2. **Double-click `run.bat`** to:
   - Create virtual environment (if not exists)
   - Install dependencies
   - Launch the Flask web app


    ```
   ⚠️ Warning:
    When you double-click `run.bat`, it will set up the environment and install dependencies on your local machine. Please ensure that you trust the code before running it, as it involves installing packages and running the application. Running untrusted code can pose security risks.
    ```

### 3. **Access the Application**

3. **Open your browser** and go to: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)


4. **Upload a CSV file** containing a list of IP addresses.
    - The file must contain a column header with the name `ip`.


    Example CSV format:
    ```csv
    ip
    8.8.8.8
    1.1.1.1
    192.168.1.1
    ```

5. **Download the result** CSV file with country and ISP info.

## 🧾 Requirements

All dependencies will be installed automatically, but here’s what’s included in `requirements.txt`:

```txt
Flask
IP2Location
