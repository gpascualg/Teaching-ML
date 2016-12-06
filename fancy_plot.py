try:
    import seaborn as sns

    def color(c):
        return sns.xkcd_rgb[c]

    def cubhelix(*args, **kwargs):
        return sns.cubehelix_palette(*args, **kwargs)
    
    def diverging(high, low, *args, **kwargs):
        return sns.diverging_palette(high, low, *args, **kwargs)

except:
    import difflib
    from matplotlib import cm
    import matplotlib.colors as mcolors

    def color(c):
        return difflib.get_close_matches(c, ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white'], n=1, cutoff=0)[0]

    def cubhelix(*args, **kwargs):
        try:
            return cm.viridis
        except:
            return 'hot_r'

    def diverging(high=(0.565, 0.392, 0.173), low=(0.094, 0.310, 0.635), *args, **kwargs):
        '''
        low and high are colors that will be used for the two
        ends of the spectrum. they can be either color strings
        or rgb color tuples
        '''
        
        def make_colormap(seq):
            """Return a LinearSegmentedColormap
            seq: a sequence of floats and RGB-tuples. The floats should be increasing
            and in the interval (0,1).
            """
            seq = [(None,) * 3, 0.0] + list(seq) + [1.0, (None,) * 3]
            cdict = {'red': [], 'green': [], 'blue': []}
            for i, item in enumerate(seq):
                if isinstance(item, float):
                    r1, g1, b1 = seq[i - 1]
                    r2, g2, b2 = seq[i + 1]
                    cdict['red'].append([item, r1, r2])
                    cdict['green'].append([item, g1, g2])
                    cdict['blue'].append([item, b1, b2])
            
            return mcolors.LinearSegmentedColormap('CustomMap', cdict)
        
        s = {10: 'red', 133: 'green'}
        c = mcolors.ColorConverter().to_rgb
        if type(low) == int: low = s[low]
        if type(high) == int: high = s[high]
        if isinstance(low, basestring): low = c(low)
        if isinstance(high, basestring): high = c(high)
        return make_colormap([high, c('white'), 0.5, c('white'), low])