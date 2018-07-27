import unittest
import os

import pdfmerger


class TestMerge(unittest.TestCase):
    def test_merge__str(self):
        output_filepath = 'tests/test_files/test_merge__str.pdf'
        input_filepaths = [os.path.join('tests/test_files/', filename) for filename in ['page1.pdf', 'page2.pdf', 'page3-4.pdf']]
        pdfmerger.merge(input_filepaths, output_filepath)

        if not os.path.isfile(output_filepath):
            self.fail('{} not created'.format(output_filepath))
        else:
            os.remove(output_filepath)

    def test_merge__file_obj(self):
        output_filepath = 'tests/test_files/test_merge__file_obj.pdf'
        input_filepaths = [os.path.join('tests/test_files/', filename) for filename in ['page1.pdf', 'page2.pdf', 'page3-4.pdf']]

        input_file_objs = []
        for filepath in input_filepaths:
            file_obj = open(filepath, 'rb')
            input_file_objs.append(file_obj)

            self.assertEqual(file_obj.tell(), 0)

        output_file_obj = open(output_filepath, 'wb')

        self.assertEqual(output_file_obj.tell(), 0)

        try:
            pdfmerger.merge(input_file_objs, output_file_obj)

            for file_obj in input_file_objs:
                self.assertNotEqual(file_obj.tell(), 0)

            self.assertNotEqual(output_file_obj.tell(), 0)
        finally:
            for file_obj in input_file_objs:
                file_obj.close()

                with self.assertRaises(ValueError):
                    file_obj.tell()

            output_file_obj.close()

            with self.assertRaises(ValueError):
                output_file_obj.tell()

        if not os.path.isfile(output_filepath):
            self.fail('{} not created'.format(output_filepath))
        else:
            os.remove(output_filepath)
