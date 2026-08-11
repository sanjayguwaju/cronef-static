import os
import glob

html_files = glob.glob('*.html')

target_block = """        <div class="brand">
          <img src="imgs/logo.png" alt="CRONEF" style="height: 36px; width: auto; filter: brightness(0) invert(1);">
        </div>"""

new_block = """        <div class="brand">
          <img src="imgs/logo.png" alt="CRONEF" style="height: 44px; width: auto; background: var(--paper); padding: 4px 10px; border-radius: 6px;">
        </div>"""

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()
    
    if target_block in content:
        content = content.replace(target_block, new_block)
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Target block not found in {file}")
