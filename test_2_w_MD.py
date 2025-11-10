import markdown

# Create a sample Markdown file
with open("sample.md", "w") as f:
    f.write("""
# File Example

This is content from a **Markdown file**.
""")

with open("test.md", "r") as f:
    markdown_content = f.read()

html_output = markdown.markdown(markdown_content)

with open("output.html", "w") as f:
    f.write(html_output)

print("Converted sample.md to output.html")