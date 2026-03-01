from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf(toc_level=0)
with open("assets/resume_leanlinmy.md", "r", encoding="utf-8") as f:
    content = f.read()

# Custom CSS to shrink the margins and font sizes, ensuring it fits on one page
css = """
body {
    font-size: 8px;
    font-family: Georgia, serif;
    line-height: 1.5;
}
h2 {
    font-size: 11px;
    margin-top: 3px;
    margin-bottom: 2px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 2px;
}
h3 {
    font-size: 9px;
    margin-top: 2px;
    margin-bottom: 1px;
}
h4 {
    font-size: 8px;
    margin-top: 2px;
    margin-bottom: 1px;
}
p, ul, li {
    margin-top: 2px;
    margin-bottom: 2px;
}
/* Reduce page margins */
@page {
    margin: 0.2cm 0.5cm;
}
"""

# Add section to PDF with custom CSS
pdf.add_section(Section(content, toc=False), user_css=css)
pdf.save("assets/resume_leanlinmy.pdf")
print("PDF generated successfully at assets/resume_leanlinmy.pdf")
