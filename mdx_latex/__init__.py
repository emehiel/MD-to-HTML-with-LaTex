"""
LaTeX Extension for Python-Markdown
===============================

Adds support for LaTeX math equations in markdown for use in Canvas.
"""
from markdown.extensions import Extension
from markdown.inlinepatterns import Pattern
import xml.etree.ElementTree as etree
import urllib.parse
import re
from .shift_headings import ShiftHeadingsTreeprocessor

"""Regex patterns:
LATEX_DISPLAY_PATTERN: matches display math between $$...$$
LATEX_INLINE_PATTERN: matches inline math between single $...$ but avoids matching $$ (uses lookarounds)
"""
LATEX_DISPLAY_PATTERN = r'\$\$(.+?)\$\$'  # Matches $$equation$$ (display math)
LATEX_INLINE_PATTERN = r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)'  # Matches $equation$ (inline math), not $$

class LatexPattern(Pattern):
    def handleMatch(self, m):
        """Convert LaTeX math equation to HTML."""
        equation = m.group(2)
        # Percent-encode the equation so it can safely be used in URLs or data attributes
        equation_encoded = urllib.parse.quote(equation, safe='')

        img = etree.Element('img')
        # define class 'equation_image' for use in Canvas
        img.set('class', 'equation_image')
        img.set('title', equation)
        # Use the encoded equation in the src URL
        img.set('src', f"https://canvas.calpoly.edu/equation_images/{equation_encoded}?scale=1")
        img.set('alt', f"LaTeX: {equation}")
        img.set('data-equation-content', equation)
        # also provide a percent-encoded form of the LaTeX for safe URLs/attributes
        img.set('data-latex-encoded', equation_encoded)
        img.set('data-ignore-a11y-check', '')
        return img

class LatexExtension(Extension):
    def __init__(self, **kwargs):
        # configuration: shift_headings_offset controls heading shifting
        # 0 disables shifting, positive integers shift headings by that offset
        self.config = {
            'shift_headings_offset': [0, 'Heading level offset to apply (0 = disabled)']
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        """Add LaTeX pattern to markdown patterns and optionally register heading shifter."""
        # Optionally register the heading-shifting treeprocessor if configured
        try:
            offset = int(self.getConfig('shift_headings_offset'))
        except Exception:
            offset = 0

        if offset != 0:
            md.treeprocessors.register(ShiftHeadingsTreeprocessor(md, offset), 'shift_headings', 15)

        # Register display math first (higher priority) so $$...$$ isn't picked up by the inline $ pattern
        display_pattern = LatexPattern(LATEX_DISPLAY_PATTERN, md)
        md.inlinePatterns.register(display_pattern, 'latex-display', 175)

        # Register inline math pattern (lower priority)
        inline_pattern = LatexPattern(LATEX_INLINE_PATTERN, md)
        md.inlinePatterns.register(inline_pattern, 'latex-inline', 170)

def makeExtension(**kwargs):
    """Return extension."""
    return LatexExtension(**kwargs)