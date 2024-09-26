import re

class Parser:

    def __init__(self, fmt_fn=None, flags=0):

        self._match_fns = []
        self._default_fmt_fn = fmt_fn
        self._default_flags = flags

    def kv_search(self, key, value=r'(\S+)', sep=':', endwith='', fmt_fn=None, flags=None):
        key = re.escape(key)
        endwith = re.escape(endwith)
        pattern = rf'\s*({key})\s*{sep}\s*{value}{endwith}'
        if fmt_fn is None and self._default_fmt_fn is None:
            fmt_fn = lambda m: m.groups()
        return self.re_search(pattern, fmt_fn, flags)
    
        
    def re_search(self, pattern, fmt_fn=None, flags=None):
        if fmt_fn is None:
            fmt_fn = self._default_fmt_fn
        if flags is None:
            flags = self._default_flags
        def match_fn(text):
            return re.search(pattern, text, flags)
        self._match_fns.append((match_fn, fmt_fn))
        return self
    
    def parse(self, text: str):
        for match_fn, fmt_fn in self._match_fns:
            match = match_fn(text)
            if match:
                text = text[match.end():]  # this is not efficient
                yield match if fmt_fn is None else fmt_fn(match)
            
