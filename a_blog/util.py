import re
from django import forms
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """

    """
    _, filenames = default_storage.listdir("blogs")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content, pan):
    """

    """
    filename = f"blogs/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content, pan))


def get_entry(title):
    """

    """
    try:
        f = default_storage.open(f"blogs/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
