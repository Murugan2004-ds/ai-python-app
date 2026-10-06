from src.api_client import get_github_user
from src.document import Document
from src.loader import load_text
from src.storage import save_json, load_json

def main():
    text = load_text("sample.txt")
    if text is None:
        return

    doc = Document("Sample",text)
    user =get_github_user("Murugan2004-ds")
    if user is None:
        return

    result = {
        "title":doc.title,
        "cleaned_text": doc.cleaned(),
        "github_user": user["login"],
        "public_repos": user["public_repos"],
    }
    save_json(result,"result.json")
    print("Saved result.json")
    print(result)


if __name__== "__main__":
    main()    