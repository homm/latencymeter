import sys
from japronto import Application


async def hello(request):
    return request.Response(text='hello world')


class Application(Application):
    @property
    def _log_request(self):
        return False

    @_log_request.setter
    def _log_request(self, value):
        pass
    

port = int(sys.argv[1])

app = Application()
app.router.add_route('/', hello)
app.run(debug=False, port=port)
