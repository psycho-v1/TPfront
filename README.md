# TPfront

Invoice footer and company seal for Tropical Fruits Pvt Ltd in Manager.io.

## Use it

Open `dist/footer.html`, copy everything, and paste it into the footer field in Manager.io.

The seal is embedded in the code because Manager.io's PDF export does not load images from links.
The seal has been resized to 300 px, so the footer is about 90% shorter than the original.

`dist/footer-url.html` loads the seal from this repo instead. It is shorter still, but the seal will
be missing from PDFs, so only use it if Manager.io starts loading outside images.

## Modern theme

`theme/theme.html` is a full document theme for Manager.io in the seal's green: header band,
a "Bill to" card, a green item table, a highlighted grand total and a status badge (Paid, Overdue, etc.).
It works for invoices, quotes, orders, receipts and reports.

1. In Manager.io go to **Settings → Themes → New Theme**, paste the whole of `theme/theme.html`, and save.
2. Use `dist/footer-modern.html` as the footer. It matches the theme's colours.
3. Pick the theme on your invoices (or set it as the default theme).

## Tax Invoice theme

`theme/tax-invoice.html` is a second theme, built separately:

- Company ("From") and customer ("Bill to") side by side on one row
- The title shows **TAX INVOICE** whenever any line item has tax (e.g. GST 8%), and plain **INVOICE** otherwise
- Issue and due dates in a strip under the parties, green rule-style item table, large green grand total

- The Tropical Fruits logo (`brand/logo.svg`) is built into the theme and always shows at the top; the seal appears only in the footer

Install it the same way: **Settings → Themes → New Theme**, paste the whole file, save, and pick it on your invoices.
It pairs with `dist/footer-modern.html`.

## Logo files

`brand/` holds the cleaned-up logo, traced from the original into a vector so it stays sharp at any size:

- `logo.svg` - vector, use this wherever possible (website, print, signage)
- `logo-2000.png` - 2000 px wide, transparent background
- `logo-2000-white-bg.png` - 2000 px wide, white background
- `logo-600.png` - 600 px wide, transparent background (email signatures, social media)

## Change it

- Text (terms, bank details): edit `src/footer.template.html` (classic) or `src/footer-modern.template.html` (modern)
- Seal: replace `src/seal.jpg`
- Tax Invoice theme layout: edit `src/tax-invoice.template.html` (the build writes `theme/tax-invoice.html`)
- Logo: replace `brand/logo.svg`

Then run `python build.py`, or just push to `main` and the GitHub Action rebuilds `dist/` for you.
