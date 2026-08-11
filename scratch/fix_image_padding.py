import os
import glob
import re

html_files = glob.glob("*.html")

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()

    # We want to find <div class="about-card reveal"> or <div class="about-card reveal" style="order: 2;"> 
    # that immediately contains an <img class="about-img"...
    # A simple regex replacement: 
    # <div class="about-card reveal">
    #   <img class="about-img"
    
    # Let's replace <div class="about-card reveal"> with <div class="about-card reveal" style="padding: 0; overflow: hidden;">
    # but only if it's the one wrapping the image.
    
    # Since in our template all .about-card elements are used for images, let's check if there are any that aren't.
    # We can just blindly add padding: 0; overflow: hidden; if it's wrapping an image.
    
    pattern1 = re.compile(r'<div class="about-card reveal">\s*<img class="about-img"', re.MULTILINE)
    replacement1 = r'<div class="about-card reveal" style="padding: 0; overflow: hidden;">\n      <img class="about-img"'
    
    pattern2 = re.compile(r'<div class="about-card reveal" style="order: 2;">\s*<img class="about-img"', re.MULTILINE)
    replacement2 = r'<div class="about-card reveal" style="order: 2; padding: 0; overflow: hidden;">\n      <img class="about-img"'

    new_content = pattern1.sub(replacement1, content)
    new_content = pattern2.sub(replacement2, new_content)
    
    # Let's also make sure the images themselves don't have border-radius if the container is handling it
    # Actually container has border-radius, so overflow: hidden takes care of it, but keeping it on img is fine.
    # Let's also ensure object-fit: cover is on the image.
    
    # We will do a generic replacement for the img to ensure object-fit: cover
    def add_object_fit(match):
        img_tag = match.group(0)
        if 'object-fit: cover' not in img_tag:
            if 'style="' in img_tag:
                img_tag = img_tag.replace('style="', 'style="object-fit: cover; ')
            else:
                img_tag = img_tag.replace('<img ', '<img style="object-fit: cover;" ')
        return img_tag
        
    img_pattern = re.compile(r'<img class="about-img"[^>]+>')
    new_content = img_pattern.sub(add_object_fit, new_content)

    if content != new_content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
