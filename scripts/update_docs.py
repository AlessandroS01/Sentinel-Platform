import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Configuration
ROOT_DIR = Path(__file__).parent.parent
README_PATH = ROOT_DIR / "README.md"
IGNORE_DIRS = {".git", ".idea", "__pycache__", "scripts", ".air", "data"}


def get_project_structure(root_path: Path) -> str:
    """Scans the directory and returns a text map of the architecture."""
    structure = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        level = str(dirpath).replace(str(root_path), "").count(os.sep)
        indent = " " * 4 * level
        structure.append(f"{indent}{os.path.basename(dirpath)}/")

        for f in filenames:
            if f.endswith((".py", ".txt", ".md", "Dockerfile", ".env")):
                structure.append(f"{indent}    {f}")
    return "\n".join(structure)


def get_current_readme(path: Path) -> str:
    """Retrieves the existing README to preserve manual context."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "No existing README found. Please generate a new one from scratch."


def update_readme():
    load_dotenv()
    print("Scoping repository architecture...")
    tree = get_project_structure(ROOT_DIR)
    current_readme = get_current_readme(README_PATH)

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a senior AI engineer maintaining the Sentinel Platform monorepo. "
                "Your job is to update the repository's README.md file. "
                "Preserve the tone, formatting, and manual descriptions from the existing README, "
                "but update the 'Repository Architecture' or folder tree sections to perfectly match "
                "the new physical architecture provided. Output ONLY the raw Markdown code.",
            ),
            (
                "user",
                "Here is the EXISTING README:\n\n{current_readme}\n\n"
                "---\n\n"
                "Here is the NEW physical architecture of the repository:\n\n{tree}\n\n"
                "Generate the updated README.md.",
            ),
        ]
    )

    # Initialize the Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        temperature=0.1, 
        max_retries=2,
    )
    chain = prompt | llm

    print("Merging updates with Gemini...")
    new_readme = chain.invoke({"tree": tree, "current_readme": current_readme})

    # Clean up markdown code blocks if the LLM wraps the response in them
    final_content = (
        new_readme.content.removeprefix("```markdown\n")
        .removeprefix("```\n")
        .removesuffix("\n```")
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(final_content)

    print("Success! README.md has been intelligently synchronized.")


if __name__ == "__main__":
    update_readme()
