try:
    import seaborn as sns

    def color(c):
        return sns.xkcd_rgb[c]

    def cubhelix(*args, **kwargs):
    	return sns.cubehelix_palette(*args, **kwargs)

except:
    import difflib

    def color(c):
        return difflib.get_close_matches(c, ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'])

    def cubhelix(*args, **kwargs):
        return 'magma'
