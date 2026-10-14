"""Check the theme's host contract, reading contrast, and input boundary."""

import importlib.util
import json
from pathlib import Path
import re
import unittest

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('sync_theme', root / 'tools/sync-theme.py')
theme = importlib.util.module_from_spec(spec)
spec.loader.exec_module(theme)


def luminance(value):
    channels = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * weight for c, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(first, second):
    low, high = sorted((luminance(first), luminance(second)))
    return (high + 0.05) / (low + 0.05)


class ThemeContractTests(unittest.TestCase):
    def setUp(self):
        self.palette = json.loads((root / 'palette.json').read_text())

    def test_contribution_has_the_eight_supported_host_colors(self):
        colors = dict(re.findall(r'(\w+): "(#[A-Fa-f0-9]{6})"', theme.render(self.palette)))
        self.assertEqual(set(colors), {
            'background', 'foreground', 'raised', 'control', 'border',
            'accent', 'mutedForeground', 'ring',
        })
        self.assertEqual(colors['accent'], self.palette['accent.primary'])

    def test_text_and_placeholders_remain_readable_on_each_reading_surface(self):
        colors = dict(re.findall(r'(\w+): "(#[A-Fa-f0-9]{6})"', theme.render(self.palette)))
        for text in ('foreground', 'mutedForeground', 'ring'):
            for surface in ('background', 'raised', 'control'):
                with self.subTest(text=text, surface=surface):
                    self.assertGreaterEqual(contrast(colors[text], colors[surface]), 4.5)
        self.assertGreaterEqual(contrast(colors['foreground'], colors['border']), 4.5)

    def test_transparent_or_malformed_base_tokens_are_rejected(self):
        for value in ('#10141C00', 'rgb(16,20,28)', '#ZZZZZZ', None, 42):
            with self.subTest(value=value):
                self.palette['bg.0'] = value
                with self.assertRaisesRegex(ValueError, 'bg.0'):
                    theme.render(self.palette)

    def test_missing_required_tokens_are_rejected(self):
        del self.palette['text.primary']
        with self.assertRaises(KeyError):
            theme.render(self.palette)


if __name__ == '__main__':
    unittest.main()
