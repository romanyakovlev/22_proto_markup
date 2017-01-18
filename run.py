import staticjinja


if __name__ == "__main__":
    site = staticjinja.make_site(staticpaths=["static/"], outpath="pages")
    site.render()
