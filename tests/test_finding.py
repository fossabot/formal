"""
Changes notice
==============

This file has been changed by the Hackerfleet Community and this notice has
been added in accordance to the Apache License 2.0

"""

import unittest

import warmongo


class TestFinding(unittest.TestCase):

    def setUp(self):
        self.schema = {
            'name': 'Country',
            "id": "#Country",
            'properties': {
                'name': {'type': 'string'},
                'abbreviation': {'type': 'string'},
                'languages': {
                    'type': 'array',
                    'items': {
                        'type': 'string'
                    }
                }
            },
            'additionalProperties': False,
        }

        # Connect to warmongo_test - hopefully it doesn't exist
        warmongo.connect("warmongo_test")
        self.Country = warmongo.model_factory(self.schema)

        # Drop all the data in it
        self.Country.collection().remove({})

        # Create some defaults
        sweden = self.Country({
            "name": "Sweden",
            "abbreviation": "SE",
            "languages": ["swedish"]
        })
        sweden.save()
        usa = self.Country({
            "name": "United States of America",
            "abbreviation": "US",
            "languages": ["english"]
        })
        usa.save()

    def testFindOne(self):
        """ Test grabbing a single value the Mongo way """

        usa = self.Country.find_one({"abbreviation": "US"})

        self.assertIsNotNone(usa)
        self.assertEqual("United States of America", usa.name)

    def testFind(self):
        """ Just grab a bunch of stuff """

        countries = self.Country.find()

        # Since find() returns a generator, need to convert to list
        countries = [c for c in countries]

        self.assertEqual(2, len(countries))

    def testCount(self):
        """ See if everything is there """
        self.assertEqual(2, self.Country.count())
        self.assertEqual(1, self.Country.count({"abbreviation": "SE"}))
        self.assertEqual(0, self.Country.count({"abbreviation": "CA"}))

    def testFindAll(self):
        """ Test fetching everything the mongo way """

        countries = self.Country.find({"abbreviation": "SE"})

        # Since find() returns a generator, need to convert to list
        countries = [c for c in countries]

        self.assertEqual(1, len(countries))
        self.assertEqual("Sweden", countries[0].name)
