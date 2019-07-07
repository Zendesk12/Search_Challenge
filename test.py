# import statements
import unittest
import json

import database
import search_engine



class TestSystemFunctions(unittest.TestCase):

	# Test Parser Functions

	def test_createConnection(self):
		result = database.create_connection("../Search_challenge/sqliteTest.db")
		self.assertIsNotNone(result)


	def test_extractColumnsName(self):
		json_test = open('../Search_challenge/Json_Data/test.json', encoding='utf-8-sig')
		json_data_test = json.loads(json_test.read())
		result = database.extract_columns_name(json_data_test)
		json_test.close()
		self.assertEqual('A',result[0])
		self.assertEqual('B',result[1])
		self.assertEqual('C',result[2])
		self.assertEqual('D',result[3])


	def test_extractDataValues(self):
		json_test = open('../Search_challenge/Json_Data/test.json', encoding='utf-8-sig')
		json_data_test = json.loads(json_test.read())
		columns = database.extract_columns_name(json_data_test)
		result = database.extract_data_values(json_data_test,columns)
		json_test.close()
		self.assertEqual('aaa',result[0][0])
		self.assertEqual('bbb',result[0][1])
		self.assertEqual('ccc',result[0][2])
		self.assertEqual('ddd',result[0][3])


	def test_createDataBase_one(self):
		database.create_data_base("../Search_challenge/sqliteTest.db", ["test.json"])
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
		result = cursor.fetchall()[0][0]
		self.assertIsNotNone(conn)
		self.assertEqual(result, 'test')


	def test_createDataBase_many(self):
		database.create_data_base("../Search_challenge/sqliteTest.db", ["test.json", "test_2.json"])
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
		result = cursor.fetchall()
		self.assertIsNotNone(conn)
		self.assertEqual(result[0][0], 'test')
		self.assertEqual(result[1][0], 'test_2')


	def test_searchByUser_user_id(self):
		database.create_data_base("../Search_challenge/sqliteTest.db", ["users.json", "organizations.json", "tickets.json"])
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, '_id', '75')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '75')
		self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
		self.assertEqual(result_1[0]['organization_id'], '119')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')
		self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
		self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')


	def test_searchByUser_url(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'url', 'http://initech.zendesk.com/api/v2/users/75.json')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '75')
		self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
		self.assertEqual(result_1[0]['organization_id'], '119')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')
		self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
		self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')


	def test_searchByUser_external_id(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'external_id', '0db0c1da-8901-4dc3-a469-fe4b500d0fca')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '75')
		self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
		self.assertEqual(result_1[0]['organization_id'], '119')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')
		self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
		self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')


	def test_searchByUser_name(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'name', 'Catalina Simpson')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '75')
		self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
		self.assertEqual(result_1[0]['organization_id'], '119')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')
		self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
		self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')


	def test_searchByUser_alias(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'alias', 'Miss Rosanna')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '75')
		self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
		self.assertEqual(result_1[0]['organization_id'], '119')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')
		self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
		self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')


	def test_searchByUser_created_at(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'created_at', '2016-06-07T09:18:00 -10:00')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '75')
		self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
		self.assertEqual(result_1[0]['organization_id'], '119')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')
		self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
		self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')

	def test_searchByUser_active(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'active', False)
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '3')
		self.assertEqual(result_1[0]['name'], 'Ingrid Wagner')
		self.assertEqual(result_1[0]['organization_name'], 'Xylar')
		self.assertEqual(result_1[-1]['_id'], '75')
		self.assertEqual(result_1[-1]['name'], 'Catalina Simpson')
		self.assertEqual(result_1[-1]['organization_name'], 'Multron')

	def test_searchByUser_verified(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'verified', True)
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '1')
		self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')
		self.assertEqual(result_1[-1]['_id'], '75')
		self.assertEqual(result_1[-1]['name'], 'Catalina Simpson')
		self.assertEqual(result_1[-1]['organization_name'], 'Multron')

	def test_searchByUser_shared(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'shared', False)
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '1')
		self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')
		self.assertEqual(result_1[-1]['_id'], '74')
		self.assertEqual(result_1[-1]['name'], 'Melissa Bishop')
		self.assertEqual(result_1[-1]['organization_name'], 'Isotronic')

	def test_searchByUser_locale(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'locale', 'en-AU')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '1')
		self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')
		self.assertEqual(result_1[-1]['_id'], '74')
		self.assertEqual(result_1[-1]['name'], 'Melissa Bishop')
		self.assertEqual(result_1[-1]['organization_name'], 'Isotronic')

	def test_searchByUser_timezone(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'timezone', 'Sri Lanka')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '1')
		self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')

	def test_searchByUser_last_login_at(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'last_login_at', '2013-08-04T01:03:27 -10:00')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '1')
		self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')

	def test_searchByUser_email(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'email', 'jonibarlow@flotonic.com')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '2')
		self.assertEqual(result_1[0]['name'], 'Cross Barlow')
		self.assertEqual(result_1[0]['organization_name'], 'Qualitern')

	def test_searchByUser_phone(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'phone', '9575-552-585')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '2')
		self.assertEqual(result_1[0]['name'], 'Cross Barlow')
		self.assertEqual(result_1[0]['organization_name'], 'Qualitern')

	def test_searchByUser_signature(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'signature', 'Don\'t Worry Be Happy!')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '1')
		self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')

	def test_searchByUser_organization_id(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'organization_id', '106')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '2')
		self.assertEqual(result_1[0]['name'], 'Cross Barlow')
		self.assertEqual(result_1[0]['organization_name'], 'Qualitern')

	def test_searchByUser_suspended(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'suspended', False)
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '2')
		self.assertEqual(result_1[0]['name'], 'Cross Barlow')
		self.assertEqual(result_1[0]['organization_name'], 'Qualitern')

	def test_searchByUser_role(self):
		conn = database.create_connection("../Search_challenge/sqliteTest.db")
		result_1, result_2 = search_engine.search_by_user(conn, 'role', 'admin')
		self.assertIsNotNone(conn)
		self.assertEqual(result_1[0]['_id'], '1')
		self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
		self.assertEqual(result_1[0]['organization_name'], 'Multron')


# Run the tests

if __name__ == '__main__':
	unittest.main()