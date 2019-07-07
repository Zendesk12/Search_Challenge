# import statements
import unittest
import database
import json


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


# Run the tests

if __name__ == '__main__':
	unittest.main()