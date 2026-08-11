import os
import glob
import shutil

# Rename contact.html to contact-us.html if it exists
if os.path.exists("contact.html"):
    shutil.move("contact.html", "contact-us.html")
    print("Renamed contact.html to contact-us.html")

# Update all references in all HTML and JS files
files_to_check = glob.glob("*.html") + glob.glob("js/*.js")

for file in files_to_check:
    with open(file, 'r') as f:
        content = f.read()
    
    if "contact.html" in content:
        content = content.replace("contact.html", "contact-us.html")
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated links in {file}")
