# Contributing to qrm-resources

## Before You Start

Please read through the
[MiaowWare CONTRIBUTING.md](https://github.com/miaowware/.github/blob/master/CONTRIBUTING.md).

## Image Processing Requirements

Contributed images (especially ones with lots of flat colours) should be processed
with [pngquant](https://pngquant.org) to improve the file size.
`pngquant --quality 30-40` is a good default. If this causes artifacts like extreme
dithering or posterising, a higher `--quality` can be used. If an image still has a
large file size, it can be downscaled, but this is not optimal.

## Updating the Resource Index

After making changes to `index.json` or files directly tracked in `index.json`, run
the `gethashes.py` script to update the metadata in `resources/index.json`. This should
be committed with your changes.
