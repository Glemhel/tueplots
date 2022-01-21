
<p align="center">
<img src="./docs/source/img/logo.png" width="500"/>
</p>

# TUEplots: Extend matplotlib for scientific publications

[![PyPi Version](https://img.shields.io/pypi/v/tueplots.svg?style=flat-square)](https://pypi.org/project/tueplots/)
[![Docs](https://readthedocs.org/projects/pip/badge/?version=latest&style=flat-square)](https://github.com/pnkraemer/tueplots)
[![GitHub stars](https://img.shields.io/github/stars/pnkraemer/tueplots.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/pnkraemer/tueplots)
[![gh-actions](https://img.shields.io/github/workflow/status/pnkraemer/tueplots/ci?style=flat-square)](https://github.com/pnkraemer/tueplots/actions?query=workflow%3Aci)
<a href="https://github.com/pnkraemer/tueplots/blob/master/LICENSE"><img src="https://img.shields.io/github/license/pnkraemer/tueplots?style=flat-square&color=2b9348" alt="License Badge"/></a>



## Why?

`tueplots` helps you to create scientific plots that can be used in papers, presentations, posters, or other publications.
`tueplots` does not try to make your plots as beautiful as possible (who are we to judge your favourite color).
Instead, it makes it effortless to avoid common issues like too-small figures, inappropriate fontsizes, or inconsistencies among figures.
Because good-looking figures _are_ important. 

For example, consider the style tailored to the ICML2022 template.
(Left: default matplotlib, middle: one line of tueplots-code, right: two lines of tueplots-code)

<p align="center">
<img src="./_img/before.png" width="200"/>
<img src="./_img/after1.png" width="200"/>
<img src="./_img/after2.png" width="200"/>
</p>


## Principles

**`tueplots` has no internal state:**
It only passes around dictionaries, whose key-value pairs match those that matplotlib uses.
Instead of updating global state, it makes it easy for you to do it yourself! 
If you want to globally change settings, pass them to `matplotlib.pyplot.rcParams.update()`.
If you only need them for specific contexts, pass them to `matpltlib.pyplot.rc_context()`.
`tueplots` makes the change easy, so you can make the easy change. This should make `tueplots` naturally compatible with other matplotlib extensions.
Usage examples are given below.


**`tueplots` has no opinions:**
It does not tell you what your figures should like like in the end, but helps you to tailor your plots to your own needs.
We like all the colors, frame-styles, markers, or linewidths.
But we _do_ think that figure sizes should match the text-width in your publication, 
and that the font-size in the plot should be readable, and similar to the rest of the paper/presentation/....

## Getting started 

[**Installation**](https://tueplots.readthedocs.io/en/latest/quickstart/installation.html) | [**Usage examples**](https://tueplots.readthedocs.io/en/latest/quickstart/usage_example.html)

## ICML 2022
If you're getting ready to submit your paper to ICML 2022, plug either of the following into your preamble. 
The signatures are interchangeable.
```python 
>>> import matplotlib.pyplot as plt
>>> from tueplots import bundles
>>> bundles.icml2022()
{'axes.labelsize': 8,
 'axes.titlesize': 8,
 'figure.autolayout': False,
 'figure.constrained_layout.use': True,
 'figure.figsize': (3.25, 2.0086104634371584),
 'font.family': 'sans-serif',
 'font.size': 8,
 'legend.fontsize': 6,
 'text.latex.preamble': '\\usepackage{times} '
                        '\\renewcommand{\\familydefault}{\\sfdefault} '
                        '\\usepackage{sansmath} \\sansmath',
 'text.usetex': True,
 'xtick.labelsize': 6,
 'ytick.labelsize': 6}
>>> bundles.icml2022(family="sans-serif", usetex=False, column="full", nrows=2)
{'axes.labelsize': 8,
 'axes.titlesize': 8,
 'figure.autolayout': False,
 'figure.constrained_layout.use': True,
 'figure.figsize': (6.75, 8.343458848123582),
 'font.family': 'sans-serif',
 'font.serif': ['Times'],
 'font.size': 8,
 'legend.fontsize': 6,
 'mathtext.bf': 'Times:bold',
 'mathtext.fontset': 'stix',
 'mathtext.it': 'Times:italic',
 'mathtext.rm': 'Times',
 'text.usetex': False,
 'xtick.labelsize': 6,
 'ytick.labelsize': 6}
>>>
>>> # Plug any of those into either the rcParams or into an rc_context:
>>> plt.rcParams.update(bundles.icml2022())
>>> with plt.rc_context(bundles.icml2022()):
...     pass
```
If you don't want a pre-packaged solution, at least fix your figure- and font-sizes as follows.
```python
>>> from tueplots import figsizes, fontsizes, fonts
>>> figsizes.icml2022_full()
{'figure.autolayout': False,
 'figure.constrained_layout.use': True,
 'figure.figsize': (6.75, 2.0858647120308955)}
>>> figsizes.icml2022_half(nrows=2, constrained_layout=True, tight_layout=False)
{'figure.autolayout': False,
 'figure.constrained_layout.use': True,
 'figure.figsize': (3.25, 4.017220926874317)}
>>> fontsizes.icml2022()
{'axes.labelsize': 8,
 'axes.titlesize': 8,
 'font.size': 8,
 'legend.fontsize': 6,
 'xtick.labelsize': 6,
 'ytick.labelsize': 6}
>>> fonts.icml2022()
{'font.family': 'serif',
 'font.serif': ['Times'],
 'mathtext.bf': 'Times:bold',
 'mathtext.fontset': 'stix',
 'mathtext.it': 'Times:italic',
 'mathtext.rm': 'Times',
 'text.usetex': False}
>>> fonts.icml2022(family="serif")
{'font.family': 'serif',
 'font.serif': ['Times'],
 'mathtext.bf': 'Times:bold',
 'mathtext.fontset': 'stix',
 'mathtext.it': 'Times:italic',
 'mathtext.rm': 'Times',
 'text.usetex': False}
>>> fonts.icml2022_tex(family="sans-serif")
{'font.family': 'sans-serif',
 'text.latex.preamble': '\\usepackage{times} '
                        '\\renewcommand{\\familydefault}{\\sfdefault} '
                        '\\usepackage{sansmath} \\sansmath',
 'text.usetex': True}
```
and if you want to give your plots a makeover (albeit a slightly opinionated one) with a single line of code,
consider the `axes.lines()` setting.
```python
>>> from tueplots import axes
>>> axes.lines()
{'axes.axisbelow': True,
 'axes.linewidth': 0.5,
 'grid.linewidth': 0.5,
 'legend.edgecolor': 'inherit',
 'lines.linewidth': 1.0,
 'patch.linewidth': 0.5,
 'xtick.major.size': 3.0,
 'xtick.major.width': 0.5,
 'xtick.minor.size': 2.0,
 'xtick.minor.width': 0.25,
 'ytick.major.size': 3.0,
 'ytick.major.width': 0.5,
 'ytick.minor.size': 2.0,
 'ytick.minor.width': 0.25}
>>> axes.lines(base_width=0.5)
{'axes.axisbelow': True,
 'axes.linewidth': 0.5,
 'grid.linewidth': 0.5,
 'legend.edgecolor': 'inherit',
 'lines.linewidth': 1.0,
 'patch.linewidth': 0.5,
 'xtick.major.size': 3.0,
 'xtick.major.width': 0.5,
 'xtick.minor.size': 2.0,
 'xtick.minor.width': 0.25,
 'ytick.major.size': 3.0,
 'ytick.major.width': 0.5,
 'ytick.minor.size': 2.0,
 'ytick.minor.width': 0.25}
```

## Troubleshooting

#### My version of matplotlib cannot find font XYZ?!
Some of the fonts that `tueplot` provides (e.g., `Times` or `Roboto`) needs to be installed on your machine before matplotlib can find it.
This means that you need to find a `.ttf` file online (e.g., `Roboto` family is available at Google fonts: https://fonts.google.com/specimen/Roboto),
download it, and install it. For Ubuntu, this means opening the file (with your font manager) and clicking `install`.
There are probably many other ways to do this.
Once the font is installed, delete your matplotlib cache (usually: `rm ~/.cache/matplotlib -rf`) and restart your notebook (not just the kernel).
See also https://stackoverflow.com/questions/42097053/matplotlib-cannot-find-basic-fonts/42841531.

## Examples 
To run the examples, additional dependencies need to be installed via 
```
pip install .[examples]
```
For example: `jupyter`.

## Contribution

Install `tueplots` with all ci-related dependencies via
```
pip install .[ci]
```
Run all checks via
```
tox
```
or only run the tests via
```
tox -e pytest
```
or use tox (which also runs the linter, and the python-code-snippets in this readme).
```
tox
```
The CI checks for compliance of the code with black and isort, and runs the tests and the notebooks.
To automatically satisfy the former, there is a pre-commit that can be used (do this once):
```
pip install pre-commit
pre-commit install
```
From then on, your code will be checked for isort and black compatibility automatically. 


## Related packages
There are similar packages to `tueplots` (with different foci, respectively):
* Seaborn: https://seaborn.pydata.org/index.html
* ProPlot: https://proplot.readthedocs.io/en/latest/cycles.html
* SciencePlots: https://github.com/garrettj403/SciencePlots
* MatplotX: https://github.com/nschloe/matplotx
* Themepy: https://github.com/petermckeeverPerform/themepy

If you know of any others, please open an issue/PR. 


# Miscellanous

`tueplots`has been developed at the University of Tübingen (hence the name).
