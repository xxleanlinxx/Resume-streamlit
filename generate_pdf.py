from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf(toc_level=0)
with open("assets/resume_leanlinmy.md", "r", encoding="utf-8") as f:
    content = f.read()

css = """
body {
    font-size: 8px;
    font-family: Georgia, serif;
    line-height: 1.5;
}
h1 {
    font-size: 13px;
    margin-top: 0px;
    margin-bottom: 1px;
}
h2 {
    font-size: 10px;
    margin-top: 2px;
    margin-bottom: 1px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 1px;
}
h3 {
    font-size: 8.5px;
    margin-top: 2px;
    margin-bottom: 0px;
}
h4 {
    font-size: 8px;
    margin-top: 1px;
    margin-bottom: 0px;
}
p, ul, li {
    margin-top: 1px;
    margin-bottom: 1px;
}
ul {
    padding-left: 14px;
}
@page {
    margin-top: 0.05cm;
    margin-bottom: 0.15cm;
    margin-left: 0.5cm;
    margin-right: 0.5cm;
}
"""

pdf.add_section(Section(content, toc=False), user_css=css)
pdf.save("assets/resume_leanlinmy.pdf")
print("PDF generated successfully at assets/resume_leanlinmy.pdf")
