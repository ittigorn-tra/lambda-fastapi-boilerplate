from src.root import app
from mangum import Mangum


handler = Mangum(app, lifespan="on")
