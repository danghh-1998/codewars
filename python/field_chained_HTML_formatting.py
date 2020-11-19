"""
We want to create an object with methods for various HTML elements: div, p, span and h1 for the sake of this Kata.

These methods will wrap the passed-in string in the tag associated with each.

format.div("foo")  # returns "<div>foo</div>"
format.p("bar")  # returns "<p>bar</p>"
format.span("fiz")  # returns "<span>fiz</span>"
format.h1("buz")  # returns "<h1>buz</h1>"

We also want to be able to add additional formatting by chaining our methods together.

format.div.h1("FooBar") # "<div><h1>FooBar</h1><div>"

format.div.p.span("FizBuz") # "<div><p><span>FizBuz</span></p></div>"

and so on, as deep as we care to use.
Multiple arguments should be concatenated and wrapped in the correct HTML formatting.

format.div.h1("Foo", "Bar") # "<div><h1>FooBar</h1></div>"

We should be able to store the created methods and reuse them.

wrap_in_div = format.div
wrap_in_div("Foo")    # "<div>Foo</div>"
wrap_in_div.p("Bar")  # "<div><p>Bar</p></div>"

wrap_in_div_h1 = format.div.h1
wrap_in_div_h1("Far")  # "<div><h1>Far</h1></div>"
wrap_in_div_h1.span("Bar")  # "<div><h1><span>Bar</span></h1></div>"
And finally, we should be able to nest calls.

format.div(
    format.h1("Title"),
    format.p(f"Paragraph with a {format.span('span')}.")
)
# returns "<div><h1>Title</h1><p>Paragraph with a <span>span</span>.</p></div>"

"""


class Format:
    tags = frozenset(('div', 'h1', 'p', 'span'))

    def __init__(self, chained_tags=None):
        self.chained_tags = chained_tags if chained_tags else []

    def __getattr__(self, attr):
        return Format(chained_tags=self.chained_tags.__add__([attr])) if not attr.startswith(
            '__') and attr in Format.tags else eval('self.attr')

    def __call__(self, *args):
        if args and type(args[0]) == str:
            result = ''.join(args)
            for tag in self.chained_tags[::-1]:
                result = f'<{tag}>{result}</{tag}>'
            return result
        else:
            result = self(''.join([item() for item in args]))
            self.chained_tags = []
            return result
