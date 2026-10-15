# test_processor_class.py
import unittest
from processor import END, ListReader, ListWriter, TextWriter
from processor_class import Pipeline, UppercasePipeline


class PipelineTests(unittest.TestCase):
    def test_same_inherited_method_and_bound_conversion(self):
        writer = ListWriter()
        job = UppercasePipeline(ListReader(['fern']), writer)
        self.assertIs(UppercasePipeline.run, Pipeline.run)
        self.assertIs(job.convert.__self__, job)
        self.assertIsNone(job.run())
        self.assertEqual(writer.items, ['FERN'])

    def test_two_writers_and_empty_text(self):
        for writer in (ListWriter(), TextWriter()):
            UppercasePipeline(ListReader(['a', '', 'b']), writer).run()
            actual = writer.items if isinstance(writer, ListWriter) else writer.text
            expected = ['A', '', 'B'] if isinstance(writer, ListWriter) else 'A\n\nB\n'
            self.assertEqual(actual, expected)

    def test_borrowed_state_and_exhausted_rerun(self):
        reader, writer = ListReader(['first', 'second']), ListWriter()
        job = UppercasePipeline(reader, writer)
        self.assertIs(job.reader, reader)
        self.assertIs(job.writer, writer)
        self.assertEqual(reader.read(), 'first')
        writer.write('already stored')
        job.run()
        job.run()
        self.assertEqual(writer.items, ['already stored', 'SECOND'])
        self.assertIs(reader.read(), END)

    def test_missing_conversion_fails_when_used(self):
        writer = ListWriter()
        self.assertIsNone(Pipeline(ListReader([]), writer).run())
        reader = ListReader(['consumed', 'later'])
        with self.assertRaisesRegex(NotImplementedError, 'a subclass must supply conversion'):
            Pipeline(reader, writer).run()
        self.assertEqual(writer.items, [])
        self.assertEqual(reader.read(), 'later')

    def test_failed_conversion_preserves_earlier_output(self):
        reader, writer = ListReader(['kept', 0, 'later']), ListWriter()
        job = UppercasePipeline(reader, writer)
        with self.assertRaisesRegex(TypeError, 'record must be a built-in string'):
            job.run()
        self.assertEqual(writer.items, ['KEPT'])
        self.assertEqual(reader.read(), 'later')
        self.assertIs(reader.read(), END)


if __name__ == '__main__':
    unittest.main(verbosity=2)
