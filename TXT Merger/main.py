import os
from bs4 import BeautifulSoup

input_dir = "./input/"
output_path = "output.txt"

with open(output_path, "w", encoding="utf-8") as output_file:
    for folder in os.listdir(input_dir):
        folder_path = os.path.join(input_dir, folder)
        if os.path.isdir(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith(".html"):
                    file_path = os.path.join(folder_path, filename)

                    with open(file_path, "r", encoding="utf-8") as html_file:
                        soup = BeautifulSoup(html_file, "html.parser")

                    conversation_title = f"{folder}/{filename}"
                    output_file.write(f"\n=== Conversation: {conversation_title} ===\n")

                    sections = soup.find_all("section", class_="_a6-g")
                    for section in sections:
                        sender = section.find("h2").get_text(strip=True)
                        content_div = section.find("div", class_="_a6-p")
                        if content_div:
                            message_divs = content_div.find_all("div")
                            message_text = next(
                                (div.get_text(strip=True) for div in message_divs if div.get_text(strip=True)), "")
                        else:
                            message_text = ""

                        timestamp_div = section.find("footer")
                        timestamp = timestamp_div.get_text(strip=True) if timestamp_div else ""

                        # Write message
                        output_file.write(f"[{timestamp}] {sender}: {message_text}\n")
