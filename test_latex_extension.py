import unittest
import markdown

class TestLatexExtension(unittest.TestCase):
    def setUp(self):
        self.md = markdown.Markdown(extensions=['mdx_latex'])

    def test_simple_equation(self):
        text = "$$E = mc^2$$"
        html = self.md.convert(text)
        self.assertIn('class="equation_image"', html)
        # encoded attribute should exist and spaces should be percent-encoded
        self.assertIn('%20', html)

    def test_complex_equation(self):
        # use a raw string so backslashes are preserved (e.g. \frac)
        text = r"$$f(x) = \frac{x}{y} \sin (\omega t)$$"
        html = self.md.convert(text)
        self.assertIn('class="equation_image"', html)
        # the encoded value should include percent-encoded backslash (\ -> %5C)
        self.assertIn('%5Cfrac', html)

    def test_mixed_content(self):
        text = "Regular text\n$$E = mc^2$$\nMore text"
        html = self.md.convert(text)
        self.assertIn('class="equation_image"', html)
        self.assertIn('Regular text', html)
        self.assertIn('More text', html)

    def test_shift_headings_offset(self):
        # Create a Markdown instance that enables heading shifting via the main extension config
        md_shift = markdown.Markdown(extensions=['mdx_latex'], extension_configs={'mdx_latex': {'shift_headings_offset': 1}})
        md_no_shift = markdown.Markdown(extensions=['mdx_latex'])

        source = """
# Title

## Subtitle

Content
"""
        html_shifted = md_shift.convert(source)
        html_no_shift = md_no_shift.convert(source)

        # Without shift, top-level heading is <h1>
        self.assertIn('<h1', html_no_shift)
        # With shift offset=1, the <h1> should become <h2>
        self.assertIn('<h2', html_shifted)
        # Ensure subtitle moved from h2 to h3 when shifted
        self.assertIn('<h3', html_shifted)

if __name__ == '__main__':
    unittest.main()