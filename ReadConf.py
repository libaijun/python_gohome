"""
    config demo
"""
import configparser


config = configparser.ConfigParser()
config.read('conf.ini')

process = config['process']
# print(process['process_name'])
# print(process['process_path'])


db = config['db']
# print(db['host'])
# print(db['port'])
# print(db['username'])
# print(db['password'])


mongo = config['mongo']
# print(mongo['host'])
# print(mongo['port'])

