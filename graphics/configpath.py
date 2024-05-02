import os

def uploadImage(image):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, "assets")
    final = os.path.join(assets_dir, f"{image}")
    return final

def pathJson():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, "config.json")
    return assets_dir

def requirements():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(script_dir, "requirements.txt")
    return assets_dir