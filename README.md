# 🛡️ Basic Network Sniffer

## 📌 Overview

The **Basic Network Sniffer** is a Python-based cybersecurity project developed as part of the **CodeAlpha Cyber Security Internship**. The application captures network packets in real time, extracts useful information, and displays details such as the source IP address, destination IP address, protocol, and packet payload.

This project demonstrates the fundamentals of network packet analysis and helps understand how data travels across a network using common protocols.

---

## 🎯 Objectives

* Capture live network packets.
* Analyze packet structure.
* Display packet information.
* Understand common network protocols.
* Learn the basics of packet sniffing using Python.

---

## 🚀 Features

* Real-time packet capturing.
* Displays Source IP Address.
* Displays Destination IP Address.
* Detects Network Protocol.
* Displays Packet Payload.
* Supports continuous packet monitoring.
* Simple and easy-to-understand Python implementation.

---

## 🛠 Technologies Used

* Python 3
* Scapy
* Socket (if applicable)

---

## 📂 Project Structure

```
Basic-Network-Sniffer/
│
├── network_sniffer.py
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Sreeram2611/Basic-Network-Sniffer.git
```

Navigate into the project folder:

```bash
cd Basic-Network-Sniffer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the application:

```bash
python network_sniffer.py
```

> **Note:** Administrator/root privileges may be required for packet capturing.

---

## 📊 Sample Output

```
=========================================
Packet Captured
=========================================
Source IP      : 192.168.1.10
Destination IP : 142.250.183.14
Protocol       : TCP

Payload:
GET / HTTP/1.1
Host: example.com
=========================================
```
---

## 📚 Concepts Covered

* Packet Sniffing
* IP Protocol
* TCP
* UDP
* ICMP
* Network Packet Analysis
* Payload Inspection

---

## ⚠️ Disclaimer

This project is intended **only for educational and ethical cybersecurity learning purposes**.

Do not use packet sniffing tools on networks that you do not own or do not have permission to monitor.

---

## 👨‍💻 Author

**Sreeram S P**

B.Tech CSE (Cyber Security)

SRM Institute of Science and Technology, Tiruchirappalli

---

## 📄 License

This project is created for educational purposes as part of the **CodeAlpha Cyber Security Internship**.
