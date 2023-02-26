import os
import dotenv

token_vk = ''
token_bot = ''

dotenv.load_dotenv()

PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))
ip = os.getenv('ip')

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'

resetdb = 0