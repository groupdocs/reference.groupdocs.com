#!/usr/bin/env python3
"""Static server for ./public-local that sends charset=utf-8 for text responses.

Plain `python -m http.server` serves .txt/.md without a charset, so UTF-8 punctuation
(—, →) renders as mojibake (â€", â†') in the browser. Production sends
`; charset=utf-8` via the S3 deploy matchers, so this just makes local preview faithful.

Usage:  python serve-local.py [port]      # default 1313, serves ./public-local
"""
import functools
import http.server
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 1313


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, ".md": "text/markdown"}

    def guess_type(self, path):
        t = super().guess_type(path)
        if t and t.startswith("text/") and "charset" not in t:
            t += "; charset=utf-8"
        return t


with socketserver.TCPServer(("127.0.0.1", PORT), functools.partial(Handler, directory="public-local")) as httpd:
    print("Serving ./public-local at http://127.0.0.1:%d/ (text responses as UTF-8)" % PORT)
    httpd.serve_forever()
