🔐 Advanced Python Port Scanner

An advanced *Port Scanner* built using Python, designed to provide improved port scanning accuracy, flexible IP and port range validation, and faster scanning experience for deeper cybersecurity exploration.

📌 Project Overview

This tool allows users to scan a specific IP address across a custom-defined port range to detect open TCP ports. With enhanced input validation and optimized scanning using sockets, this tool provides better control and learning for users studying network security.

✅ Features

-  Validate IP address before scanning
-  User-defined start and end port range
-  Fast and efficient scanning using socket connections
-  Clean command-line interface with meaningful feedback
-  Measures scan duration and displays total time taken

🛠 Technologies Used

- Python 3.x
- socket – For handling network connections
- re – For validating IP addresses using regex
- time – To measure scanning performance


📸example output

PS C:\Users\karth\OneDrive\Desktop\cyber projects> python advanced_port_scanner.py

Enter the IP address to scan: 127.0.0.1

Enter start port (e.g., 20): 30

Enter end port (e.g., 80): 99

Scanning 127.0.0.1 from port 30 to 99...


Scan complete.

Total Open Ports: 0

Time Taken: 35.67 seconds

🎯 Learning Objectives

-This project was built as part of my cybersecurity learning journey to:

-Learn advanced input validation with regex

-Understand efficient socket usage

-Improve error handling for port scanning tools

-Practice responsible ethical hacking concepts


📊 Project Status

✅ Completed — stable for learning and experimentation.

📜 License

This project is strictly for educational and ethical use only. Unauthorized scanning of networks without permission is illegal and discouraged.

👨‍💻 Author

Muthusamy T.

B.Sc Cybersecurity Student

Vels University, Chennai (Pallavaram)

GitHub: muthu-23

💡 Future Enhancements

-Add multi-threading for faster scans

-Integrate real-time progress bar

-Export scan results to CSV or JSON

-Add options for scanning remote hosts
