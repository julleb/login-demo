import psycopg2
import sys
import psycopg2.extras
import random
from psycopg2 import IntegrityError
import hashlib

#TODO: Prepared statements to db.
class UserService:

	def __init__(self):
		self.id = "1234";
		self.table_name = "USERS";
		self.init_db();

	def create_user(self, username, password):
		query = "INSERT INTO " + self.table_name + " VALUES(%s, %s, %s)";
		salt = self.generate_salt();
		password_and_salt = password + salt;
		hashed_password = self.hash(password_and_salt); #password_and_salt should be here..
		try:
			self.getQuerier().execute(query, [username, hashed_password, salt]);
			self.commit();
		except IntegrityError as e:
			self.rollback();
			raise Exception("Username already exists");

	def generate_salt(self):
		#TODO better salt-generator
		salt = random.randint(0,1337);
		return str(salt);

	def hash(self, string_to_hash):
		hashed_string = hashlib.sha256(string_to_hash);
		return hashed_string.hexdigest();

	def get_user(self, username, password): 
		query = "SELECT * FROM "+ self.table_name + " WHERE username=%s";	
		self.getQuerier().execute(query, [username])
		result = self.getQuerier().fetchall();		
		salt = "";
		for r in result:
			salt = r["salt"];
			break;
		password_and_salt = password + salt;
		hashed_password = self.hash(password_and_salt);
		query = "SELECT * FROM "+ self.table_name + " WHERE username=%s AND password=%s";
		self.getQuerier().execute(query, [username, hashed_password])
		result = self.getQuerier().fetchall();
		print result
		for r in result:
			return r["username"]; 

		raise Exception("Username or password is not correct");

	

	def init_db(self):
		try:
                        self.connection = psycopg2.connect(host='localhost', database='logindemo', user='postgres', password='lol12345')
                        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor) #self.connection.cursor()
		except psycopg2.DatabaseError as e:
			print ('Error %s' % e    )

	def getQuerier(self):
		return self.cursor;
	def commit(self):
		self.connection.commit();
	def rollback(self):
		self.connection.rollback();
