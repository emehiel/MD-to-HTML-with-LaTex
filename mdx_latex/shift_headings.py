from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
import re


class ShiftHeadingsTreeprocessor(Treeprocessor):
    """Treeprocessor that shifts heading levels by a configured offset.

    It walks the ElementTree and adjusts tags h1..h6 to new levels.
    """

    def __init__(self, md, offset=1):
        super().__init__(md)
        try:
            self.offset = int(offset)
        except Exception:
            self.offset = 1

    def run(self, root):
        for el in list(root.iter()):
            # el.tag may be a callable in some non-HTML trees; ensure it's a string
            if not isinstance(el.tag, str):
                continue
            tag = el.tag.lower()
            m = re.fullmatch(r'h([1-6])', tag)
            if not m:
                continue
            level = int(m.group(1))
            new_level = min(6, max(1, level + self.offset))
            el.tag = f'h{new_level}'
        return root


class ShiftHeadingsExtension(Extension):
    """Markdown extension to register the ShiftHeadingsTreeprocessor.

    Config options:
      - offset: integer amount to add to heading levels (default: 1)
    """

    def __init__(self, **kwargs):
        self.config = {
            'offset': [1, 'Heading level offset (int)']
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        offset = self.getConfig('offset')
        md.treeprocessors.register(ShiftHeadingsTreeprocessor(md, offset), 'shift_headings', 15)


def makeExtension(**kwargs):
    return ShiftHeadingsExtension(**kwargs)
