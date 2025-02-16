"""
A list of the languages that Pycco supports, mapping the file extension to
the name of the Pygments lexer and the symbol that indicates a comment. To
add another language to Pycco's repertoire, add it here.

The problem with this is that the one language that we supposedly specialise
for (namely python) can't be properly specified here. For a start, triple-quote
blocks can also use single quotes. Additionally, they can also be used in
assignments and on single lines.

e.g.

    s = '''one one line'''

    s2 = '''
    across
    several
    lines'''

    s3 = 'x' + '''some text''' + 'y'

...and so on.

None of these are documentation (comments) nor docstrings

"""

__all__ = ("supported_languages",)

HASH = "#"
SLASH_STAR = "/*"
STAR_SLASH = "*/"
SLASH_SLASH = "//"
DASH_DASH = "--"
TRIPLE_QUOTE = '"""'


def lang(name, comment_symbol, multistart=None, multiend=None) -> dict:
    """
    Generate a language entry dictionary, given a name and comment symbol and
    optional start/end strings for multiline comments.
    """
    result = {"name": name, "comment_symbol": comment_symbol}
    if multistart is not None and multiend is not None:
        result.update(multistart=multistart, multiend=multiend)
    return result


c_lang = lang("c", SLASH_SLASH, SLASH_STAR, STAR_SLASH)

supported_languages = {
    ".coffee": lang("coffee-script", HASH, "###", "###"),  # <--- We might need to process .coffee files differently.

    ".pl": lang("perl", HASH),

    ".sql": lang("sql", DASH_DASH, SLASH_STAR, STAR_SLASH),

    ".sh": lang("bash", HASH),

    ".c": c_lang,

    ".h": c_lang,

    ".cl": c_lang,

    ".css": lang("css", SLASH_SLASH, SLASH_STAR, STAR_SLASH),  # Note, strictly, css has no single-line comment type

    ".cpp": lang("cpp", SLASH_SLASH, SLASH_STAR, STAR_SLASH),  # This was incorrect, it should include SLASH_STAR, STAR_SLASH

    ".js": lang("javascript", SLASH_SLASH, SLASH_STAR, STAR_SLASH),

    ".rb": lang("ruby", HASH, "=begin", "=end"),

    ".py": lang("python", HASH, TRIPLE_QUOTE, TRIPLE_QUOTE),

    ".pyx": lang("cython", HASH, TRIPLE_QUOTE, TRIPLE_QUOTE),  # <-- Cython is not passed to dycco)

    ".scm": lang("scheme", ";;", "#|", "|#"),

    ".lua": lang("lua", DASH_DASH, "--[[", "--]]"),

    ".erl": lang("erlang", "%%"),

    ".tcl": lang("tcl", HASH),

    ".hs": lang("haskell", DASH_DASH, "{-", "-}"),

    ".r": lang("r", HASH),
    ".R": lang("r", HASH),

    ".jl": lang("julia", HASH, "#=", "=#"),

    ".m": lang("matlab", "%", "%{", "%}"),

    ".do": lang("stata", SLASH_SLASH, SLASH_STAR, STAR_SLASH)

}
