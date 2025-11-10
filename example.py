import markdown

# Create sample markdown text with LaTeX equations
#markdown_text = 
"""
# Math Example

Here's a LaTeX equation:

$$f(x) = \frac{x}{y} \sin (\omega t)$$

And some regular text.

Here's another equation:

$$E = mc^2$$
"""
# Expected HTML output:
"""
<p>
    <img class="equation_image" 
    title="f(x) = \frac{x}{y} \sin (\omega t) " 
    src="https://canvas.calpoly.edu/equation_images/f(x)%2520%253D%2520%255Cfrac%257Bx%257D%257By%257D%2520%255Csin%2520(%255Comega%2520t)%2520?scale=1" 
    alt="LaTeX: f(x) = \frac{x}{y} \sin (\omega t) " 
    data-equation-content="f(x) = \frac{x}{y} \sin (\omega t) " 
    data-ignore-a11y-check="" />
</p>
"""
with open("test.md", "r") as f:
    markdown_content = f.read()
    
# Create Markdown instance with LaTeX extension and enable heading shifting here
# Use the extension tuple form to pass config: shift_headings_offset will shift headings by the given amount
md = markdown.Markdown(extensions=['mdx_latex'], extension_configs={'mdx_latex': {'shift_headings_offset': 1}})

# Convert to HTML (the extension will perform heading shifting if configured)
html = md.convert(markdown_content)

print(html)