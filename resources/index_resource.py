class IndexResource:
    def on_get(self, req, resp):
        with open('index.html', 'r') as f:
            html = f.read()
        resp.content_type = 'text/html'
        resp.body = html
