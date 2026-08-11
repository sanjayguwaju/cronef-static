import os
import glob
import shutil

# Rename contact-us.html to contact.html if it exists
if os.path.exists("contact-us.html"):
    shutil.move("contact-us.html", "contact.html")

# Update all references in all HTML and JS files
files_to_check = glob.glob("*.html") + glob.glob("js/*.js")

for file in files_to_check:
    with open(file, 'r') as f:
        content = f.read()
    
    if "contact-us.html" in content:
        content = content.replace("contact-us.html", "contact.html")
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated links in {file}")
