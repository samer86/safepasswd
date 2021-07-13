#!/usr/bin/env python3
from random import choices
import questionary
from bashcmd import *
from generatepass import GeneratePass as gpass
import pandas as pd
from sqlite_object import database as db
from question import question
from pyfiglet import Figlet
import os
import csv


# def makeConfig():
#     os.chdir('/')
#     selected_path = question('path', 'Select main app folder')
#     config_dictionary = dict(path=selected_path,
#                              email=question('text', 'Enter Recipian recipient email'))
#     os.chdir(selected_path)
#     with open('config', 'w+') as csvfile:
#         x = [f'{k}: {v}\n' for k, v in config_dictionary.items()]
#         csvfile.writelines(x)
#     class conf:
#         pass
#     config = conf()
#     for k, v in config_dictionary.items():
#         try:
#             config.__dict__[k] = v
#         except Exception as e:
#             ''
#     return config


def readConfig():
    class conf:
        pass
    config = conf()
    try:
        with open('config', 'r') as f:
            reader = csv.reader(f, delimiter=':')
            for row in reader:
                try:
                    config.__dict__[row[0]] = row[1].strip()
                except:
                    ''
        return config
    except Exception as e:
        raise e


def commander(cmd):
    cmdOutput = testRun(cmd)[0]
    encryptKey = cmdOutput.decode('utf-8')
    return encryptKey


def y(x): return dbObject.query(x)


class row():
    pass


def encryptedKey(rowKey, email):
    cmd = f'''echo {rowKey} |gpg --encrypt --armor  -r {email}'''
    cmdOutput = testRun(cmd)[0]
    encryptKey = cmdOutput.decode('utf-8')
    # encryptKey = cmdOutput
    return encryptKey


def makeEntry(email):
    entry = row()
    # question('print', 'CTRL+D get you back to main menu.', style='bold')
    questionary.print('CTRL+D get you back to main menu.', style='bold')
    try:
        while True:
            entry.Program = question('text', 'Enter Program Name: ')
            entry.Details = question('text', 'Enter App details:\n')
            entry.UserName = question('text', 'Enter UserName: ')
            if question('confirm', 'Enter Password?'):
                unencryptedKey = question('text', 'Enter a password: ')
            else:
                unencryptedKey = gpass(20)
            if None not in (entry.Program, entry.Details, entry.UserName, unencryptedKey):
                print('Summary:\n')
                print('Program: '+entry.Program)
                print('Details: '+entry.Details)
                print('User name: '+entry.UserName)
                print(f'Generated password: {unencryptedKey}')
            else:
                print('Some of the options has no value')
                return None
            if question('confirm', 'Does it look right? '):
                break
        entry.key = encryptedKey(unencryptedKey, email)
    except Exception as e:
        print(e)
        return None
    return entry


def sendEntrytoDb(row):
    if row is not None:
        if question('confirm', 'Send Encrypted Credentials to db?'):
            e = pd.DataFrame([row.__dict__])
            e.to_sql(
                con=dbObject.conn, name='main', if_exists='append', index=False)
        else:
            question('print', 'Credentials discarded!', style='bold')
    else:
        print('No entry saved!')


def getAppList():
    return y('select * from main')


def search(x):
    table = y(
        f'select id ,Program, Details, UserName from main where Program like "%{x}%" or Details like "%{x}%" or UserName like "%{x}%"')
    return table


def decrypt(x):
    credentials = y(f'select * from main where id = "{x}"')
    result = testRun(f''' echo "{credentials.key[0]}"| gpg''')
    try:
        print('Credentials:')
        print(f'App Name: {credentials.Program[0]}')
        print(f'Details: {credentials.Details[0]}')
        print('User Name: ' + credentials.UserName[0])
        copy2clip(result[0].decode('utf-8').strip())
        # print(f"Password: {result[0].decode('utf-8').strip()}")
        print(f"Password: o_O")
    except Exception as e:
        print(e)


def deleteEntry():
    x = input('Enter id for entry to delete: ')
    print(y(f'select * from main where id = "{x}"'))
    confirmation = input('For deleting the Above Entery type yes: ')
    if confirmation == 'yes':
        y(f'delete from main where id = {x}')
        dbObject.commit()


def main():
    # Change get the workding directory from the link:
    os.chdir(os.path.dirname(os.path.abspath(os.readlink(__file__))))
    config = readConfig()
    global dbObject
    dbObject = db('container.db')
    f = Figlet(font='slant')
    print(f.renderText('Password'))
    questionary.print(f.renderText('Blackhole!'), style='bold')
    while True:
        choice = question('select', 'Choose a command:', choices=[
            'Add new entery', 'Find entery', 'Delete entery',  'Decrypt entery', 'Exit'])
        if choice == 'Add new entery':
            sendEntrytoDb(makeEntry(config.email))
        if choice == 'Find entery':
            print(search(input('Search for: ')))
        if choice == 'Delete entery':
            deleteEntry()
        if choice == 'Decrypt entery':
            decrypt(input('Id for the credentials: '))
            break
        if choice == 'Exit':
            # commander(closeFile)
            break


if __name__ == '__main__':
    main()
