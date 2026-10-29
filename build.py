"""Build the Manager.io invoice footer.

Edit src/footer.template.html (text) or src/seal.jpg (image), then run:
    python build.py
Outputs:
    dist/footer.html        - classic footer (seal embedded, works in PDFs)
    dist/footer-modern.html - footer styled to match theme/theme.html
    dist/footer-url.html  - same, but loads the seal from GitHub (does NOT show in Manager PDFs)
"""
import base64, re, pathlib

root = pathlib.Path(__file__).parent
def one_line(t):
    # Manager.io now keeps line breaks, so collapse the template to a single line.
    t = re.sub(r">\s+", ">", t.strip())
    return re.sub(r"\s*\n\s*", " ", t)

tpl = one_line((root / "src/footer.template.html").read_text(encoding="utf-8"))

seal = base64.b64encode((root / "src/seal.jpg").read_bytes()).decode()
url = "https://raw.githubusercontent.com/psycho-v1/TPfront/main/src/seal.jpg"

(root / "dist").mkdir(exist_ok=True)
(root / "dist/footer.html").write_text(tpl.replace("{{SEAL}}", "data:image/jpeg;base64," + seal), encoding="utf-8")
(root / "dist/footer-url.html").write_text(tpl.replace("{{SEAL}}", url), encoding="utf-8")

modern = one_line((root / "src/footer-modern.template.html").read_text(encoding="utf-8"))
(root / "dist/footer-modern.html").write_text(modern.replace("{{SEAL}}", "data:image/jpeg;base64," + seal), encoding="utf-8")
print("Built dist/footer.html, dist/footer-modern.html and dist/footer-url.html")
