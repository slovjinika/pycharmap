import unicodedata
from fontTools.ttLib import TTFont
import sys

def display_available_glyphs(font_path):
    # Load the font
    font = TTFont(font_path)
    
    # Get the set of code points available in the font
    cmap = font.getBestCmap()
    
    print(f"Available glyphs in the font {font_path}:")
    print("=" * 40)
    
    # Iterate through all available code points
    for code_point in sorted(cmap.keys()):
        char = chr(code_point)
        try:
            name = unicodedata.name(char)
        except ValueError:
            name = "Unknown"
        
        # Display glyph information
        print(f"U+{code_point:04X} | {char} | {name}")
    
    print("=" * 40)
    print(f"Total available glyphs: {len(cmap)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python unicode_glyph_checker.py <font_file_path>")
        sys.exit(1)
    
    font_path = sys.argv[1]
    display_available_glyphs(font_path)
