async def app(scope, receive, send):
    """
    Test type 6: Plaintext
    """
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain; charset=utf-8'],
            [b'content-length', b'11'],
        ]
    })
    await send({
        'type': 'http.response.body',
        'body': b'hello world',
        'more_body': False
    })
