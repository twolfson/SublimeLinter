from base_linter import BaseLinter

CONFIG = {
    'language': 'reStructuredText',
}

class Linter(BaseLinter):
    def built_in_check(self, view, code, filename):
        errors = []

        print 'xxx'

        return errors

    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        print 'hai'
