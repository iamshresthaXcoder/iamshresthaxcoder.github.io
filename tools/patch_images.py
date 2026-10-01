import os
import sys

P = "index.html"
CSS = (
    ".shot-h{background-image:var(--img-i)!important;"
    "background-size:200% auto!important;background-position:right center!important}"
    ".shot-i{background-size:200% auto!important;background-position:left center!important}"
)


def main():
    if not os.path.exists(P):
        print("index.html not found")
        return 1
    s = open(P, encoding="utf-8").read()
    if "background-position:right center!important" in s:
        print("already patched - nothing to do")
        return 0
    i = s.find("</style>")
    if i < 0:
        print("no </style> found")
        return 1
    s = s[:i] + CSS + s[i:]
    open(P, "w", encoding="utf-8").write(s)
    print("patched index.html (+%d chars)" % len(CSS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
