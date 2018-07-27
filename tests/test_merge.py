import unittest
import os

import pdf_merger


class TestMerge(unittest.TestCase):
    def test_merge(self):
        output_filepath = 'tests/test_files/test_merge.pdf'
        filenames = ['page1.pdf', 'page2.pdf', 'page3-4.pdf']
        pdf_merger.merge(('tests/test_files/{}'.format(filename) for filename in filenames), output_filepath)

        if not os.path.isfile(output_filepath):
            self.fail('{} not created'.format(output_filepath))
        else:
            os.remove(output_filepath)
