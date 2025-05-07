
import os
import zipfile
from uuid import uuid4

BASE_PATH = "output"

REACT_TEMPLATE = {
    "index.html": """<html><head><title>{name}</title></head><body><h1>{description}</h1></body></html>"""
}

HTML_TEMPLATE = {
    "index.html": """<html><head><title>{name}</title></head><body><p>{description}</p></body></html>"""
}

def build_app_code(payload):
    folder_id = str(uuid4())
    app_dir = os.path.join(BASE_PATH, folder_id)
    os.makedirs(app_dir, exist_ok=True)

    if payload.template_id == "react-basic":
        template = REACT_TEMPLATE
    else:
        template = HTML_TEMPLATE

    for filename, content in template.items():
        with open(os.path.join(app_dir, filename), "w") as f:
            f.write(content.format(name=payload.name, description=payload.description or "Generated App"))

    zip_path = f"{app_dir}.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(app_dir):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, app_dir)
                zipf.write(full_path, arcname)

    return f"/downloads/{folder_id}.zip"

