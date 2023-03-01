import os
import dotenv

dotenv.load_dotenv()

token_vk = 'vk1.a.LQYq1bIYr80_VNEWIa2qSE8VJZSP1MLKKf-Pasm9PtB9ysybEjliSz_SDnoj5b05KS_Yl_wit_OiPUDSeixNSLQxAe4Y0wG8rTNReVy5xHVNAB7wV0nJTHS3RaSPF7rbrLdzNMIENNawswrtCuwvPkkzHhDq6b_PsLpqjaAOb5Y8MS0tMueAhPVUxzHqEmaTvnOHnwHiJjDhxJDmAXYUaA'
token_bot = 'vk1.a.U-YNNf8HBUEkONfuhQo4wFiR4GXQ-1eC4FW0NbTYj8rYoXR-FFOhEJXzjp3d7c8AXNbZq7Xm68SNmZYQSMklcw-8oOx2JL3ocG5SHqBO9jOo8OlCndqc77COLE96XzzZGPHHLp48mRRAcqWHwPjWH0epq-faSohfiRw4JhItaoNfmoa1iUjiTiFuOKtfCRH4SkeflZhCMBhfxD7njyz1OA'

PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))
ip = os.getenv('ip')

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'

resetdb = 1