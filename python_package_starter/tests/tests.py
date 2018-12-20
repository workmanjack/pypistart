# project files
from python_package_starter import PyPackageStarter, TEMPLATES_DIR


# python packages
import unittest
import os


class TestPyPackageStarter(unittest.TestCase):

    def setUp(self):
        self.package_name = 'beggars-canyon'
        self.location = 'tatooine'
        self.author_name = 'luke skywalker'
        self.author_email = 'luke.skywalker@rebelalliance.net'
        self.Starter = PyPackageStarter(
            package_name=self.package_name,
            location=self.location,
            author_name=self.author_name,
            author_email=self.author_email
        )
        return

    def tearDown(self):
        return

    def test___init__(self):
        self.assertEqual(self.package_name, self.Starter.package_name)
        self.assertEqual(self.location, self.Starter.location)
        self.assertEqual(self.author_name, self.Starter.author_name)
        self.assertEqual(self.author_email, self.Starter.author_email)

    def test__write_file(self):
        contents = 'testing123'
        dest = 'test__write_file.txt'
        self.Starter._write_file(contents, dest)
        with open(dest, 'r') as f:
            actual_contents = f.read()
        self.assertEqual(contents, actual_contents)
        os.remove(dest)

    def test__write_file_contents_is_none(self):
        contents = None
        dest = 'test__write_file_contents_is_none.txt'
        self.Starter._write_file(contents, dest)
        with open(dest, 'r') as f:
            actual_contents = f.read()
        self.assertEqual('', actual_contents)
        os.remove(dest)

    def test__write_file_dest_is_none(self):
        contents = 'testing321'
        dest = None
        self.assertRaises(Exception, self.Starter._write_file, contents, dest)

    def test__init_package_dir(self):
        parent_dir = 'test__init_package_dir'
        package_name = 'package_test__init_package_dir'
        self.Starter._init_package_dir(parent_dir, package_name)
        self.assertTrue(os.path.isdir(parent_dir))
        self.assertTrue(os.path.isfile(os.path.join(parent_dir, '__init__.py')))
        self.assertTrue(os.path.isfile(os.path.join(parent_dir, '{}.py'.format(package_name))))
        os.rmdir(package_name)

    def test__get_rendered_template(self):
        # find template directory
        template = os.path.join(TEMPLATES_DIR, 'license.txt')
        # now do the test
        expected_contents = None
        with open(template, 'r') as f:
            expected_contents = f.read()
        actual_contents = self.Starter._get_rendered_template(template)
        self.assertEquals(expected_contents, actual_contents)

    def test__readme(self):
        """
        Just testing to see if it returns content and that the args are plugged into
        the template somewhere
        """
        actual_contents = self.Starter._readme(template)
        self.assertTrue(len(actual_contents) > 0)
        self.assertTrue(self.package_name in actual_contents)

    def test__setup(self):
        """
        Just testing to see if it returns content and that the args are plugged into
        the template somewhere
        """
        actual_contents = self.Starter._setup()
        self.assertTrue(len(actual_contents) > 0)
        print(actual_contents)
        self.assertTrue(self.package_name in actual_contents)
        self.assertTrue(self.author_name in actual_contents)
        self.assertTrue(self.author_email in actual_contents)

    def test_start(self):
        """
        Other tests check to see if files have the expected content.
        This test will check and see if all expected files & dirs are
        created.
        """
        self.Starter.start()
        # meta
        self.assertTrue(os.path.isfile(os.path.join(self.location, 'LICENSE')))
        self.assertTrue(os.path.isfile(os.path.join(self.location, 'MANIFEST.in')))
        self.assertTrue(os.path.isfile(os.path.join(self.location, 'CHANGES.txt')))
        self.assertTrue(os.path.isfile(os.path.join(self.location, '.gitignore')))
        # package
        package_dir = os.path.join(self.location, self.package_name)
        self.assertTrue(os.path.isdir(package_dir))
        self.assertTrue(os.path.isfile(os.path.join(package_dir, '__init__.py')))
        self.assertTrue(os.path.isfile(os.path.join(package_dir, '{}.py'.format(self.package_name))))
        # test dir
        test_dir = os.path.join(package_dir, 'tests')
        self.assertTrue(os.path.isdir(test_dir))
        self.assertTrue(os.path.isfile(os.path.join(test_dir, '__init__.py')))
        self.assertTrue(os.path.isfile(os.path.join(test_dir, 'tests.py')))
        os.rmdir(self.package_name)
