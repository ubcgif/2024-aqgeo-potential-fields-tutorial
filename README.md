# Potential fields tutorial for AQGEO 2024 Meeting

## Information

|                            | **Information**                                                      |
| -------------------------- | -------------------------------------------------------------------- |
| When                       | November 7, 2024                                                     |
| Slides (web)               | [ubcgif.github.io/2024-aqgeo-potential-fields-tutorial][slides]      |
| Slides (PDF)               | [slides.pdf][slides-pdf]                                             |
| Forward modelling notebook | [notebooks/forward.ipynb](notebooks/forward.ipynb)                   |
| Inversion notebook         | [notebooks/inversion-sparse.ipynb](notebooks/inversion-sparse.ipynb) |

## How to see slides

Slides are being hosted in GitHub Pages, you can see them by visiting
[ubcgif.github.io/2024-aqgeo-potential-fields-tutorial][slides].

Alternatively, you can download this repository as a [zip file][repo-zip], or
clone it with `git`:

```bash
git clone https://github.com/ubcgif/2024-aqgeo-potential-fields-tutorial
```

And then serve them locally by opening the `index.html` file in your browser,
or running a local web server with:

```bash
python -m http.server
```

or

```bash
livereload
```

These commands will provide you a URL you can open in your browser to see
the slides.

## How to run the notebooks

### Install a Python distribution

In order to run the notebooks you need to install a Python distribution like
[Miniforge][miniforge], [Anaconda][anaconda] or [Miniconda][miniconda].

Follow the instructions provided by any of them to install it in your system.

> [!NOTE]
> In the following steps we'll instruct you to run some commands. They are
> meant to be run in a terminal (for Mac and Linux users), or in an Anaconda
> Prompt or Miniforge Prompt if you are running Windows.

### Download the repository

Then, download this repository as a [zip file][repo-zip], or clone it with `git`:

```bash
git clone https://github.com/ubcgif/2024-aqgeo-potential-fields-tutorial
```

### Create a new conda environment

In the downloaded folder you'll find an `environment.yml` file that you can use
to create a conda environment by running:

```bash
conda env create -f environment.yml
```

Once the new environment is created and all the packages are installed, we need
to activate the environment with:

```bash
conda activate aqgeo-2024-potential-fields
```

## Run JupyterLab

After we activated the environment, let's start JupyterLab, where we can open,
edit and execute the notebooks:

```bash
jupyterlab
```

I will automatically open a new tab in your browser with the Jupyter Lab, where
you can navigate into the `notebooks` folder and open any of the notebooks
you'll find there.

> [!IMPORTANT]
> It's important not to close the terminal (or Prompt) window while you are
> using Jupyter Lab. Closing the terminal will make Jupyter Lab to quit.

## License

The slides and their content are provided under the [CC-BY License](LICENSE).

The code under the `notebooks` folder is provided under the [MIT
License](notebooks/LICENSE).

[slides]: https://ubcgif.github.io/2024-aqgeo-potential-fields-tutorial
[slides-pdf]: N/A
[anaconda]: https://anaconda.org
[miniconda]: https://docs.anaconda.com/miniconda/miniconda-install
[miniforge]: https://github.com/conda-forge/miniforge
[repo-zip]: https://github.com/ubcgif/2024-aqgeo-potential-fields-tutorial/archive/refs/heads/main.zip
