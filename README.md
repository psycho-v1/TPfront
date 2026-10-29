# TPfront

Invoice footer and company seal for Tropical Fruits Pvt Ltd in Manager.io.

## Use it

Open `dist/footer.html`, copy everything, and paste it into the footer field in Manager.io.

The seal is embedded in the code because Manager.io's PDF export does not load images from links.
The seal has been resized to 300 px, so the footer is about 90% shorter than the original.

`dist/footer-url.html` loads the seal from this repo instead. It is shorter still, but the seal will
be missing from PDFs, so only use it if Manager.io starts loading outside images.

## Change it

- Text (terms, bank details): edit `src/footer.template.html`
- Seal: replace `src/seal.jpg`

Then run `python build.py`, or just push to `main` and the GitHub Action rebuilds `dist/` for you.
