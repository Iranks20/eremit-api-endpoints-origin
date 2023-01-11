from email.mime import application
from flask import Flask, redirect, request,url_for, render_template
from helper.dbhelper import DB as DB_CON
import jwt
from functools import wraps


application = Flask(__name__)
