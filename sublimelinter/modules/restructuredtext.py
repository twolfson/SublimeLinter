import json

from base_linter import BaseLinter

CONFIG = {
    'language': 'reStructuredText',
    'executable': 'rst-lint',
    'lint_args': '{filename}',
}

class Linter(BaseLinter):
    def parse_errors(self, view, error_json, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        if error_json == 'File was clean.':
            return

        errors = json.loads(error_json)
        for error in errors:
            self.add_message(error['line'], lines, error['message'], errorMessages)
