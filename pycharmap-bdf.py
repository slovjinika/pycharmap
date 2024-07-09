import unicodedata
import sys
from bdflib import reader

def display_available_glyphs(font_path):
    # Load the BDF font
    with open(font_path, 'rb') as font_file:
        font = reader.read_bdf(font_file)

    print(f"Available glyphs in the font {font_path}:")
    print("=" * 40)

    # Iterate through all available glyphs
    glyph_count = 0
    for glyph in font.glyphs:
        if glyph.codepoint is not None:
            char = chr(glyph.codepoint)
            try:
                name = unicodedata.name(char)
            except ValueError:
                name = "Unknown"

            # Display glyph information
            print(f"U+{glyph.codepoint:04X} | {char} | {name}")
            glyph_count += 1

    print("=" * 40)
    print(f"Total available glyphs: {glyph_count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bdf_glyph_checker.py <bdf_font_file_path>")
        sys.exit(1)

    font_path = sys.argv[1]
    display_available_glyphs(font_path)
