import os
import re
import requests

# Your sample text

file_path = "./index.html"
with open(file_path, 'r') as file:
    text= file.read()

# Directory to save the downloads
download_dir = "downloaded_files"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Regex to find URLs
url_pattern = r'(https?:\/\/www\.?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*(?!jpg|png))'

# Function to download a file from a URL
def download_file(url):
    local_filename = url.split('/')[-1]
    path = os.path.join(download_dir, local_filename)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

# Find all URLs in the text
urls = re.findall(url_pattern, text)
print(urls)

# Download each URL found
# for url in urls:
#     try:
#         filename = download_file(url)
#         print(f"Downloaded {url} as {filename}")
#     except Exception as e:
#         print(f"Failed to download {url}: {str(e)}")
