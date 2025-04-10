# iOS-Logger2 – Infected iOS Application (Research Project)

This project is an **intentionally infected iOS application** created for research, reverse engineering, and threat analysis purposes. It is designed and developed by **Abdulrahman Al-Hakami** to simulate how a malicious iOS app might behave and how it can be analyzed both statically and dynamically.

---

##  Project Structure

- **iOS-Logger2.ipa**  
  Unsigned `.ipa` file containing the infected iOS app bundle, ready for analysis on jailbroken devices.

- **Payload/iOS-Logger2.app/**  
  The actual `.app` folder including a modified Mach-O binary with all malicious behavior integrated.

- **webapp.py**  
  Python Flask web server that listens on port `8080`, logs all incoming data (keystrokes, GPS coordinates, clipboard, etc.) and displays them in a web-based dashboard.

- **dashboard.html**  
  A live dashboard template for viewing incoming logs, including IP address, keystrokes, and geolocation data.

---

##  Infected Behavior Summary

The iOS app demonstrates the following malicious behaviors:

| Feature                    | Description |
|----------------------------|-------------|
|  Keystroke Logging       | Captures user input and sends it to a C2 server. |
|  Location Tracking       | Sends GPS coordinates of the device. |
|  IP-Based Geolocation    | Fetches and sends approximate location based on external IP. |
|  Clipboard Exfiltration | Reads and exfiltrates clipboard data. |
|  Malicious IP Checker   | Compares target IPs against a local list of known suspicious IPs. |

---



##  Dashboard Preview

- Run the Flask server:
    ```bash
    python3 webapp.py
    ```

- Visit:
    ```
    http://<your-local-ip>:8080/dashboard
    ```

---

## ⚠️ Legal Disclaimer

> This project is for **educational and authorized research purposes only**.  
> Do not deploy or distribute without full consent and legal justification.  
> The author is not responsible for any misuse.

---

##  Author

**Abdulrahman Al-Hakami**  
[GitHub](https://github.com/AbdulrahmanALHakami)  
[LinkedIn](https://www.linkedin.com/in/abdulrahmanalhakami/)
