import re

class Parser:

    def __init__(self, flags=0):
        self._match_fns = []
        self._default_flags = flags

    def kv_search(self, key, value=r'(\S+)', sep=':', stop_at='', fmt_fn=None, flags=None, v_type=lambda v: v, k_name=None):
        if k_name is None:
            k_name = key
        key = re.escape(key)
        pattern = rf'{key}\s*?{sep}\s*?{value}{stop_at}'

        if fmt_fn is None:
            fmt_fn = lambda m: (k_name, v_type(m.group(1)))
        return self.re_search(pattern, fmt_fn, flags)
        
    def re_search(self, pattern, fmt_fn=None, flags=None):
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
                text = text[match.end():]
                yield match if fmt_fn is None else fmt_fn(match)
