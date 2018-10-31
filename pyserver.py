#!/usr/bin/env python3

import socket
import time
import ast
import os

env = {}

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

#You can put things that run before or after the main loop here
def start():
    print("Starting Service")
    update()
    loop()
    print("Shutting down")

#Starts a socket server used for testing
def startsocket():
    rdebug("Starting socket server")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        rdebug("Socket Open")
        s.listen()
        conn, addr = s.accept()
        with conn:
            rdebug('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

def loop():
    global env
    while env["turn_on_flag"] == "True":
        rdebug(env)
        run()
        time.sleep(5)
        update()

def run():
    global env
    if ("socket_server_up" in env and env["socket_server_up"] == "True"):
        startsocket()
    return 0

def update():
    global env
    changes, result = checkchanges()
    if changes:
        #If there are changes then modify accordingly
        env = result
        g = open("env.txt","w")
        g.write(str(env))
        g.close()
    rdebug("Changes to env since last run : " + str(changes))

def checkchanges():
    global env
    f = open("env.txt", "r")
    readinfo = f.read()
    f.close()
    newenv = {}
    if(readinfo != ""):
        newenv = eval(readinfo)
    if env != newenv:
        return True, newenv
    else:
        return False, ""

def rdebug(target):
    global env
    if(env["debug_flag"] == "True"):
        print(target)

#INIT
start()