# test.py

'''This test class has been implemented using unittest library.'''

# Import statements
import unittest
import json

import database
import search_engine


class TestSystemFunctions(unittest.TestCase):
    # Test Data Base Functions

    def test_createConnection(self):
        result = database.create_connection()
        self.assertIsNotNone(result)
        result.close()

    def test_extractColumnsName(self):
        json_test = open('../Search_challenge/Json_Data/test.json', encoding='utf-8-sig')
        json_data_test = json.loads(json_test.read())
        result = database.extract_columns_name(json_data_test)
        json_test.close()
        self.assertEqual('A', result[0])
        self.assertEqual('B', result[1])
        self.assertEqual('C', result[2])
        self.assertEqual('D', result[3])

    def test_extractDataValues(self):
        json_test = open('../Search_challenge/Json_Data/test.json', encoding='utf-8-sig')
        json_data_test = json.loads(json_test.read())
        columns = database.extract_columns_name(json_data_test)
        result = database.extract_data_values(json_data_test, columns)
        json_test.close()
        self.assertEqual('aaa', result[0][0])
        self.assertEqual('bbb', result[0][1])
        self.assertEqual('ccc', result[0][2])
        self.assertEqual('ddd', result[0][3])

    def test_createDataBase_one(self):
        conn = database.create_data_base(["test.json"])
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = cursor.fetchall()[0][0]
        self.assertIsNotNone(conn)
        self.assertEqual(result, 'test')
        conn.close()

    def test_createDataBase_many(self):
        conn = database.create_data_base(["test.json", "test_2.json"])
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
        result = cursor.fetchall()
        self.assertIsNotNone(conn)
        self.assertEqual(result[0][0], 'test')
        self.assertEqual(result[1][0], 'test_2')
        conn.close()

    # Test Search Engine Functions
    
    # Test Search_by_user function
    
    def test_searchByUser_user_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, '_id', '75')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '75')
        self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
        self.assertEqual(result_1[0]['organization_id'], '119')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
        self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')
        conn.close()

    def test_searchByUser_url(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'url',
                                                          'http://initech.zendesk.com/api/v2/users/75.json')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '75')
        self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
        self.assertEqual(result_1[0]['organization_id'], '119')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
        self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')
        conn.close()

    def test_searchByUser_external_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'external_id', '0db0c1da-8901-4dc3-a469-fe4b500d0fca')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '75')
        self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
        self.assertEqual(result_1[0]['organization_id'], '119')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
        self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')
        conn.close()

    def test_searchByUser_name(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'name', 'Catalina Simpson')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '75')
        self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
        self.assertEqual(result_1[0]['organization_id'], '119')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
        self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')
        conn.close()

    def test_searchByUser_alias(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'alias', 'Miss Rosanna')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '75')
        self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
        self.assertEqual(result_1[0]['organization_id'], '119')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
        self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')
        conn.close()

    def test_searchByUser_created_at(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'created_at', '2016-06-07T09:18:00 -10:00')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '75')
        self.assertEqual(result_1[0]['name'], 'Catalina Simpson')
        self.assertEqual(result_1[0]['organization_id'], '119')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        self.assertEqual(tuple(result_2[0])[1], 'A Problem in Switzerland')
        self.assertEqual(tuple(result_2[1])[1], 'A Problem in Svalbard and Jan Mayen Islands')
        conn.close()

    def test_searchByUser_active(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'active', False)
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '3')
        self.assertEqual(result_1[0]['name'], 'Ingrid Wagner')
        self.assertEqual(result_1[0]['organization_name'], 'Xylar')
        self.assertEqual(result_1[-1]['_id'], '75')
        self.assertEqual(result_1[-1]['name'], 'Catalina Simpson')
        self.assertEqual(result_1[-1]['organization_name'], 'Multron')
        conn.close()

    def test_searchByUser_verified(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'verified', True)
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '1')
        self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        self.assertEqual(result_1[-1]['_id'], '75')
        self.assertEqual(result_1[-1]['name'], 'Catalina Simpson')
        self.assertEqual(result_1[-1]['organization_name'], 'Multron')
        conn.close()

    def test_searchByUser_shared(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'shared', False)
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '1')
        self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        self.assertEqual(result_1[-1]['_id'], '74')
        self.assertEqual(result_1[-1]['name'], 'Melissa Bishop')
        self.assertEqual(result_1[-1]['organization_name'], 'Isotronic')
        conn.close()

    def test_searchByUser_locale(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'locale', 'en-AU')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '1')
        self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        self.assertEqual(result_1[-1]['_id'], '74')
        self.assertEqual(result_1[-1]['name'], 'Melissa Bishop')
        self.assertEqual(result_1[-1]['organization_name'], 'Isotronic')
        conn.close()

    def test_searchByUser_timezone(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'timezone', 'Sri Lanka')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '1')
        self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        conn.close()

    def test_searchByUser_last_login_at(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'last_login_at', '2013-08-04T01:03:27 -10:00')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '1')
        self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        conn.close()

    def test_searchByUser_email(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'email', 'jonibarlow@flotonic.com')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '2')
        self.assertEqual(result_1[0]['name'], 'Cross Barlow')
        self.assertEqual(result_1[0]['organization_name'], 'Qualitern')
        conn.close()

    def test_searchByUser_phone(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'phone', '9575-552-585')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '2')
        self.assertEqual(result_1[0]['name'], 'Cross Barlow')
        self.assertEqual(result_1[0]['organization_name'], 'Qualitern')
        conn.close()

    def test_searchByUser_signature(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'signature', 'Don\'t Worry Be Happy!')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '1')
        self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        conn.close()

    def test_searchByUser_organization_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'organization_id', '106')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '2')
        self.assertEqual(result_1[0]['name'], 'Cross Barlow')
        self.assertEqual(result_1[0]['organization_name'], 'Qualitern')
        conn.close()

    def test_searchByUser_suspended(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'suspended', False)
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '2')
        self.assertEqual(result_1[0]['name'], 'Cross Barlow')
        self.assertEqual(result_1[0]['organization_name'], 'Qualitern')
        conn.close()

    def test_searchByUser_tags(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'tags', ["Springville", "Sutton", "Hartsville/Hartley",
                                                                         "Diaperville"])
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '1')
        self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        conn.close()

    def test_searchByUser_role(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'role', 'admin')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '1')
        self.assertEqual(result_1[0]['name'], 'Francisca Rasmussen')
        self.assertEqual(result_1[0]['organization_name'], 'Multron')
        conn.close()

     def test_searchByuser_wrong_column(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2 = search_engine.search_by_user(conn, 'wrong column','34')
        self.assertIsNotNone(conn)
        self.assertEqual(len(result_1),0)
        self.assertEqual(len(result_2),0)
        conn.close()

    # Test Search_by_organization function
    
    def test_searchByOrganization_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2, result_3 = search_engine.search_by_organization(conn, '_id', '106')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '106')
        self.assertEqual(result_1[0]['name'], 'Qualitern')
        self.assertEqual(result_1[0]['external_id'], '2355f080-b37c-44f3-977e-53c341fde146')
        self.assertEqual(result_2[0][1], 'A Nuisance in Greece')
        self.assertEqual(result_3[0][1], 'Cross Barlow')
        conn.close()

    def test_searchByOrganization_url(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2, result_3 = search_engine.search_by_organization(conn, 'url',
                                                                            'http://initech.zendesk.com/api/v2'
                                                                            '/organizations/106.json') 
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '106')
        self.assertEqual(result_1[0]['name'], 'Qualitern')
        self.assertEqual(result_1[0]['external_id'], '2355f080-b37c-44f3-977e-53c341fde146')
        self.assertEqual(result_2[0][1], 'A Nuisance in Greece')
        self.assertEqual(result_3[0][1], 'Cross Barlow')
        conn.close()

    def test_searchByOrganization_external_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2, result_3 = search_engine.search_by_organization(conn, 'external_id',
                                                                            '2355f080-b37c-44f3-977e-53c341fde146')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '106')
        self.assertEqual(result_1[0]['name'], 'Qualitern')
        self.assertEqual(result_1[0]['external_id'], '2355f080-b37c-44f3-977e-53c341fde146')
        self.assertEqual(result_2[0][1], 'A Nuisance in Greece')
        self.assertEqual(result_3[0][1], 'Cross Barlow')
        conn.close()

    def test_searchByOrganization_name(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2, result_3 = search_engine.search_by_organization(conn, 'name', 'Qualitern')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '106')
        self.assertEqual(result_1[0]['name'], 'Qualitern')
        self.assertEqual(result_1[0]['external_id'], '2355f080-b37c-44f3-977e-53c341fde146')
        self.assertEqual(result_2[0][1], 'A Nuisance in Greece')
        self.assertEqual(result_3[0][1], 'Cross Barlow')
        conn.close()

    def test_searchByOrganization_created_at(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2, result_3 = search_engine.search_by_organization(conn, 'created_at',
                                                                            '2016-07-23T09:48:02 -10:00')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '106')
        self.assertEqual(result_1[0]['name'], 'Qualitern')
        self.assertEqual(result_1[0]['external_id'], '2355f080-b37c-44f3-977e-53c341fde146')
        self.assertEqual(result_2[0][1], 'A Nuisance in Greece')
        self.assertEqual(result_3[0][1], 'Cross Barlow')
        conn.close()

    def test_searchByOrganization_details(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2, result_3 = search_engine.search_by_organization(conn, 'details', 'Artisân')
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '106')
        self.assertEqual(result_1[0]['name'], 'Qualitern')
        self.assertEqual(result_1[0]['external_id'], '2355f080-b37c-44f3-977e-53c341fde146')
        self.assertEqual(result_1[-1]['_id'], '114')
        self.assertEqual(result_1[-1]['name'], 'Isotronic')
        self.assertEqual(result_1[-1]['external_id'], '49c97d6a-f1ec-422e-aabe-8a429e81e656')
        conn.close()

    def test_searchByOrganization_shared_tickets(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2, result_3 = search_engine.search_by_organization(conn, 'shared_tickets', False)
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '101')
        self.assertEqual(result_1[0]['name'], 'Enthaze')
        self.assertEqual(result_1[0]['external_id'], '9270ed79-35eb-4a38-a46f-35725197ea8d')
        self.assertEqual(result_1[-1]['_id'], '125')
        self.assertEqual(result_1[-1]['name'], 'Strezzö')
        self.assertEqual(result_1[-1]['external_id'], '42a1a845-70cf-40ed-a762-acb27fd606cc')
        conn.close()

    def test_searchByOrganization_tags(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2, result_3 = search_engine.search_by_organization(conn, 'tags',
                                                                            ["Nolan", "Rivas", "Morse", "Conway"])
        self.assertIsNotNone(conn)
        self.assertEqual(result_1[0]['_id'], '106')
        self.assertEqual(result_1[0]['name'], 'Qualitern')
        self.assertEqual(result_1[0]['external_id'], '2355f080-b37c-44f3-977e-53c341fde146')
        self.assertEqual(result_2[0][1], 'A Nuisance in Greece')
        self.assertEqual(result_3[0][1], 'Cross Barlow')
        conn.close()

    def test_searchByorganization_wrong_column(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result_1, result_2, result_3 = search_engine.search_by_organization(conn, 'wrong column','34')
        self.assertIsNotNone(conn)
        self.assertEqual(len(result_1),0)
        self.assertEqual(len(result_2),0)
        self.assertEqual(len(result_3),0)
        conn.close()

    # Test Search_by_ticket function
    
    def test_searchByTickets_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, '_id', '1a227508-9f39-427c-8f57-1b72f3fab87c')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '1a227508-9f39-427c-8f57-1b72f3fab87c')
        self.assertEqual(result[0]['subject'], 'A Catastrophe in Micronesia')
        self.assertEqual(result[0]['user_name'], 'Prince Hinton')
        self.assertEqual(result[0]['organization_name'], 'Quilk')
        conn.close()

    def test_searchByTickets_url(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'url',
                                                 'http://initech.zendesk.com/api/v2/tickets/1a227508-9f39-427c-8f57'
                                                 '-1b72f3fab87c.json') 
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '1a227508-9f39-427c-8f57-1b72f3fab87c')
        self.assertEqual(result[0]['subject'], 'A Catastrophe in Micronesia')
        self.assertEqual(result[0]['user_name'], 'Prince Hinton')
        self.assertEqual(result[0]['organization_name'], 'Quilk')
        conn.close()

    def test_searchByTickets_external_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'external_id', '3e5ca820-cd1f-4a02-a18f-11b18e7bb49a')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '1a227508-9f39-427c-8f57-1b72f3fab87c')
        self.assertEqual(result[0]['subject'], 'A Catastrophe in Micronesia')
        self.assertEqual(result[0]['user_name'], 'Prince Hinton')
        self.assertEqual(result[0]['organization_name'], 'Quilk')
        conn.close()

    def test_searchByTickets_created_at(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'created_at', '2016-04-14T08:32:31 -10:00')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '1a227508-9f39-427c-8f57-1b72f3fab87c')
        self.assertEqual(result[0]['subject'], 'A Catastrophe in Micronesia')
        self.assertEqual(result[0]['user_name'], 'Prince Hinton')
        self.assertEqual(result[0]['organization_name'], 'Quilk')
        conn.close()

    def test_searchByTickets_type(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'type', 'incident')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        self.assertEqual(result[-1]['_id'], '50f3fdbd-f8a6-481d-9bf7-572972856628')
        self.assertEqual(result[-1]['user_name'], 'Geneva Poole')
        self.assertEqual(result[-1]['organization_name'], 'Strezzö')
        conn.close()

    def test_searchByTickets_subject(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'subject', 'A Catastrophe in Micronesia')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '1a227508-9f39-427c-8f57-1b72f3fab87c')
        self.assertEqual(result[0]['subject'], 'A Catastrophe in Micronesia')
        self.assertEqual(result[0]['user_name'], 'Prince Hinton')
        self.assertEqual(result[0]['organization_name'], 'Quilk')
        conn.close()

    def test_searchByTickets_description(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'description',
                                                 'Nostrud ad sit velit cupidatat laboris ipsum nisi amet laboris ex '
                                                 'exercitation amet et proident. Ipsum fugiat aute dolore tempor '
                                                 'nostrud velit ipsum.') 
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        conn.close()

    def test_searchByTickets_priority(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'priority', 'high')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        self.assertEqual(result[-1]['_id'], '50dfc8bc-31de-411e-92bf-a6d6b9dfa490')
        self.assertEqual(result[-1]['user_name'], 'Charlene Coleman')
        self.assertEqual(result[-1]['organization_name'], 'Plasmos')
        conn.close()

    def test_searchByTickets_status(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'status', 'pending')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        self.assertEqual(result[-1]['_id'], '50f3fdbd-f8a6-481d-9bf7-572972856628')
        self.assertEqual(result[-1]['user_name'], 'Geneva Poole')
        self.assertEqual(result[-1]['organization_name'], 'Strezzö')
        conn.close()

    def test_searchByTickets_submitter_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'submitter_id', '38')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        conn.close()

    def test_searchByTickets_assignee_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'assignee_id', '24')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        conn.close()

    def test_searchByTickets_organization_id(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'organization_id', '116')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        conn.close()

    def test_searchByTickets_tags(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'tags',
                                                 ["Ohio", "Pennsylvania", "American Samoa", "Northern Mariana Islands"])
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        conn.close()

    def test_searchByTickets_has_incidents(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'has_incidents', False)
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        self.assertEqual(result[-1]['_id'], '50f3fdbd-f8a6-481d-9bf7-572972856628')
        self.assertEqual(result[-1]['user_name'], 'Geneva Poole')
        self.assertEqual(result[-1]['organization_name'], 'Strezzö')
        conn.close()

    def test_searchByTickets_due_at(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'due_at', '2016-07-31T02:37:50 -10:00')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        conn.close()

    def test_searchByTickets_via(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'via', 'web')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '436bf9b0-1147-4c0a-8439-6f79833bff5b')
        self.assertEqual(result[0]['user_name'], 'Elma Castro')
        self.assertEqual(result[0]['organization_name'], 'Zentry')
        self.assertEqual(result[-1]['_id'], '59d803f6-a9cd-448c-a6bd-91ce9f044305')
        self.assertEqual(result[-1]['user_name'], 'Key Mendez')
        self.assertEqual(result[-1]['organization_name'], 'Comtext')
        conn.close()

    def test_searchByTickets_empty_description(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'description')
        self.assertIsNotNone(conn)
        self.assertEqual(result[0]['_id'], '4cce7415-ef12-42b6-b7b5-fb00e24f9cc1')
        self.assertEqual(result[0]['user_name'], 'Josefa Mcfadden')
        self.assertEqual(result[0]['organization_name'], 'Xylar')
        conn.close()

    def test_searchBytickets_wrong_column(self):
        conn = database.create_data_base(["users.json", "organizations.json", "tickets.json"])
        result = search_engine.search_by_tickets(conn, 'wrong column','34')
        self.assertIsNotNone(conn)
        self.assertEqual(len(result),0)
        conn.close()



# Run the tests

if __name__ == '__main__':
    unittest.main()
