import socket
import tkinter as tk

def scan_ports():
    target = entry_ip.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())

    result_text.delete("1.0", tk.END)  # Clear the result text area

    result_text.insert(tk.END, f"Scanning ports on {target}...\n\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
        sock.settimeout(1)  # Set a timeout of 1 second for the connection attempt
        result = sock.connect_ex((target, port))  # Try to connect to the target IP and port
        if result == 0:  # If the connection attempt is successful (port is open)
            result_text.insert(tk.END, f"Port {port} is open\n")
            result_text.tag_add("open", f"{result_text.index(tk.END)} linestart", f"{result_text.index(tk.END)} lineend")
            result_text.tag_config("open", foreground="lime green")
        else:  # If the connection attempt failed (port is closed)
            result_text.insert(tk.END, f"Port {port} is closed\n")
            result_text.tag_add("closed", f"{result_text.index(tk.END)} linestart", f"{result_text.index(tk.END)} lineend")
            result_text.tag_config("closed", foreground="red")
        sock.close()  # Close the socket connection

# Create the GUI window
window = tk.Tk()
window.title("Network Scanner")
window.configure(bg="black")

# IP address label and entry
label_ip = tk.Label(window, text="Target IP Address:", fg="lime green", bg="black", font=("Courier", 12))
label_ip.pack()
entry_ip = tk.Entry(window, font=("Courier", 12))
entry_ip.pack()

# Starting port label and entry
label_start_port = tk.Label(window, text="Starting Port Number:", fg="lime green", bg="black", font=("Courier", 12))
label_start_port.pack()
entry_start_port = tk.Entry(window, font=("Courier", 12))
entry_start_port.pack()

# Ending port label and entry
label_end_port = tk.Label(window, text="Ending Port Number:", fg="lime green", bg="black", font=("Courier", 12))
label_end_port.pack()
entry_end_port = tk.Entry(window, font=("Courier", 12))
entry_end_port.pack()

# Scan button
button_scan = tk.Button(window, text="Scan Ports", command=scan_ports, fg="black", bg="lime green", font=("Courier", 12, "bold"))
button_scan.pack()

# Result text area
result_text = tk.Text(window, height=10, width=50, bg="black", fg="white", font=("Courier", 12))
result_text.pack()
result_text.tag_config("open", foreground="lime green")
result_text.tag_config("closed", foreground="red")

# Run the GUI window
window.mainloop()