import shutil
from pathlib import Path
import re

def copy_cv_files(base_name: str, source_dir: Path, target_dir: Path):
    """Copy HTML and PDF files from source to target directory."""
    base_path = source_dir / base_name

    html_src = base_path.with_suffix(".html")
    pdf_src = base_path.with_suffix(".pdf")

    html_dest = target_dir / "index.html"
    pdf_dest = target_dir / pdf_src.name

    # Check files exist
    if not html_src.exists() or not pdf_src.exists():
        raise FileNotFoundError(
            f"Missing files in {source_dir}. Ensure both {base_name}.html and {base_name}.pdf exist."
        )

    # Perform copies
    shutil.copy(html_src, html_dest)
    shutil.copy(pdf_src, pdf_dest)

    print(f"Copied {html_src.name} → {html_dest}")
    print(f"Copied {pdf_src.name} → {pdf_dest}")

    return html_dest, pdf_dest


def add_download_link(html_file: Path, pdf_file: Path):
    """Insert a 'Download as PDF' link at the top of the first <ul> in the HTML."""
    html_text = html_file.read_text(encoding="utf-8")

    insert_html = f'\n\t\t<li><a href="{pdf_file.name}" download>Download as PDF</a></li>'

    # Regex: find the first <ul> tag and insert immediately after it
    new_html, count = re.subn(r'(<ul[^>]*>)', r'\1' + insert_html, html_text, count=1)

    if count == 0:
        print(f"Warning: no <ul> found in {html_file}; download link not added.")
    else:
        html_file.write_text(new_html, encoding="utf-8")
        print(f"Added download link at top of first <ul> in {html_file}")


def main():
    base_name = "Arthur_Allilaire_CV"

    script_dir = Path(__file__).parent
    source_dir = script_dir.parent / "render-cv" / "rendercv_output"

    html_dest, pdf_dest = copy_cv_files(base_name, source_dir, script_dir)
    add_download_link(html_dest, pdf_dest)


if __name__ == "__main__":
    main()
