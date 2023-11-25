import requests
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageSequence
from threading import Timer

def scrape_http():
    http_proxies = []

    url_http_proxywizard = 'https://raw.githubusercontent.com/d7emy/Proxy-Wizard/main/output.txt'
    response_http_proxywizard = requests.get(url_http_proxywizard)
    http_proxies += [proxy.replace('http://', '') for proxy in response_http_proxywizard.text.split('\n') if proxy]

    url_http_proxyscrape = 'https://api.proxyscrape.com/?request=getproxies&proxytype=http'
    response_http_proxyscrape = requests.get(url_http_proxyscrape)
    http_proxies += [proxy for proxy in response_http_proxyscrape.text.split('\n') if proxy]

    url_http_prxchk = 'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt'
    response_http_prxchk = requests.get(url_http_prxchk)
    http_proxies += [proxy for proxy in response_http_prxchk.text.split('\n')]

    url_socks5_additional = 'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt'
    response_socks5_additional = requests.get(url_socks5_additional)
    http_proxies += [proxy for proxy in response_socks5_additional.text.split('\n')]

    url_http_additional = 'https://github.com/proxy4parsing/proxy-list/raw/main/http.txt'
    response_http_additional = requests.get(url_http_additional)
    http_proxies += [proxy for proxy in response_http_additional.text.split('\n')]

    url_http_casals = 'https://raw.githubusercontent.com/casals-ar/proxy-list/main/http'
    response_http_casals = requests.get(url_http_casals)
    http_proxies += [proxy for proxy in response_http_casals.text.split('\n')]

    url_http_vakhov = 'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt'
    response_http_vakhov = requests.get(url_http_vakhov)
    http_proxies += [proxy for proxy in response_http_vakhov.text.split('\n')]

    url_http_zaeem20 = 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt'
    response_http_zaeem20 = requests.get(url_http_zaeem20)
    http_proxies += [proxy for proxy in response_http_zaeem20.text.split('\n')]

    url_http_monosans = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt'
    response_http_monosans = requests.get(url_http_monosans)
    http_proxies += [proxy for proxy in response_http_monosans.text.split('\n')]

    return http_proxies

def scrape_socks4():
    socks4_proxies = []

    url_socks4_monosans = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt'
    response_socks4_monosans = requests.get(url_socks4_monosans)
    socks4_proxies += [proxy for proxy in response_socks4_monosans.text.split('\n')]

    url_socks4_zaeem20 = 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt'
    response_socks4_zaeem20 = requests.get(url_socks4_zaeem20)
    socks4_proxies += [proxy for proxy in response_socks4_zaeem20.text.split('\n')]

    url_socks4_vakhov = 'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt'
    response_socks4_vakhov = requests.get(url_socks4_vakhov)
    socks4_proxies += [proxy for proxy in response_socks4_vakhov.text.split('\n')]

    url_socks4_casals = 'https://raw.githubusercontent.com/casals-ar/proxy-list/main/socks4'
    response_socks4_casals = requests.get(url_socks4_casals)
    socks4_proxies += [proxy for proxy in response_socks4_casals.text.split('\n')]

    url_socks4_prxchk = 'https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt'
    response_socks4_prxchk = requests.get(url_socks4_prxchk)
    socks4_proxies += [proxy for proxy in response_socks4_prxchk.text.split('\n')]

    url_socks4_proxyscrape = 'https://api.proxyscrape.com/?request=getproxies&proxytype=socks4'
    response_socks4_proxyscrape = requests.get(url_socks4_proxyscrape)
    socks4_proxies += [proxy for proxy in response_socks4_proxyscrape.text.split('\n') if proxy]

    return socks4_proxies

def scrape_socks5():
    socks5_proxies = []

    url_socks5_monosans = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt'
    response_socks5_monosans = requests.get(url_socks5_monosans)
    socks5_proxies += [proxy for proxy in response_socks5_monosans.text.split('\n')]

    url_socks5_zaeem20 = 'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt'
    response_socks5_zaeem20 = requests.get(url_socks5_zaeem20)
    socks5_proxies += [proxy for proxy in response_socks5_zaeem20.text.split('\n')]

    url_socks5_vakhov = 'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt'
    response_socks5_vakhov = requests.get(url_socks5_vakhov)
    socks5_proxies += [proxy for proxy in response_socks5_vakhov.text.split('\n')]

    url_socks5_casals = 'https://raw.githubusercontent.com/casals-ar/proxy-list/main/socks5'
    response_socks5_casals = requests.get(url_socks5_casals)
    socks5_proxies += [proxy for proxy in response_socks5_casals.text.split('\n')]

    url_socks5_prxchk = 'https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt'
    response_socks5_prxchk = requests.get(url_socks5_prxchk)
    socks5_proxies += [proxy for proxy in response_socks5_prxchk.text.split('\n')]

    url_socks5_proxyscrape = 'https://api.proxyscrape.com/?request=getproxies&proxytype=socks5'
    response_socks5_proxyscrape = requests.get(url_socks5_proxyscrape)
    socks5_proxies += [proxy for proxy in response_socks5_proxyscrape.text.split('\n') if proxy]

    return socks5_proxies

def save_to_file(proxies, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join(proxies))

# Read proxies from file and remove duplicates
def remove_duplicates(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Use a set to remove duplicates
    unique_lines = set(lines)

    with open(filename, 'w') as file:
        file.write(''.join(unique_lines))

def scrape_and_update():
    # Scrape and save HTTP proxies
    http_proxies = scrape_http()
    save_to_file(http_proxies, 'http.txt')
    remove_duplicates('http.txt')

    # Scrape and save SOCKS4 proxies
    socks4_proxies = scrape_socks4()
    save_to_file(socks4_proxies, 'socks4.txt')
    remove_duplicates('socks4.txt')

    # Scrape and save SOCKS5 proxies
    socks5_proxies = scrape_socks5()
    save_to_file(socks5_proxies, 'socks5.txt')
    remove_duplicates('socks5.txt')

    # Update the UI with the status
    status_label.config(text="Proxies scraped and updated!")

    # Display a pop-up message
    messagebox.showinfo("Proxies Scraped", "All proxies have been scraped successfully!")

    # Schedule the next update if the checkbox is selected
    if reloading_var.get():
        Timer(600, scrape_and_update).start()  # 600 seconds = 10 minutes

def on_exit():
    root.destroy()

# Function to download the GIF from the URL
def download_gif(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)

# Download the GIF from the provided URL
gif_url = "https://i.pinimg.com/originals/7f/ff/57/7fff576fe1e9583a9d83d38b3c2ddaaf.gif"
download_gif(gif_url, "proxy_scraper.gif")

# Tkinter UI setup
root = tk.Tk()
root.title("Proxy Leecher v1 by detective | t.me/undecryptable")  # Set the title
root.iconbitmap("logo.ico")  # Set the icon

# Load and display the GIF using Pillow
gif_path = "proxy_scraper.gif"
gif = Image.open(gif_path)
frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif)]

label = tk.Label(root)
label.pack()

# Scrape button
scrape_button = ttk.Button(root, text="Scrape", command=scrape_and_update)
scrape_button.pack()

# Checkbox for reloading after 10 minutes
reloading_var = tk.BooleanVar()
reload_checkbox = ttk.Checkbutton(root, text="Keep reloading every 10 minutes", variable=reloading_var)
reload_checkbox.pack()

# Status label
status_label = ttk.Label(root, text="")
status_label.pack()

# Exit button
exit_button = ttk.Button(root, text="Exit", command=on_exit)
exit_button.pack()

# Function to update the animated GIF
def update_gif(frame_num):
    frame = frames[frame_num]
    label.configure(image=frame)
    label.image = frame
    root.after(100, update_gif, (frame_num + 1) % len(frames))

# Start updating the GIF frames
root.after(0, update_gif, 0)

# Start the Tkinter event loop
root.mainloop()
