#!/usr/bin/env python3
from server import create_app
import uvicorn

app = create_app()


if __name__ == '__main__':
    config = uvicorn.Config(app, port=5000, log_level='info')
    server = uvicorn.Server(config)
    server.run()
    
