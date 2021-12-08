"""Font settings for conference papers and journals."""
from . import colors


def neurips(*, usetex=False, family="serif"):
    return {
        "text.usetex": usetex,
        "font.serif": ["Times New Roman"],
        "mathtext.fontset": "custom",
        "mathtext.rm": "Times New Roman",
        "mathtext.it": "Times New Roman:italic",
        "mathtext.bf": "Times New Roman:bold",
        "font.family": family,
    }


def icml(*, usetex=False, family="serif"):
    return {
        "text.usetex": usetex,
        "font.serif": ["Times"],
        "mathtext.fontset": "custom",
        "mathtext.rm": "Times",
        "mathtext.it": "Times:italic",
        "mathtext.bf": "Times:bold",
        "font.family": family,
    }


def beamer_moml():
    """For use with the MoML beamer template."""
    return {
        "font.serif": ["Roboto Condensed"],
        "font.family": "serif",
        "text.color": colors.tue_dark(),
        "axes.edgecolor": colors.tue_dark(),
        "axes.labelcolor": colors.tue_dark(),
        "xtick.color": colors.tue_dark(),
        "ytick.color": colors.tue_dark(),
        "axes.facecolor": "none",
        "axes.titlesize": "medium",
        "grid.color": colors.tue_gray(),
        "axes.grid": False,
    }


def beamer_moml_dark_bg():
    """Colors for dark beamer slides."""
    return {
        "font.serif": ["Roboto Condensed"],
        "font.family": "serif",
        "text.color": "w",
        "axes.edgecolor": "w",
        "axes.labelcolor": "w",
        "xtick.color": "w",
        "ytick.color": "w",
        "axes.facecolor": "none",
    }
